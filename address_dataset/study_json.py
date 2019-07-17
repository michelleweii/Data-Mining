import json

# json.dumps()函数的使用，将字典转化为字符串
dict1 = {"age": "12"}
json_info = json.dumps(dict1)
print("dict1的类型："+str(type(dict1)))
print("通过json.dumps()函数处理：")
print("json_info的类型："+str(type(json_info)))
"""
dict1的类型：<class 'dict'>
通过json.dumps()函数处理：
json_info的类型：<class 'str'>
"""

# json.loads函数的使用，将字符串转化为字典
json_info = '{"age": "12"}'
dict1 = json.loads(json_info)
print("json_info的类型："+str(type(json_info)))
print("通过json.dumps()函数处理：")
print("dict1的类型："+str(type(dict1)))
"""
json_info的类型：<class 'str'>
通过json.dumps()函数处理：
dict1的类型：<class 'dict'>
"""

# json.dump()函数的使用，将json信息写进文件
json_info = "{'age': '12'}"
file = open('1.json','w',encoding='utf-8')
json.dump(json_info,file)
# "{'age': '12'}"


# json.load()函数的使用，将读取json信息
file = open('1.json','r',encoding='utf-8')
info = json.load(file)
print(info)
# {'age': '12'}