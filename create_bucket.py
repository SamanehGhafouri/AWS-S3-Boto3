import boto3
import uuid

s3_resource = boto3.resource('s3')


def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])


def create_bucket(bucket_prefix, s3_connection):

    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(Bucket=bucket_name)
    print(bucket_name)
    return bucket_name, bucket_response


if __name__ == '__main__':
    first_bucket_name, first_response = create_bucket(bucket_prefix='firstpythonbucket', s3_connection=s3_resource.meta.client)
    print(first_response)
    print('-----------------------------------------------------------')

    second_bucket_name, second_response = create_bucket(bucket_prefix='secondpythonbucket', s3_connection=s3_resource)
    print(second_response)
