
import boto3
import os
import subprocess
import pathlib


AWS_REGION = 'us-west-2'
AWS_PROFILE = 'localstack'
ENDPOINT_URL = os.environ.get('S3_URL')

boto3.setup_default_session(profile_name=AWS_PROFILE)
s3_client = boto3.client("s3", region_name=AWS_REGION,
                         endpoint_url=ENDPOINT_URL)


def service_execute(uuid):
    apk_name = _get_apk_name(uuid)

    # backup original source code
    subprocess.run(["cp", "-r", "/home/Xbot-main", "/home/tmp/Xbot-main"])

    _get_data(uuid, apk_name)

    _process_result()

    _upload_result(uuid, apk_name)

    # restore original source code
    subprocess.run(["rm", "-r", "/home/Xbot-main"])
    subprocess.run(["cp", "-r", "/home/tmp/Xbot-main", "/home/Xbot-main"])
    subprocess.run(["rm", "-r", "/home/tmp/Xbot-main"])

# get name of file stored where key==uuid in s3
def _get_apk_name(uuid):
    response = s3_client.list_objects_v2(Bucket='apk-bucket')
    contents = response['Contents']
    apk_name = contents[0]['Key']
    return apk_name

# get the required inputs from s3
def _get_data(uuid, apk_name):
    filepath = '/home/Xbot-main/main-folder/apks/%s.apk' % apk_name
    s3_client.download_file('apk-bucket', uuid, filepath)

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
    # test run
    service_execute('a2dp.Vol_133')
