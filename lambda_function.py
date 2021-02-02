
import logging
import boto3
from botocore.exceptions import ClientError

lifecycle_config_settings = {
    'Rules': [
        {'ID': 'Delete Rule',
         'Filter': {'Prefix': ''},
         'Status': 'Enabled',
         'Expiration': { 'Days':100 }}
    ]}


def put_bucket_lifecycle_configuration(bucket_name, lifecycle_config):
    """Set the lifecycle configuration of an Amazon S3 bucket

    :param bucket_name: string
    :param lifecycle_config: dict of lifecycle configuration settings
    :return: True if lifecycle configuration was set, otherwise False
    """

    # Set the configuration
    s3 = boto3.client('s3')
    try:
        s3.put_bucket_lifecycle_configuration(Bucket=bucket_name,
                                              LifecycleConfiguration=lifecycle_config)
    except ClientError as e:

        return False
    return True

def lambda_handler(event, context):
    # TODO implement
    print('Event: {}'.format(event))
    print('This is the bucket name: {}'.format(event.get('detail').get('requestParameters').get('bucketName')))
    
    bucket_name = (event.get('detail').get('requestParameters').get('bucketName'))
    #print(event)
   

    success = put_bucket_lifecycle_configuration(bucket_name,lifecycle_config_settings)

    if success:
    #  logging.info('The lifecycle configuration was set for {test_bucket_name}')
        print('The lifecycle configuration was set for {bucket_name}')
