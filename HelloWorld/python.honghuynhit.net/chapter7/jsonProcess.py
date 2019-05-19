import urllib3
import json
import os

http = urllib3.PoolManager()

import requests
url = 'http://api.github.com/users/honghuynhit/repos'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
r = requests.get(url, headers=headers)

data = json.loads(r.content.decode('utf-8'))
print(data)

if os.path.exists('E:\Work\Project') is False:
    print('path not exists')
else:

# Read and create file and write file json to file.
    with open('E:/Work/Project/jsonTest.json','w+') as outfile:
        json.dump(data, outfile)