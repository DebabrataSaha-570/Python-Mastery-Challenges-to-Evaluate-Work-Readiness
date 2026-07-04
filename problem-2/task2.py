uber_deducted_commission = 22 / 100

#.........Anowar
anowar_trips = 18
anowar_per_trip_earning = 420
anowar_received_bonus = 750
anowar_fuel_cost = 2850
anowar_tolls_cost = 350
anowar_parking_cost = 450


anowar_total_trip_earning = anowar_trips * anowar_per_trip_earning
print(anowar_total_trip_earning)

anowar_trip_uber_commision = anowar_total_trip_earning * uber_deducted_commission

print(anowar_trip_uber_commision)

anowar_final_earning = anowar_total_trip_earning - anowar_trip_uber_commision + anowar_received_bonus

print(anowar_final_earning)

anowar_total_expenses = anowar_fuel_cost + anowar_tolls_cost + anowar_parking_cost

print(anowar_total_expenses)

anowar_net_profit = anowar_final_earning - anowar_total_expenses; 
print("anowar net profit", anowar_net_profit)

#.........Abdullah
abdullah_trips = 21
abdullah_per_trip_earning = 390
abdullah_received_bonus = 500
abdullah_fuel_cost = 3150
abdullah_tolls_cost = 500
abdullah_parking_cost = 300


abdullah_total_trip_earning = abdullah_trips * abdullah_per_trip_earning
print(abdullah_total_trip_earning)

abdullah_trip_uber_commision = abdullah_total_trip_earning * uber_deducted_commission

print(abdullah_trip_uber_commision)

abdullah_final_earning = abdullah_total_trip_earning - abdullah_trip_uber_commision + abdullah_received_bonus

print(abdullah_final_earning)

abdullah_total_expenses = abdullah_fuel_cost + abdullah_tolls_cost + abdullah_parking_cost

print(abdullah_total_expenses)

abdullah_net_profit = abdullah_final_earning - abdullah_total_expenses
print("abdullah net profit", abdullah_net_profit)



#.........Jubayer 
Jubayer_trips = 16
Jubayer_per_trip_earning = 510
Jubayer_received_bonus = 900
Jubayer_fuel_cost = 2600
Jubayer_tolls_cost = 250
Jubayer_parking_cost = 550


Jubayer_total_trip_earning = Jubayer_trips * Jubayer_per_trip_earning
print(Jubayer_total_trip_earning)

Jubayer_trip_uber_commision = Jubayer_total_trip_earning * uber_deducted_commission

print(Jubayer_trip_uber_commision)

Jubayer_final_earning = Jubayer_total_trip_earning - Jubayer_trip_uber_commision + Jubayer_received_bonus

print(Jubayer_final_earning)

Jubayer_total_expenses = Jubayer_fuel_cost + Jubayer_tolls_cost + Jubayer_parking_cost

print(Jubayer_total_expenses)

Jubayer_net_profit = Jubayer_final_earning - Jubayer_total_expenses
print("Jubayer net profit", Jubayer_net_profit)


#..........highest net profit
if anowar_net_profit >= abdullah_net_profit and anowar_net_profit >= Jubayer_net_profit:
    print("Highest Net Profit : Anowar")

elif abdullah_net_profit >= anowar_net_profit and abdullah_net_profit >= Jubayer_net_profit:
    print("Highest Net Profit : Abdullah")

else:
    print("Highest Net Profit : Jubayer")

#........rank drivers

if anowar_net_profit >= abdullah_net_profit and anowar_net_profit >= Jubayer_net_profit:
    print("1st : Anowar")

    if abdullah_net_profit >= Jubayer_net_profit:
        print("2nd : Abdullah")
        print("3rd : Jubayer")
    else:
        print("2nd : Jubayer")
        print("3rd : Abdullah")

elif abdullah_net_profit >= anowar_net_profit and abdullah_net_profit >= Jubayer_net_profit:
    print("1st : Abdullah")

    if anowar_net_profit >= Jubayer_net_profit:
        print("2nd : Anowar")
        print("3rd : Jubayer")
    else:
        print("2nd : Jubayer")
        print("3rd : Anowar")

else:
    print("1st : Jubayer")

    if anowar_net_profit >= abdullah_net_profit:
        print("2nd : Anowar")
        print("3rd : Abdullah")
    else:
        print("2nd : Abdullah")
        print("3rd : Anowar")


#..........Longest working duration
anowar_working_time = 9 * 60 + 15
abdullah_working_time = 10 * 60
jubayer_working_time = 8 * 60 + 30


if anowar_working_time >= abdullah_working_time and anowar_working_time >= jubayer_working_time:
    print("Longest Working Duration : Anowar")

elif abdullah_working_time >= anowar_working_time and abdullah_working_time >= jubayer_working_time:
    print("Longest Working Duration : Abdullah")

else:
    print("Longest Working Duration : Jubayer")



#.........excellent performance

if anowar_net_profit >= 6000:
    print("Anowar : Excellent Performance")
elif anowar_net_profit >= 4000:
    print("Anowar : Good Performance")
else:
    print("Anowar : Needs Improvement")


if abdullah_net_profit >= 6000:
    print("Abdullah : Excellent Performance")
elif abdullah_net_profit >= 4000:
    print("Abdullah : Good Performance")
else:
    print("Abdullah : Needs Improvement")


if Jubayer_net_profit >= 6000:
    print("Jubayer : Excellent Performance")
elif Jubayer_net_profit >= 4000:
    print("Jubayer : Good Performance")
else:
    print("Jubayer : Needs Improvement")


