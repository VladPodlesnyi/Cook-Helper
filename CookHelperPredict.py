from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os

# Create variables for your project
publish_iteration_name = "CookHelperPub"
project_id = "f4ec7aed-3c70-4698-a41c-bde9ce39b2e5"


# Create variables for your prediction resource
prediction_key = "546ce298309f4867b39e7d18edbde621"
endpoint = "https://northeurope.api.cognitive.microsoft.com/"
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(endpoint, prediction_credentials)


image_url = "https://sugargeekshow.com/wp-content/uploads/2018/01/french-macaron-recipe.jpg"


results = predictor.classify_image_url(project_id,publish_iteration_name,url=image_url)

print(results.predictions[1].tag_name)
