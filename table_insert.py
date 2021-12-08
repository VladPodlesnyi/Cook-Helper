from azure.cosmosdb.table.tableservice import TableService

meals = open("meals.txt", "r")
recipes = open("recipes.txt", "r")

m_lines = meals.readlines()
r_lines = recipes.readlines()

for i in range(len(r_lines)):
    my_entity = {
        u'PartitionKey': m_lines[i].strip(),
        u'RowKey': str(i),
        u'Link': r_lines[i].strip()
    }

    table_service = TableService(account_name='recipestorageacc', account_key='FFm0U81INHuCgEGb5UhuzZYvAwi37o2gizvr+KXXdJNA2DmCwwBc5h12yM0ZSTfT2AbiHASKaqiBcT8lo0pW9Q==')
    table_service.insert_entity('recipes', my_entity)

meals.close()
recipes.close()
