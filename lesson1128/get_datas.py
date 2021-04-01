import yaml

def get_datas():
    # encoding参数不是必填的，但是在windows系统建议加上，防止yml文件中出现中文读取报错，windows默认是GBK格式（mac可以不加该参数）
    with open("data1.yml",encoding='utf-8') as f:
    # safe_load可以直接对文档加载，也可以对读取出来的流文件f加载,注意下面语句块的缩进。
      datas = yaml.safe_load(f)
    return datas


print(get_datas())

# safe_dump 将python数据转换成yaml数据
print(yaml.safe_dump(
    [2, 5, ['a', 'b'], {'x': 3, 'y': 8}, None]
    ))