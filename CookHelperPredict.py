from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os

# Get path to images folder
dirname = os.path.dirname(__file__)
images_folder = os.path.join(dirname, 'images/Test')

trainer = CustomVisionTrainingClient(endpoint=endpoint, credentials=credentials)
projects = trainer.get_projects()

for proj in projects:
    print("\t",proj.id,"\t", proj.name)

# Create variables for your project
publish_iteration_name = "Iteration1"
project_id = "<YOUR_PROJECT_ID>"


# Create variables for your prediction resource
prediction_key = "<YOUR_KEY>"
endpoint = "<YOUR_ENDPOINT>"
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(endpoint, prediction_credentials)
# Open an image and make a prediction
with open(os.path.join(images_folder, "tigerlily4.jpg"), "rb") as image_contents:
    results = predictor.classify_image(project_id, publish_iteration_name, image_contents.read())
# Display the results
for prediction in results.predictions:
    print(f"{prediction.tag_name}: {prediction.probability * 100 :.2f}%")
