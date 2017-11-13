distance = float(input())
tank_capacity = float(input())
heavy_winds = float(input())

non_heavy_winds = distance - heavy_winds
non_heavy_winds *= 25
heavy_winds *= (25 * 1.5)
consumption = non_heavy_winds + heavy_winds
tolerance = consumption * 0.05
total_consumption = tolerance + consumption
remaining = tank_capacity - total_consumption

print('Fuel needed: {0}L'.format(round(total_consumption, 2)))
if remaining >= 0:
    print('Enough with {0}L to spare!'.format(round(remaining, 2)))
else:
    print('We need {0}L more fuel.'.format(round(abs(remaining), 2)))
