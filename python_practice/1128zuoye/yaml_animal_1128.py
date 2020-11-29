# 1、自己写一个面向对象的例子：
# 比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
# 创建子类【猫】，继承【动物类】，
# 复写父类的__init__方法，继承父类的属性，
# 添加一个新的属性，毛发=短毛，
# 添加一个新的方法， 会捉老鼠，
# 复写父类的‘【会叫】的方法，改成【喵喵叫】
# 创建子类【狗】，继承【动物类】，
# 复写父类的__init__方法，继承父类的属性，
# 添加一个新的属性，毛发=长毛，
# 添加一个新的方法， 会看家，
# 复写父类的【会叫】的方法，改成【汪汪叫】
# 调用 name== ‘main’：
# 创建一个猫猫实例
# 调用捉老鼠的方法
# 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
# 创建一个狗狗实例
# 调用【会看家】的方法
# 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
# 2、将数据配置到yaml文件里

import os, yaml

file_path = os.path.split(os.path.realpath(__file__))[0]
parent_path = os.path.abspath(os.path.join(file_path, ".."))
yaml_path = os.path.join(parent_path + '\yaml_file')
Animal_yml = yaml_path + '\Animal.yml'
print("Animal_yml：", Animal_yml)


class Animal:
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def run(self):
        print("running")

    def bark(self):
        print("barking")


class Cat(Animal):
    def __init__(self, hair, name, color, age, sex):
        self.hair = hair
        super().__init__(name, color, age, sex)

    def all_attribute(self):
        return f"{self.name},{self.color},{self.age},{self.sex},{self.hair},捉到了老鼠"

    def catch(self):
        return f"{self.name}会抓老鼠"

    def bark(self):
        print(f"{self.name}会喵喵叫")


class Dog(Animal):
    def __init__(self, hair, name, color, age, sex):
        self.hair = hair
        super().__init__(name, color, age, sex)

    def all_attribute(self):
        attr = f"{self.name},{self.color},{self.age},{self.sex},{self.hair}"
        # print(f"{self.name},{self.color},{self.age},{self.sex},{self.hair}")
        return attr

    def protect(self):
        return f"{self.name}会看家"

    def bark(self):
        print(f"{self.name}会汪汪叫")


if __name__ == '__main__':
    with open(Animal_yml, encoding="UTF-8") as f:
        animal = yaml.safe_load(f)
    # print(animal)
    # print(animal['Animal'])
    cat4cat = animal['Animal']['Cat']
    dog4dog = animal['Animal']['Dog']
    mm = Cat(cat4cat["hair"], cat4cat["name"], cat4cat["color"], cat4cat["age"], cat4cat["sex"])
    gg = Dog(dog4dog['hair'], dog4dog['name'], dog4dog['color'], dog4dog['age'], dog4dog['sex'])
    print("cat", mm.all_attribute())
    print("dog", gg.all_attribute())
