# 大小写敏感
# 使用缩进表示层级关系
# 缩进不允许使用tab，只允许空格
# 缩进的空格数不重要，只要相同层级的元素左对齐即可
# '#'表示注释
# YAML 支持以下几种数据类型：
# 对象：键值对的集合，又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary）
# 数组：一组按次序排列的值，又称为序列（sequence） / 列表（list）
# 纯量（scalars）：单个的、不可再分的值

# 对象键值对使用冒号结构表示 key: value，冒号后面要加一个空格。
# 也可以使用 key:{key1: value1, key2: value2, ...}。
# 还可以使用缩进表示层级关系；
# key:
#     child-key: value
#     child-key2: value2

import yaml
# 字典里面嵌套字典，注：关键字后接冒号，冒号后必须空格
# document = """
# a: 1
# b:
#  c: 2
#  d: 3
# """
# # safe_load将yaml格式的数据文档document加载成python能认识的格式，也可以把这个documnet文档单独写在yml文件里
# print(yaml.safe_load(document))

print(yaml.safe_load("""
- python
- java
- ruby
"""
                     ))

