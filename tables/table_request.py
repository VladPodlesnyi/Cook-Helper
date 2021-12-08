from azure.data.tables import TableClient

meal = "'Apple pie'"
my_filter = "PartitionKey eq " + meal
table_client = TableClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=recipestorageacc;AccountKey=FFm0U81INHuCgEGb5UhuzZYvAwi37o2gizvr+KXXdJNA2DmCwwBc5h12yM0ZSTfT2AbiHASKaqiBcT8lo0pW9Q==;EndpointSuffix=core.windows.net", table_name="recipes")
entities = table_client.query_entities(my_filter)
for entity in entities:
    print(entity['Link'])