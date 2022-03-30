import requests
import json
import os
import time

SOURCE_BASE_URL = os.environ.get('SOURCE_BASE_URL')
SOURCE_KEY = os.environ.get('SOURCE_KEY')

TARGET_BASE_URL = os.environ.get('TARGET_BASE_URL')
TARGET_KEY = os.environ.get('TARGET_KEY')
TARGET_NAME = os.environ.get('TARGET_NAME')

def fetch():
    headers={"X-Api-Key":SOURCE_KEY}
    response = requests.get(SOURCE_BASE_URL, headers=headers)
    return response.json()

def send():
    source_data = fetch()
    now = str(round(time.time() * 1000))
    source_data['createdAt'] = { "$date": { "$numberLong": now }}

    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': TARGET_KEY
    }
    raw_data = json.dumps({
            "dataSource": TARGET_NAME,
            "database": "myFirstDatabase",
            "collection": "test",
            "document": source_data
    })
    response = requests.post(TARGET_BASE_URL, headers=headers, data=raw_data)
    print(raw_data)
    return response

def main():
    while True:
        print(send())
        time.sleep(200)

if __name__ == "__main__":
    main()