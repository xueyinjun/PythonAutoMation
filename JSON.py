#utf-8
#json字符串转成python值
import json
stringofJsonData = '{"name":"Zophie","isCat":true,"miceCaught":0,"feilIO":null}'
jsonDataAsPythonValue = json.loads(stringofJsonData)
print(jsonDataAsPythonValue)


#python值转成Json字符串
import json
pythonValue = {
    'isCat': True,
    'miceCaught': 0,
    'name': 'Zophie',
    'felineIQ': None
}
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)