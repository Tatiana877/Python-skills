meter1_act_T1 = int(input('Введите текущие показания электросчетчика к.1 T1: '))
meter1_act_T2 = int(input('Введите текущие показания электросчетчика к.1 T2: '))
meter1_act_T3 = int(input('Введите текущие показания электросчетчика к.1 T3: '))
meter1_prev_T1 = int(input('Введите предыдущие показания электросчетчика к.1 T1: '))
meter1_prev_T2 = int(input('Введите предыдущие показания электросчетчика к.1 T2: '))
meter1_prev_T3 = int(input('Введите предыдущие показания электросчетчика к.1 T3: '))

meter2_act_T1 = int(input('Введите текущие показания электросчетчика к.2 T1: '))
meter2_act_T2 = int(input('Введите текущие показания электросчетчика к.2 T2: '))
meter2_act_T3 = int(input('Введите текущие показания электросчетчика к.2 T3: '))
meter2_prev_T1 = int(input('Введите предыдущие показания электросчетчика к.2 T1: '))
meter2_prev_T2 = int(input('Введите предыдущие показания электросчетчика к.2 T2: '))
meter2_prev_T3 = int(input('Введите предыдущие показания электросчетчика к.2 T3: '))

meter3_act_T1 = int(input('Введите текущие показания электросчетчика к.3 T1: '))
meter3_act_T2 = int(input('Введите текущие показания электросчетчика к.3 T2: '))
meter3_act_T3 = int(input('Введите текущие показания электросчетчика к.3 T3: '))
meter3_prev_T1 = int(input('Введите предыдущие показания электросчетчика к.3 T1: '))
meter3_prev_T2 = int(input('Введите предыдущие показания электросчетчика к.3 T2: '))
meter3_prev_T3 = int(input('Введите предыдущие показания электросчетчика к.3 T3: '))

meter4_act_T1 = int(input('Введите текущие показания электросчетчика к.4 T1: '))
meter4_act_T2 = int(input('Введите текущие показания электросчетчика к.4 T2: '))
meter4_act_T3 = int(input('Введите текущие показания электросчетчика к.4 T3: '))
meter4_prev_T1 = int(input('Введите предыдущие показания электросчетчика к.4 T1: '))
meter4_prev_T2 = int(input('Введите предыдущие показания электросчетчика к.4 T2: '))
meter4_prev_T3 = int(input('Введите предыдущие показания электросчетчика к.4 T3: '))

meter5_act_T1 = int(input('Введите текущие показания электросчетчика к.5 T1: '))
meter5_act_T2 = int(input('Введите текущие показания электросчетчика к.5 T2: '))
meter5_act_T3 = int(input('Введите текущие показания электросчетчика к.5 T3: '))
meter5_prev_T1 = int(input('Введите предыдущие показания электросчетчика к.5 T1: '))
meter5_prev_T2 = int(input('Введите предыдущие показания электросчетчика к.5 T2: '))
meter5_prev_T3 = int(input('Введите предыдущие показания электросчетчика к.5 T3: '))

meter_flat_act_T1 = int(input('Введите текущие показания общего электросчетчика T1: '))
meter_flat_act_T2 = int(input('Введите текущие показания общего электросчетчика T2: '))
meter_flat_act_T3 = int(input('Введите текущие показания общего электросчетчика T3: '))
meter_flat_prev_T1 = int(input('Введите предыдущие показания общего электросчетчика T1: '))
meter_flat_prev_T2 = int(input('Введите предыдущие показания общего электросчетчика T2: '))
meter_flat_prev_T3 = int(input('Введите предыдущие показания общего электросчетчика T3: '))

T1_tariff = 5.84
T2_tariff = 1.63
T3_tariff = 4.87

electric_cost1 = (meter1_act_T1 - meter1_prev_T1) * T1_tariff + (meter1_act_T2 - meter1_prev_T2) * T2_tariff + (meter1_act_T3 - meter1_prev_T3) * T3_tariff

electric_cost2 = (meter2_act_T1 - meter2_prev_T1) * T1_tariff + (meter2_act_T2 - meter2_prev_T2) * T2_tariff + (meter2_act_T3 - meter2_prev_T3) * T3_tariff

electric_cost3 = (meter3_act_T1 - meter3_prev_T1) * T1_tariff + (meter3_act_T2 - meter3_prev_T2) * T2_tariff + (meter3_act_T3 - meter3_prev_T3) * T3_tariff

electric_cost4 = (meter4_act_T1 - meter4_prev_T1) * T1_tariff + (meter4_act_T2 - meter4_prev_T2) * T2_tariff + (meter4_act_T3 - meter4_prev_T3) * T3_tariff

electric_cost5 = (meter5_act_T1 - meter5_prev_T1) * T1_tariff + (meter5_act_T2 - meter5_prev_T2) * T2_tariff + (meter5_act_T3 - meter5_prev_T3) * T3_tariff

electric_cost_flat = (meter_flat_act_T1 - meter_flat_prev_T1) * T1_tariff + (meter_flat_act_T2 - meter_flat_prev_T2) * T2_tariff + (meter_flat_act_T3 - meter_flat_prev_T3) * T3_tariff

hall_cost = electric_cost_flat - electric_cost1 - electric_cost2 - electric_cost3 - electric_cost4 - electric_cost5

final_cost1 = electric_cost1 + hall_cost / 5
final_cost2 = electric_cost2 + hall_cost / 5
final_cost3 = electric_cost3 + hall_cost / 5
final_cost4 = electric_cost4 + hall_cost / 5
final_cost5 = electric_cost5 + hall_cost / 5

print(round(final_cost1, 2))
print(round(final_cost2, 2))
print(round(final_cost3, 2))
print(round(final_cost4, 2))
print(round(final_cost5, 2))
print(round(electric_cost_flat, 2))

total_cost1 = final_cost1 + total_amount_room1
total_cost2 = final_cost2 + total_amount_room2
total_cost3 = final_cost3 + total_amount_room3
total_cost4 = final_cost4 + total_amount_room4
total_cost5 = final_cost5 + total_amount_room5
total_cost_flat = electric_cost_flat + total_amount_flat

print(round(total_cost1, 2))
print(round(total_cost2, 2))
print(round(total_cost3, 2))
print(round(total_cost4, 2))
print(round(total_cost5, 2))
print(round(total_cost_flat, 2))