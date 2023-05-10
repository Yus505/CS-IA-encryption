bus_capacity = 40
bus_amount = 200
bus_fullness = 0.7

car_capacity = 5
car_amount = 5000
car_fullness = 0.4


bike_capacity = 1
bike_amount = 400
bike_fullness = 1

truck_capacity = 2
truck_amount = 40
truck_fullness = 0.5

people_pass = ((bus_amount * bus_fullness * bus_capacity) + (car_amount * car_capacity * car_fullness) + (bike_fullness * bike_amount * bike_capacity) +(truck_fullness * truck_amount * truck_capacity))
if people_pass > 20000:
    print("The bridge is fully utilized")
elif people_pass < 10000:
    print("The bridge is under utilized")
else:
    print("The bridge is under normal use")