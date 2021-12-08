import telebot
import requests

from azure.data.tables import TableClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

bot = telebot.TeleBot('5098799334:AAE7x-zNdSd3HmlzBIKvM9dZ09qGRwXEfBc')
publish_iteration_name = "CookHelperPub"
project_id = "f4ec7aed-3c70-4698-a41c-bde9ce39b2e5"
prediction_key = "546ce298309f4867b39e7d18edbde621"
endpoint = "https://northeurope.api.cognitive.microsoft.com/"
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(endpoint, prediction_credentials)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Hello, send me a picture")


@bot.message_handler(content_types=["photo"])
def photo(message):
    raw = message.photo[-1].file_id
    path = raw + ".jpg"
    file = bot.get_file(raw)
    download = bot.download_file(file.file_path)
    with open(path, 'wb') as new_file:
        new_file.write(download)

    with open(path, "rb") as image_contents:
        results = predictor.classify_image(project_id, publish_iteration_name, image_contents.read())

    #url = 'http://google.com'
    #files = {'media': open(path, 'rb')}
    #response = requests.post(url, files=files)
    #image_url = "https://sugargeekshow.com/wp-content/uploads/2018/01/french-macaron-recipe.jpg"
    #results = predictor.classify_image_url(project_id, publish_iteration_name, url=path)
    meal = results.predictions[1].tag_name

    my_filter = "PartitionKey eq '" + meal + "'"
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=recipestorageacc;AccountKey=FFm0U81INHuCgEGb5UhuzZYvAwi37o2gizvr+KXXdJNA2DmCwwBc5h12yM0ZSTfT2AbiHASKaqiBcT8lo0pW9Q==;EndpointSuffix=core.windows.net",
        table_name="recipes")
    entities = table_client.query_entities(my_filter)
    for entity in entities:
        link = entity['Link']
    bot.send_message(message.from_user.id, link)


bot.polling(none_stop=True, interval=0)
