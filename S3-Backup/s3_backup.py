import boto3
import uuid

s3 = boto3.resource("s3")
def upload_backup(s3, file_name, bucket_name, key_name):
    data = open(file_name, 'rb') #reads the data in binary format, cause in when uploading data to an S3 bucket the data is read in binary format
    s3.Bucket(bucket_name).put_object(Key=key_name, Body = data)
    print("Uploaded!")

file_name = #Enter the file name to be backed up, it should be present in your repository
bucket_name = # Enter your Bucket name
key_name = "backup " +str(uuid.uuid4()) +".tar.gz"

upload_backup(s3, file_name,bucket_name, key_name)