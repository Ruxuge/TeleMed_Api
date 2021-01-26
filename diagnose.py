from __future__ import print_function

from google.cloud import automl_v1, automl

import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"


def main(path):
    project_id = "telemed-300210"
    model_id = "ICN2967249830855835648"

    file_path = path

    with open(file_path, 'rb') as ff:
        content = ff.read()

    get_prediction(content, project_id, model_id)


# 'content' is base-64-encoded image data.
def get_prediction(content, project_id, model_id):
    prediction_client = automl_v1.PredictionServiceClient()

    model_full_id = automl.AutoMlClient.model_path(
        project_id, "us-central1", model_id)

    payload = {'image': {'image_bytes': content}}
    params = {}
    request = prediction_client.predict(name=model_full_id, payload=payload, params=params)
    print("Prediction results:")
    for result in request.payload:
        print("Predicted entity label: {}".format(result.display_name))
        print("\n")
        var = result.display_name
        return var

