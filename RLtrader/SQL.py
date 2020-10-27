from azure.cosmos import CosmosClient
import csv

print('Imported packages successfully.')

# 아래 primarykey는 read-only 입니다.
config = {
    "endpoint": "https://jang.documents.azure.com:443/",
    "primarykey": "vqAEaHFa2Ov79VlOlcf8zP1TLtsUsuZqD0LUASUqu0IFZ9pU1MfdNUkepMdvipkSziB80dUmyzyqyDwsx7ypZg=="
}

client = CosmosClient(config["endpoint"], config["primarykey"])

database_name = 'MLStocking'
database = client.get_database_client(database_name)
container_name = 'daily_price'
container = database.get_container_client(container_name)

# SQL
q = '''
SELECT p.id, p.Date, p.code
FROM daily_price p
WHERE p.Date = "2020-08-10"
'''

# Get the number of items in daily_price container
items = container.query_items(
    query=q,
    enable_cross_partition_query=True)

json_list = []
for item in items:
    json_list.append(item)
# print(json_list)

keys = json_list[0].keys()
print(keys)