from google.cloud import storage    
    
class Search_Engine():
    def upload_to_bucket(files):
        storage_client = storage.Client()

        # get the bucket, or create a new one for the first time
        try: 
            new_bucket = storage_client.get_bucket("14848-project-bucket")
        except:
            bucket = storage_client.bucket("14848-project-bucket")
            new_bucket = storage_client.create_bucket(bucket, location="us")

        # upload files
        for f in files:
            blob = new_bucket.blob(f.split("/")[-1])
            blob.upload_from_filename(f.split("/")[-1])
            
    