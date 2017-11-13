racing_hours = int(input())
people = int(input())
average_laps_per_p = int(input())
route_length = int(input())
route_capacity = int(input())
money_per_km = float(input())

if route_capacity * racing_hours > people:
    total_meters = people * average_laps_per_p * route_length
    total_km = total_meters / 1000
    print('Money raised: {0:.2f}'.format(total_km * money_per_km))
else:
    total_meters = route_capacity * racing_hours * average_laps_per_p * route_length
    total_km = total_meters / 1000
    print('Money raised: {0:.2f}'.format(total_km * money_per_km))

