metric_from = float(input())
name_from = input()
name_to = input()

if name_from == 'mm':
    metric_from /= 1000
elif name_from == 'cm':
    metric_from /= 100
elif name_from == 'mi':
    metric_from /= 0.000621371192
elif name_from == 'in':
   metric_from /= 39.3700787
elif name_from == 'km':
    metric_from /= 0.001
elif name_from == 'ft':
    metric_from /= 3.2808399
elif name_from == 'yd':
    metric_from /= 1.0936133

if name_to == 'mm':
    metric_from *= 1000
elif name_to == 'cm':
    metric_from *= 100
elif name_to == 'mi':
    metric_from *= 0.000621371192
elif name_to == 'in':
    metric_from *= 39.3700787
elif name_to == 'km':
    metric_from *= 0.001
elif name_to == 'ft':
    metric_from *= 3.2808399
elif name_to == 'yd':
    metric_from *= 1.0936133

print(str(metric_from) + ' ' + name_to)
