# 데이터명 : 기상청_관광코스별 관광지 상세 날씨 조회서비스
# from https://www.data.go.kr/iim/api/selectAPIAcountView.do
import requests 

# url 주소 변수 지정
url = 'http://apis.data.go.kr/1360000/TourStnInfoService1/getCityTourClmIdx1?serviceKey=ZYK0bMGPmpujibjhabHiPWFvFzI%2FxcgntGutROQzYCLasxlwqqEtn4KO5lAeieJ8i35RbVnOnRer7tfV3A%2FwGA%3D%3D&pageNo=1&numOfRows=10&dataType=JSON&CURRENT_DATE=2018123110&DAY=3&CITY_AREA_ID=5013000000'

pass
# respose라는 변수로 받음
response = requests.get(url) 
pass
# response의 내용을 출력
print(response.content) 

# json 파일을 dictionary 형태로 변환
import json
contents = json.loads(response.content)
pass



# mongoDB 저장
from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["data_go_kr"]
# collection 작업
collection = database['TourStnInfoService1_getTourStnVilageFcst1']
# insert 작업 진행
result = collection.insert_many(contents['response']['body']['items']['item'])