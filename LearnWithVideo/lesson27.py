import json

# 字典转化为 json 对象
str = {'code':1025,'name':'mk','age':23}
print(json.dumps(str))

#  json 对象转化为 字典
jsonObject = '{"id":353,"name":"3t35","age":35}'
print(json.loads(jsonObject))

#字典和json对象的区别 ： ‘’ 和 “”（单引号和双引号的区别）
