import boto3

def upload_to_s3(file_path, bucket_name, object_key):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_path, bucket_name, object_key)
        print(f"Uploaded {file_path} to s3://{bucket_name}/{object_key}")
    except Exception as e:
        print(f"Upload failed: {e}")

# Example usage
upload_to_s3('data/sample_data.csv', 'my-etl-pipeline-data', 'incoming/sample_data.csv')