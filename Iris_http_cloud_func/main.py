import numpy as np
import pandas as pd
import os
import pickle
from google.cloud import storage


## Gloabl model variable
model = None


# Download model file from cloud storage bucket
def download_model_file():

    from google.cloud import storage

    # Model Bucket details
    BUCKET_NAME        = "YOUR_MODEL_BUCKET_NAME"
    PROJECT_ID         = "YOUR_GCP_PROJECT_ID"
    GCS_MODEL_FILE     = "MODEL_FILE_NAME.pkl"

    # Initialise a client
    client   = storage.Client(PROJECT_ID)
    
    # Create a bucket object for our bucket
    bucket   = client.get_bucket(BUCKET_NAME)
    
    # Create a blob object from the filepath
    blob     = bucket.blob(GCS_MODEL_FILE)
    
    folder = '/tmp/'
    if not os.path.exists(folder):
      os.makedirs(folder)
    # Download the file to a destination
    blob.download_to_filename(folder + "local_model.pkl")


# Main entry point for the cloud function
def iris_predict(request):

    # Use the global model variable 
    global model

    if not model:

        download_model_file()
        model = pickle.load(open("/tmp/local_model.pkl", 'rb'))
    
    
    # Get the features sent for prediction
    params = request.get_json()

    if (params is not None) and ('features' in params):
        # Run a test prediction
        pred_species  = model.predict(np.array([params['features']]))
        return pred_species[0]
        
    else:
        return "nothing sent for prediction"
