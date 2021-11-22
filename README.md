# Mini-Search-Engine
14848 Cloud Infra Course Project


## Step by Step Demo
1. When the engine first starts, the user is given the options to choose files. 
![alt text](gui_demo/homepage.png?raw=true "homepage")


2. When the user clicks on the `Choose Files` button, a file explorer window will pop up. 
    ![alt text](gui_demo/file_explorer_window.png?raw=true "file_explorer_window")

3. If no file is selected, and the user clicks on the `Construct Inverted Indices` button, a warning will appear.
    ![alt text](gui_demo/no_file_selected.png?raw=true "no_file_selected")
    
    Otherwise, the files will be uploaded to and stored in a GCP busket named "14848-project-bucket". A search engine will be started to perform operations including searching for a specific term and finding top-N frequent words.
    ![alt text](gui_demo/engine_loaded.png?raw=true "engine_loaded")


## Commands to Run the Application
- Step run the client-side application: 
```
docker pull xuranliu/search-engine
docker run -e GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH" xuranliu/search-engine
```

- Commands to create docker image:
```
docker build -t xuranliu/search-engine ./src
docker push xuranliu/search-engine
```


## Steps Connecting to GCP
1. Create a service account under the current project by following steps in the [tutorial](https://cloud.google.com/docs/authentication/getting-started#creating_a_service_account).

2. Use the command ``export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"`` to set the  environmenal variable for local development.

3. Connect to GCP storage.
```
from google.cloud import storage  
storage_client = storage.Client()
```

4. Create a new bucket named `14848-project-bucket` if it does not already existed; otherwise, get the specified bucket, and upload files.
```
try: 
    new_bucket = storage_client.get_bucket("14848-project-bucket")
except:
    bucket = storage_client.bucket("14848-project-bucket")
    new_bucket = storage_client.create_bucket(bucket, location="us")
```

