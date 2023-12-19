  import boto3





s3Resource = boto3.resource('s3')

def upload_file(file_name, s3_file_location):
    try:


      
        s3Resource.meta.client.upload_file(file_name,'damaimlbkt',s3_file_location)
    except Exception as exp:


      
        print('exp: ', exp)

file_name="Handshake.zip"
s3_file_location="images/batches/batch1/"
upload_file(file_name, s3_file_location)
