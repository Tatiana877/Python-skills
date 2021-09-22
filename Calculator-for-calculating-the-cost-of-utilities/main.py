cold1_105_prev = 45
cold2_500_prev = 54
cold3_205_prev = 29
cold4_101_prev = 10
cold5_459_prev = 47
cold_flat_449_prev = 330
hot1_606_prev = 31
hot2_107_prev = 38
hot3_004_prev = 17
hot4_707_prev = 5
hot5_930_prev = 36
hot_flat_927_prev = 221

cold1_105_act = 53
cold2_500_act = 63
cold3_205_act = 33
cold4_101_act = 13
cold5_459_act = 48
cold_flat_449_act = 353
hot1_606_act = 33
hot2_107_act = 40
hot3_004_act = 17
hot4_707_act = 7
hot5_930_act = 36
hot_flat_927_act = 227

meter1_act_T1 = 411
meter1_act_T2 = 508
meter1_act_T3 = 579
meter2_act_T1 = 271
meter2_act_T2 = 328
meter2_act_T3 = 348
meter3_act_T1 = 189
meter3_act_T2 = 95
meter3_act_T3 = 244
meter4_act_T1 = 95
meter4_act_T2 = 87
meter4_act_T3 = 138
meter5_act_T1 = 107
meter5_act_T2 = 87
meter5_act_T3 = 114
meter_flat_act_T1 = 1170
meter_flat_act_T2 = 1202
meter_flat_act_T3 = 1564

meter1_prev_T1 = 374
meter1_prev_T2 = 458
meter1_prev_T3 = 528
meter2_prev_T1 = 252
meter2_prev_T2 = 294
meter2_prev_T3 = 320
meter3_prev_T1 = 154
meter3_prev_T2 = 76
meter3_prev_T3 = 215
meter4_prev_T1 = 93
meter4_prev_T2 = 84
meter4_prev_T3 = 135
meter5_prev_T1 = 100
meter5_prev_T2 = 81
meter5_prev_T3 = 107
meter_flat_prev_T1 = 1062
meter_flat_prev_T2 = 1081
meter_flat_prev_T3 = 1438

cold_water_tariff = 43.57
hot_water_tariff = 211.67
water_removal_tariff = 32.02

heating_flat = 2546.83 * 0.846339
heat1 = heating_flat * 0.18
heat2 = heating_flat * 0.21
heat3 = heating_flat * 0.20
heat4 = heating_flat * 0.26
heat5 = heating_flat * 0.15

maintenance_flat = 27.80 * 75.1
maint_room = maintenance_flat / 5

contribution_flat = 19.52 * 75.1
contrib_room = contribution_flat / 5

lock_flat = 60.80
lock_room = 60.80 / 5

cold_water_cost_room1 = (cold1_105_act - cold1_105_prev) * cold_water_tariff
cold_water_cost_room2 = (cold2_500_act - cold2_500_prev) * cold_water_tariff
cold_water_cost_room3 = (cold3_205_act - cold3_205_prev) * cold_water_tariff
cold_water_cost_room4 = (cold4_101_act - cold4_101_prev) * cold_water_tariff
cold_water_cost_room5 = (cold5_459_act - cold5_459_prev) * cold_water_tariff
cold_water_cost_flat = (cold_flat_449_act - cold_flat_449_prev)*cold_water_tariff

hot_water_cost_room1 = (hot1_606_act - hot1_606_prev) * hot_water_tariff
hot_water_cost_room2 = (hot2_107_act - hot2_107_prev) * hot_water_tariff
hot_water_cost_room3 = (hot3_004_act - hot3_004_prev) * hot_water_tariff
hot_water_cost_room4 = (hot4_707_act - hot4_707_prev) * hot_water_tariff
hot_water_cost_room5 = (hot5_930_act - hot5_930_prev) * hot_water_tariff
hot_water_cost_flat = (hot_flat_927_act - hot_flat_927_prev)*hot_water_tariff

water_removal_cost_room1 = ((cold1_105_act - cold1_105_prev) + (hot1_606_act - hot1_606_prev)) * water_removal_tariff
water_removal_cost_room2 = ((cold2_500_act - cold2_500_prev) + (hot2_107_act - hot2_107_prev)) * water_removal_tariff
water_removal_cost_room3 = ((cold3_205_act - cold3_205_prev) + (hot3_004_act - hot3_004_prev)) * water_removal_tariff
water_removal_cost_room4 = ((cold4_101_act - cold4_101_prev) + (hot4_707_act - hot4_707_prev)) * water_removal_tariff
water_removal_cost_room5 = ((cold5_459_act - cold5_459_prev) + (hot5_930_act - hot5_930_prev)) * water_removal_tariff
water_removal_cost_flat = ((cold_flat_449_act - cold_flat_449_prev) + (hot_flat_927_act - hot_flat_927_prev)) * water_removal_tariff

total_water_cost_room1 = (cold_water_cost_room1 + hot_water_cost_room1 + water_removal_cost_room1) - 18.89
total_water_cost_room2 = (cold_water_cost_room2 + hot_water_cost_room2 + water_removal_cost_room2) - 18.89
total_water_cost_room3 = (cold_water_cost_room3 + hot_water_cost_room3 + water_removal_cost_room3) - 18.89
total_water_cost_room4 = (cold_water_cost_room4 + hot_water_cost_room4 + water_removal_cost_room4) - 18.89
total_water_cost_room5 = cold_water_cost_room5 + hot_water_cost_room5 + water_removal_cost_room5
total_water_cost_flat = cold_water_cost_flat + hot_water_cost_flat + water_removal_cost_flat

total_amount_room1 = total_water_cost_room1 + heat1 + maint_room + contrib_room + lock_room
total_amount_room2 = total_water_cost_room2 + heat2 + maint_room + contrib_room + lock_room
total_amount_room3 = total_water_cost_room3 + heat3 + maint_room + contrib_room + lock_room
total_amount_room4 = total_water_cost_room4 + heat4 + maint_room + contrib_room + lock_room
total_amount_room5 = total_water_cost_room5 + heat5 + maint_room + contrib_room + lock_room
total_amount_flat = total_amount_room1 + total_amount_room2 + total_amount_room3 + total_amount_room4 + total_amount_room5

print('Коммунальные услуги, квитанция август 2021: ')
print('к/у студия 1: ', round(total_amount_room1, 2), ' руб.;')
print('к/у студия 2: ', round(total_amount_room2, 2), ' руб.;')
print('к/у студия 3: ', round(total_amount_room3, 2), ' руб.;')
print('к/у студия 4: ', round(total_amount_room4, 2), ' руб.;')
print('к/у студия 5: ', round(total_amount_room5, 2), ' руб.;')
print('к/у квартира: ', round(total_amount_flat, 2), ' руб.')

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

print('Свет, август 2021: ')
print('свет студия 1: ', round(final_cost1, 2), ' руб.')
print('свет студия 2: ', round(final_cost2, 2), ' руб.;')
print('свет студия 3: ', round(final_cost3, 2), ' руб.;')
print('свет студия 4: ', round(final_cost4, 2), ' руб.;')
print('свет студия 5: ', round(final_cost5, 2), ' руб.;')
print('свет квартира: ', round(electric_cost_flat, 2), ' руб.')

total_cost1 = final_cost1 + total_amount_room1
total_cost2 = final_cost2 + total_amount_room2
total_cost3 = final_cost3 + total_amount_room3
total_cost4 = final_cost4 + total_amount_room4
total_cost5 = final_cost5 + total_amount_room5
total_cost_flat = electric_cost_flat + total_amount_flat

print('Общая сумма: ')
print('Общая сумма, студия 1: ', round(total_cost1, 2), ' руб.;')
print('Общая сумма, студия 2: ', round(total_cost2, 2), ' руб.;')
print('Общая сумма, студия 3: ', round(total_cost3, 2), ' руб.;')
print('Общая сумма, студия 4: ', round(total_cost4, 2), ' руб.;')
print('Общая сумма, студия 5: ', round(total_cost5, 2), ' руб.;')
print('Общая сумма, квартира: ', round(total_cost_flat, 2), ' руб.')