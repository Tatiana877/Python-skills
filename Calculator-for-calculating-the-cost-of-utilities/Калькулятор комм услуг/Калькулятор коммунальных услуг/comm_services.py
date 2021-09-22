cold1_act = int(input('Введите текущие показания счетчика ХВ к.1 №105: '))
cold2_act= int(input('Введите текущие показания счетчика ХВ к.2 №500: '))
cold3_act = int(input('Введите текущие показания счетчика ХВ к.3 №205: '))
cold4_act = int(input('Введите текущие показания счетчика ХВ к.4 №101: '))
cold5_act = int(input('Введите текущие показания счетчика ХВ к.5 №459: '))
cold_flat_act = int(input('Введите текущие показания счетчика общ. ХВ кв.3 №449: '))

hot1_act = int(input('Введите текущие показания счетчика ГВ к.1 №606: '))
hot2_act = int(input('Введите текущие показания счетчика ГВ к.2 №107: '))
hot3_act = int(input('Введите текущие показания счетчика ГВ к.3 №004: '))
hot4_act = int(input('Введите текущие показания счетчика ГВ к.4 №707: '))
hot5_act = int(input('Введите текущие показания счетчика ГВ к. 5 №930: '))
hot_flat_act = int(input('Введите текущие показания счетчика ГВ общ. кв.3 №927: '))

cold_water_tariff = 42.30
hot_water_tariff = 205.15
water_removal_tariff = 30.90

cold_water_cost_room1 = (cold1_act - cold1_prev) * cold_water_tariff
cold_water_cost_room2 = (cold2_act - cold2_prev) * cold_water_tariff
cold_water_cost_room3 = (cold3_act - cold3_prev) * cold_water_tariff
cold_water_cost_room4 = (cold4_act - cold4_prev) * cold_water_tariff
cold_water_cost_room5 = (cold5_act - cold5_prev) * cold_water_tariff
cold_water_cost_flat = (cold_flat_act - cold_flat_prev)*cold_water_tariff

hot_water_cost_room1 = (hot1_act - hot1_prev) * hot_water_tariff
hot_water_cost_room2 = (hot2_act - hot2_prev) * hot_water_tariff
hot_water_cost_room3 = (hot3_act - hot3_prev) * hot_water_tariff
hot_water_cost_room4 = (hot4_act - hot4_prev) * hot_water_tariff
hot_water_cost_room5 = (hot5_act - hot5_prev) * hot_water_tariff
hot_water_cost_flat = (hot_flat_act - hot_flat_prev)*hot_water_tariff

water_removal_cost_room1 = ((cold1_act - cold1_prev) + (hot1_act - hot1_prev)) * water_removal_tariff
water_removal_cost_room2 = ((cold2_act - cold2_prev) + (hot2_act - hot2_prev)) * water_removal_tariff
water_removal_cost_room3 = ((cold3_act - cold3_prev) + (hot3_act - hot3_prev)) * water_removal_tariff
water_removal_cost_room4 = ((cold4_act - cold4_prev) + (hot4_act - hot4_prev)) * water_removal_tariff
water_removal_cost_room5 = ((cold5_act - cold5_prev) + (hot5_act - hot5_prev)) * water_removal_tariff
water_removal_cost_flat = ((cold_flat_act - cold_flat_prev) + (hot_flat_act - hot_flat_prev)) * water_removal_tariff

total_water_cost_room1 = cold_water_cost_room1 + hot_water_cost_room1 + water_removal_cost_room1
total_water_cost_room2 = cold_water_cost_room2 + hot_water_cost_room2 + water_removal_cost_room2
total_water_cost_room3 = cold_water_cost_room3 + hot_water_cost_room3 + water_removal_cost_room3
total_water_cost_room4 = cold_water_cost_room4 + hot_water_cost_room4 + water_removal_cost_room4
total_water_cost_room5 = cold_water_cost_room5 + hot_water_cost_room5 + water_removal_cost_room5
total_water_cost_flat = cold_water_cost_flat + hot_water_cost_flat + water_removal_cost_flat

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

total_amount_room1 = total_water_cost_room1 + heat1 + maint_room + contrib_room + lock_room
total_amount_room2 = total_water_cost_room2 + heat2 + maint_room + contrib_room + lock_room
total_amount_room3 = total_water_cost_room3 + heat3 + maint_room + contrib_room + lock_room
total_amount_room4 = total_water_cost_room4 + heat4 + maint_room + contrib_room + lock_room
total_amount_room5 = total_water_cost_room5 + heat5 + maint_room + contrib_room + lock_room
total_amount_flat = total_amount_room1 + total_amount_room2 + total_amount_room3 + total_amount_room4 + total_amount_room5

pprint('к/у студия 1: ', round(total_amount_room1, 2), ' руб.;')
print('к/у студия 2: ', round(total_amount_room2, 2), ' руб.;')
print('к/у студия 3: ', round(total_amount_room3, 2), ' руб.;')
print('к/у студия 4: ', round(total_amount_room4, 2), ' руб.;')
print('к/у студия 5: ', round(total_amount_room5, 2), ' руб.;')
print('к/у квартира: ', round(total_amount_flat, 2), ' руб.')
