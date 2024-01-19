# from https://developers.naver.com/docs/serviceapi/search/shopping/shopping.md#%EC%87%BC%ED%95%91

import requests    # postman app 역할

# requests API 요청
url = 'https://openapi.naver.com/v1/search/shop'
params = {'query':'인공지능'}
headers = {'X-Naver-Client-Id':'uH4qY24lRbBEyrYCcYXa', 
           'X-Naver-Client-Secret':'v4GYUicOW6'}

response = requests.get(url, params=params, headers=headers)

# response API 응답
response.content
pass


# json을 변수로 변환
import json
contents = json.loads(response.content)
pass

# str을 dict으로 변환
document_info = {'lastBuildDate' : contents['lastBuildDate'],
            'total' : contents['total'],
            'start' : contents['start'],
            'display' : contents['display']}

# mongoDB 저장
from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["request_search_shop"]
# collection 작업
collection1 = database['search_shop_info']
collection2 = database['search_shop_list']


# insert 작업 진행
result_info = collection1.insert_one(document_info)


# collection1에 있는 _id find
get_id = result_info.inserted_id # {모든 문서 가져오기}, {반환활 필드를 지정/_id필드만 반환하라는 의미}
pass
# id_relative = get_id['_id'] #'_id'필드 값 가져오기/ 즉 첫번 째 문서의 '_id'필드 값을 가져와서 변수에 저장/이 과정을 거치는 이유는 dict으로 나온 값을 str으로 반환하기 위해서인데 inserted_id를 쓰면 이 과정 필요 없음 

item_list = contents['items']

for i in range(len(item_list)) :
    item_list[i]['id_relative'] = get_id


# insert 작업 진행
result_item = collection2.insert_many(item_list)




# find_one({}, {"_id" : 1}은 디비의 첫번째의 id만 나오게 하고/ inserted_id는 새롭게 삽입된 문서의 id를 반환