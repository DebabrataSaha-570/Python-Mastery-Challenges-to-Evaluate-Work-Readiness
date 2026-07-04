
#drone alpha
battery_must_reserved = 15 / 100

alpha_started_battery = 96
alpha_before_take_off_camera_usage = 6
alpha_flew_distance_usage = 40
alpha_unloading_battery_consumed = 4
alpha_returned_home_usage = 20
alpha_time = 34

alpha_total_battery_usage = alpha_before_take_off_camera_usage + alpha_flew_distance_usage + alpha_unloading_battery_consumed + alpha_returned_home_usage


alpha_remaining_battery = alpha_started_battery - alpha_total_battery_usage
alpha_reserved_battery = alpha_remaining_battery * battery_must_reserved
alpha_usable_battery = alpha_remaining_battery - alpha_reserved_battery

print("alpha usable battery", alpha_usable_battery)

if (alpha_usable_battery >= 20):
    print("alpha drone mission successful")
else : 
    print("Alpha drone recharge required")


## drone bravo

bravo_started_battery = 98
bravo_before_take_off_camera_usage = 8
bravo_flew_distance_usage = 36
bravo_unloading_battery_consumed = 5
bravo_returned_home_usage = 18
bravo_time = 30

bravo_total_battery_usage = bravo_before_take_off_camera_usage + bravo_flew_distance_usage + bravo_unloading_battery_consumed + bravo_returned_home_usage


bravo_remaining_battery = bravo_started_battery - bravo_total_battery_usage
bravo_reserved_battery = bravo_remaining_battery * battery_must_reserved
bravo_usable_battery = bravo_remaining_battery - bravo_reserved_battery

print("bravo remaining battery", bravo_remaining_battery)
print("bravo usable battery", bravo_usable_battery)

if (bravo_usable_battery >= 20):
    print("bravo drone mission successful")
else : 
    print("bravo drone recharge required")


#drone charlie


charlie_started_battery = 94
charlie_before_take_off_camera_usage = 7
charlie_flew_distance_usage = 44
charlie_unloading_battery_consumed = 6
charlie_returned_home_usage = 22
charlie_time = 38

charlie_total_battery_usage = charlie_before_take_off_camera_usage + charlie_flew_distance_usage + charlie_unloading_battery_consumed + charlie_returned_home_usage


charlie_remaining_battery = charlie_started_battery - charlie_total_battery_usage
charlie_reserved_battery = charlie_remaining_battery * battery_must_reserved
charlie_usable_battery = charlie_remaining_battery - charlie_reserved_battery

print("charlie remaining battery", charlie_remaining_battery)
print("charlie usable battery", charlie_usable_battery)

if (charlie_usable_battery >= 20):
    print("charlie drone mission successful")
else : 
    print("charlie drone recharge required")

# heighest usable battery

heighest_usable_battery = max(charlie_usable_battery, bravo_usable_battery, alpha_usable_battery)

print("Height usable battry", heighest_usable_battery)


# 1st, 2nd, 3rd

if alpha_time <= bravo_time and alpha_time <= charlie_time:
    print("first: alpha")

    if bravo_time <= charlie_time: 
        print("Second : bravo")
        print("third : charlie")
    else: 
        print("second: charlie")
        print("third : bravo")

elif bravo_time <= alpha_time and bravo_time <= charlie_time: 
    print("first: bravo")

    if alpha_time <= charlie_time: 
        print("Second : Alpha")
        print("Third : Charlie")
    else : 
        print ("Second : Charlie")
        print("Third: Alpha")
else : 
    print("First : Charlie")

    if alpha_time <= bravo_time: 
        print("Second : Alpha")
        print("Third: bravo")
    else :
        print ("second : bravo")
        print ("Third : alpha")




