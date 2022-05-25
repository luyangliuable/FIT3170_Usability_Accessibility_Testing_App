import boto3
import os
import subprocess
from PIL import Image
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

# executing new job
def _service_execute(uuid):
    print('Beginning new job for %s' % uuid)

    # backup original source code
    subprocess.run(["cp", "-r", "/home/OwlEye-main", "/home/tmp/OwlEye-main"])

    print('Downloading images from storydistiller')
    _get_data(uuid)
    print('Successfully Downloaded')
    
    print('Running OwlEye')
    _process_result()
    print('Successfully ran')
    
    print('Uploading results')
    _upload_result(uuid)
    print('Successfully uploaded')

    # restore original source code
    subprocess.run(["rm", "-r", "/home/OwlEye-main"])
    subprocess.run(["cp", "-r", "/home/tmp/OwlEye-main", "/home/OwlEye-main"])
    subprocess.run(["rm", "-r", "/home/tmp/OwlEye-main"])

    print('Job for %s complete' % uuid)

# get the inputs from s3
def _get_data(uuid):
    tmp_dir = '/home/OwlEye-main/tmp/input_png/'
    os.system('mkdir -p %s' % tmp_dir)
    dest_dir = '/home/OwlEye-main/input_pic/'

    bucketname = 'storydistiller-bucket'
    prefix = 'screenshots/%s/' % uuid
    response = s3_client.list_objects_v2(Bucket=bucketname, Prefix=prefix)
    for object in response['Contents']:
        filename = object['Key'].replace(prefix, '')
        print(filename)
        print(bucketname)
        print(prefix+filename)
        print(tmp_dir+filename)
        s3_client.download_file(bucketname, prefix+filename, tmp_dir+filename)

    _process_png_to_jpg(tmp_dir, dest_dir)
    os.system('rm -r %s' % tmp_dir)

# Process pictures from png to jpeg
def _process_png_to_jpg(raw_dir, image_dir):
    """
    Using PIL converts images from png to jpg
    """
    raw_pics = os.listdir(raw_dir)
    for raw_png in raw_pics:
        (filename, extension) = os.path.splitext(raw_png)
        if extension != ".txt":
            raw_png_dir = raw_dir + raw_png
            pil_jpg = Image.open(raw_png_dir, mode='r')

            pil_jpg__dir = image_dir + filename+".jpg"
            pil_jpg.convert('RGB').save(pil_jpg__dir,'JPEG')

# run the algorithm
def _process_result():
    os.chdir("/home/OwlEye-main")
    subprocess.run(["python3", "localization.py"])
    os.chdir("/home/app")

# upload results to s3
def _upload_result(uuid):

    results_path = "/home/OwlEye-main/output_pic"
    bucketname = "owleye-bucket"
    s3_results_path = "results/%s/" % uuid

    for (root, _, filenames) in os.walk(results_path):
        for file in filenames:
            print(file)
            s3_client.upload_file(os.path.join(root,file), bucketname, s3_results_path+file)
            


if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0", port=3004)
    
    # test run
    #service_execute('a2dp.Vol_133')