import yaml

class Bicycle:
    def run(self,km):
        print(f"健康环保，骑行的公里数为:{km}km")

class Ebicycle(Bicycle):
    def __init__(self,battery):
        self.battery = battery

    # 此充电方法感觉没有用到？？---如果要用充电这个方法比如下面的调用eb.fill_charge(3)，
    # 就需先在run方法调用之前（run方法里使用了self.battery），调用充电方法修改原始电量
    def fill_charge(self,vol):
        self.battery = self.battery + vol

    def run(self,km):
        miles = km - self.battery*10
        if miles > 0:
            print(f"用电骑了{self.battery*10}km,还需要用脚蹬{miles}km")
            # 在子类的方法中调用父类的方法用super().父类方法名,super为父类，加个括号相当于父类的一个实例，
            # 这也就是类中的方法要由实例来调用，执行父类方法打印用脚蹬的公里数，等同于先实例化父类的一个实例，再用实例调用父类的方法
            bicycle = Bicycle()
            bicycle.run(miles)
            # super().run(miles)

        else:
            print(f"电量足够用，用电行驶了{km}km")

# 实例化类的时候根据类的构造函数（构造函数的作用就是给实例传递静态属性的）传递对应的参数，比如下面的10就是子类电动车的初始电量
# main 函数相当于这个模块的一个入口函数，如果这个模块被别的模块调用，就不会执行main函数下的内容，如果不用main，目前main下面的调用语句会被执行一次
if __name__ == '__main__':
    # eb = Ebicycle(10)
    # # 在eb.run(120)之前先调用充电方法，打印电量
    # eb.fill_charge(3)
    # print(eb.battery)
    # eb.run(120)

    with open ("bicycle_data.yml") as f:
        datas = yaml.safe_load(f)
    print(datas['default'])
    battery = datas['default']['battery']
    vol = datas['default']['vol']
    run_km = datas['default']['run_km']

    eb = Ebicycle(battery)
    eb.fill_charge(vol)
    eb.run(run_km)



