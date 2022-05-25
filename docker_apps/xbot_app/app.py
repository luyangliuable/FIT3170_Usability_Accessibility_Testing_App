
import boto3
import os
import subprocess
import pathlib
from flask import Flask, request, jsonify


app = Flask(__name__)

# aws info for development environment
AWS_REGION = 'us-west-2'
AWS_PROFILE = 'localstack'
ENDPOINT_URL = os.environ.get('S3_URL')

# aws s3 client
boto3.setup_default_session(profile_name=AWS_PROFILE)
s3_client = boto3.client("s3", region_name=AWS_REGION,
                         endpoint_url=ENDPOINT_URL)

# home route
@app.route('/')
def home():
    return "Story distiller app is live."

# route for starting new job
@app.route("/new_job", methods=["POST"])
def send_uid_and_signal_run():
    if request.method == "POST":
        try:
            print('NEW JOB FOR UUID: ' + request.get_json()["uid"])
            uid = request.get_json()["uid"]
        except:
            return 'Invalid uuid data'

        _service_execute(uid)

        return jsonify( {"result": "SUCCESS"} ), 200


    return "No HTTP POST method received"


def _service_execute(uuid):
    print('Beginning new job for %s' % uuid)
    apk_name = _get_apk_name(uuid)

    # backup original source code
    subprocess.run(["cp", "-r", "/home/Xbot-main", "/home/tmp/Xbot-main"])

    _get_data(uuid, apk_name)
    print('APK name for %s is %s' % (uuid, apk_name))

    print('Running Xbot')
    _process_result()
    print('Successfully ran')

    print('Uploading results')
    _upload_result(uuid, apk_name)
    print('Successfully uploaded')

    # restore original source code
    subprocess.run(["rm", "-r", "/home/Xbot-main"])
    subprocess.run(["cp", "-r", "/home/tmp/Xbot-main", "/home/Xbot-main"])
    subprocess.run(["rm", "-r", "/home/tmp/Xbot-main"])
    print('Job for %s complete' % uuid)

# get name of file stored where key==uuid in s3
def _get_apk_name(uuid):
    response = s3_client.list_objects_v2(Bucket='apk-bucket', Prefix=uuid)
    contents = response['Contents']
    apk_name = contents[0]['Key'].replace(uuid+'/', '').replace('.apk', '')
    return apk_name

# get the required inputs from s3
def _get_data(uuid, apk_name):
    filepath = '/home/Xbot-main/main-folder/apks/%s.apk' % apk_name
    s3_client.download_file('apk-bucket', '%s/%s.apk' % (uuid, apk_name), filepath)

# run the algorithm
def _process_result():
    os.chdir("/home/Xbot-main/code")
    subprocess.run(["python", "run_xbot.py"])
    os.chdir("/home/app")

# upload results to s3
def _upload_result(uuid, apk_name):

    bucket = 'xbot-bucket'
    output_root_path = '/home/Xbot-main/main-folder/results/outputs/'

    # upload output folder zip
    output_filename = 'xbot_output_%s.zip' % apk_name
    os.chdir(output_root_path)
    os.system('zip -r %s %s' % (output_filename, apk_name))

    output_folder_path = output_root_path + output_filename
    s3_output_path = 'output-full/%s/%s' % (uuid, output_filename)
    s3_client.upload_file(output_folder_path, bucket, s3_output_path)
    os.system('rm -r %s' % (output_filename))
    os.chdir("/home/app")
    

    # upload issues (image and text description file)
    issues_root_path = output_root_path + apk_name + '/issues'
    s3_issues_path = 'issues/%s' % uuid

    for (root, _, filenames) in os.walk(issues_root_path):
        for file in filenames:
            issue_name = file[:-4]
            if (pathlib.Path(file).suffix == '.png'):
                s3_client.upload_file(os.path.join(root,file), bucket, s3_issues_path+'/%s/image/%s' % (issue_name, file))
            if (pathlib.Path(file).suffix == '.png'):
                s3_client.upload_file(os.path.join(root,file), bucket, s3_issues_path+'%s/text/%s' % (issue_name, file))


if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0", port=3003)
    
    # test run
    #_service_execute('a2dp.Vol_133')
