from google.cloud import storage 
import io, os
from zipfile import ZipFile, is_zipfile   
import tarfile, time

from google.cloud.storage.blob import Blob
    
class Search_Engine():
    def upload_to_bucket(self, files, bucket_name):
        storage_client = storage.Client()

        # get the bucket, or create a new one for the first time
        try: 
            new_bucket = storage_client.get_bucket(bucket_name)
        except:
            bucket = storage_client.bucket(bucket_name)
            new_bucket = storage_client.create_bucket(bucket, location='us')

        # upload files
        for f in files:
        #     if '.tar.gz' in f:
        #         file_object = tarfile.open(f)
        #         file_object.extractall('./data')
        #         print(file_object)
        #         if file_object:
            blob = new_bucket.blob('data/' + f.split('/')[-1])
            blob.upload_from_filename(f)

        self.decompress_zip(new_bucket, files)


    def decompress_zip(bucket, files):
        for f in files:
            if '.tar.gz' in f:
                input_blob = bucket.get_blob('data/' + f.split('/')[-1])
                # blob = bucket.get_blob('data/').download_as_string()
                
                # Turn the upload file into a tar file
                tar = tarfile.open(fileobj=io.BytesIO(input_blob.download_as_string()))

                # Iterate over all files in the tar file
                for member in tar.getnames():
                    # Extract the individual file
                    file_object = tar.extractfile(member)

                    # Check if it's a file or directory (which should be skipped)
                    if file_object:
                        print(member)
                        # output_file = f'./{contentfilename.split("/")[-1]}'

                        # Create a new blob instance in the output bucket
                        output_blob = bucket.blob(os.path.join('data/', member))

                        # Write the contents of the file to the output blob
                        output_blob.upload_from_string(file_object.read())
                        # input_blob.delete()
            
        # zipbytes = io.BytesIO(blob.download_as_string())

        # if is_zipfile(zipbytes):
        #     with ZipFile(zipbytes, 'r') as myzip:
        #         for contentfilename in myzip.namelist():
        #             contentfile = myzip.read(contentfilename)
         
        #             output_file = f'./{contentfilename.split("/")[-1]}'
        #             print(output_file)
        #             outfile = open(output_file, 'wb')
        #             outfile.write(contentfile)
        #             outfile.close()

        #             blob = bucket.blob(
        #                 f'{output_file.rstrip(".zip")}/{contentfilename}'
        #             )
        #             with open(output_file, "rb") as my_pdf:
        #                 blob.upload_from_file(my_pdf)

        #                 # make the file publicly accessible
        #                 blob.make_public()

    def inverted_index(self, word):
        fpath = 'result/inverted'
        output = {}

        # while not os.path.exists(fpath): 
        #    time.sleep(1)
        
        lines = open(fpath, 'r').readlines()

        for line in lines:
            if word in line:
                key, value = line.split('\t')
                output[key] = value

        output = dict(sorted(output.items(), key=lambda item: item[1]))
        return output
