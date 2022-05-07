
import os
import time
import csv
import random
import hashlib
import datetime
from flask import Flask, request
from collections import namedtuple

def sleep(n_secs):
    time.sleep(n_secs)


def get_cityCode():
    citycodes = [
        {"title":"平谷","cityCode":"756","statusCode":200},
        {"title":"昌平","cityCode":"785","statusCode":200},
        {"title":"大兴","cityCode":"826","statusCode":200},
        {"title":"房山","cityCode":"827","statusCode":200},
        {"title":"怀柔","cityCode":"752","statusCode":200}
    ]
    citycode = [citycodes[random.randint(0,4)]]
    return citycode


# print(get_cityCode())



# 读取CSV文件，并将制定字段以int类型输出
def csv_weather():
    with open('/Users/mr/Desktop/Git_httprunner/Httprunner2.3.0/datas/ciytCode.csv',mode='r',encoding='utf-8') as readers:
        csv_readers = csv.DictReader(readers)
        weather_date = []
        for row in csv_readers:
            weather_date.append(row)
        compressed = [(x['title'], x['cityCode'], int(x['statusCode'])) for x in weather_date]
        return compressed

# print(csv_weather())
#MD5加密
def md5_key(value):
   if isinstance(value, str) == True:
        md5_data = hashlib.md5(value.encode(encoding='UTF-8')).hexdigest()
        return md5_data.upper()
   else:
       print('int')
       value = str(value)
       md5_data = hashlib.md5(value.encode(encoding='UTF-8')).hexdigest()
       return md5_data.upper()


# print(md5_key('123'))

# mock

app = Flask(__name__)
@app.route('/WebServices/WeatherWS.asmx/getWeather',methods=['POST','GET'])

def getWeather():
    theCityCode = request.values.get("theCityCode")
    if theCityCode == '756':
        return {"data":{"cityname":"平谷","cityid":theCityCode,"status":"小雨","centigrade":"9℃/18℃","wind":"北风小于3级"}}
    elif theCityCode == '785':
        return {"data":{"cityname":"昌平","cityid":theCityCode,"status":"小雨","centigrade":"9℃/18℃","wind":"北风小于3级"}}
    elif theCityCode == '826':
        return {"data":{"cityname":"大兴","cityid":theCityCode,"status":"小雨","centigrade":"9℃/18℃","wind":"北风小于3级"}}


if __name__ == '__main__':
    app.run()
