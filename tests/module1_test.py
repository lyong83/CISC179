from cisc179.Vehicle import Vehicle
from cisc179.module1 import PickupTruck
from cisc179.module1 import Module1Class


def test_module1():
    # 创建 Module1Class 实例
    module1_instance = Module1Class()

    # 调用 execute 方法并打印结果
    result = module1_instance.execute()
    print(result)

def test_vehicle():
    # 创建 Vehicle 实例
    vehicle = Vehicle("Manufacturer", 10000, 25000, 5, ["Option 1", "Option 2"])

    # 打印实例属性
    print("Manufacturer:", vehicle.manufacturerName)
    print("Miles:", vehicle.milesOnVehicle)
    print("Price:", vehicle.price)
    print("Number of Seats:", vehicle.numberOfSeats)
    print("Options:", vehicle.options)

def test_pickup_truck():
    # 创建 PickupTruck 实例
    pickup_truck = PickupTruck("Manufacturer", 10000, 25000, 5, ["Option 1", "Option 2"], 500)

    # 打印实例属性和方法
    print("Manufacturer:", pickup_truck.manufacturerName)
    print("Miles:", pickup_truck.milesOnVehicle)
    print("Price:", pickup_truck.price)
    print("Number of Seats:", pickup_truck.numberOfSeats)
    print("Options:", pickup_truck.options)
    print("Cargo Capacity:", pickup_truck.getCargoCapacity)

# 在 test.py 中执行测试
test_module1()
test_vehicle()
test_pickup_truck()
