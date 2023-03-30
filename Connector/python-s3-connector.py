import boto3
from datetime import date
from multiprocessing import Process
from botocore.exceptions import ClientError


def file_move(key,value,bucket_name):
    s3 = boto3.resource("s3")
    back_up_folder_name = "backup/" + str(date.today())
    copy_source = {
        "Bucket": "pyspark-learning-bucket",
        "Key": key
    }
    new_file_path = back_up_folder_name + '/' + value
    try:
        s3.meta.client.copy(copy_source, bucket_name, new_file_path)
        s3.Object(bucket_name, key).delete()
        print(key + " is successfully moved to archive folder")
    except ClientError as e:
        print(e.response["Error"]["Code"])



if __name__ =="__main__":
    try:

        s3 = boto3.resource("s3")
        # printing all bucket name
        '''
        for bucket in s3.buckets.all():
            print(bucket)
        '''

        # reading objects in the specific bucket

        new_dict ={}
        bucket_name ='pyspark-learning-bucket'
        for obj in s3.Bucket(bucket_name).objects.filter(Prefix='Ingress'):
            file_path = obj.key
            if len(file_path.split("/")) >1 and file_path.split("/")[-1] !="":
                new_dict[file_path] = file_path.split("/")[-1]

        for key, value in new_dict.items():
            p = Process(target=file_move, args=(key,value,bucket_name))
            p.start()
            p.join()


    except ClientError as e:
        print(e.response["Error"]["Code"])






