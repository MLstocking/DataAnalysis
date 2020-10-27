import pandas as pd
import numpy as np
from azure.cosmos import CosmosClient
from datetime import date

def read_DBdata(config=None):
    today = date.today().isoformat()
    # 아래 primarykey는 read-only 입니다.
    if config == None:
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
    q = f'''
    SELECT p.Date, p.Open, p.High, p.Low, p.Close, p.Volume
    FROM daily_price p
    WHERE p.code = "005930" AND p.Date >= "2019-01-01" AND p.Date <= "{today}"
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

    DBdata = pd.DataFrame(json_list)
    DBdata['Date'] = pd.to_datetime(DBdata['Date'])
    DBdata.sort_values('Date', inplace=True)
    DBdata = DBdata.groupby('Date', as_index=False).first() # 중복제거
    print("Today:", today)
    print("Last Data:", DBdata['Date'].dt.strftime("%Y-%m-%d").iloc[-1])
    DBdata.columns = DBdata.columns.str.lower()
    DBdata['date'] = DBdata['date'].dt.strftime('%Y%m%d') # 날짜 포맷 변경

    return DBdata
    
if __name__ == '__main__':
    data = read_DBdata()
    print(data)