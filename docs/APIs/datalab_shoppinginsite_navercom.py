# from https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md#%EC%87%BC%ED%95%91%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8-%EB%B6%84%EC%95%BC%EB%B3%84-%ED%8A%B8%EB%A0%8C%EB%93%9C-%EC%A1%B0%ED%9A%8C

import requests   # postman app 역할

# requests API 요청
url = "https://openapi.naver.com/v1/datalab/shopping/categories"

headers = {'X-Naver-Client-Id':'xXDiGH6YIxUyKDzYsL7J', 
           'X-Naver-Client-Secret':'dXgoh9TOM5'}

bodys = {
  "startDate": "2017-08-01",
  "endDate": "2017-09-30",
  "timeUnit": "month",
  "category": [
      {"name": "패션의류", "param": [ "50000000"]},
      {"name": "화장품/미용", "param": [ "50000002"]}
  ],
  "device": "pc",
  "gender": "f",
  "ages": [ "20",  "30"]
}

response = requests.post(url, headers=headers, json=bodys)

# response API 응답
response.content

# json을 변수로 변환
import json
contents = json.loads(response.content)
pass
