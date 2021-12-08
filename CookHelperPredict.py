from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os

# Get path to images folder
dirname = os.path.dirname(__file__)
images_folder = os.path.join(dirname, 'Test')

# Create variables for your project
publish_iteration_name = "CookHelperPub"
project_id = "f4ec7aed-3c70-4698-a41c-bde9ce39b2e5"


# Create variables for your prediction resource
prediction_key = "546ce298309f4867b39e7d18edbde621"
endpoint = "https://northeurope.api.cognitive.microsoft.com/"
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(endpoint, prediction_credentials)
# Open an image and make a prediction
with open(os.path.join(images_folder, "french-macaron-recipe.jpg"), "rb") as image_contents:
    results = predictor.classify_image(project_id, publish_iteration_name, image_contents.read())
# Display the results
for prediction in results.predictions:
    print(f"{prediction.tag_name}: {prediction.probability * 100 :.2f}%")


