def fuel_tank(starting_point, ending_point, car_millege, tank_capacity):
    fuel_consumed = (ending_point - starting_point) / car_millege
    stop_for_fuel = fuel_consumed % tank_capacity
    if stop_for_fuel == 0:
        stop_for_fuel = fuel_consumed / tank_capacity
        print("number of stops for refueling",stop_for_fuel)
    else:
        stop_for_fuel = fuel_consumed // tank_capacity
        stop_for_fuel = stop_for_fuel + 1
        print("number of stops for refueling",stop_for_fuel)
             
fuel_tank(int(input("enter starting point\n")), int(input("enter ending point\n")), int(input("enter your car millege\n")), int(input("enter your car tank capacity\n")))

