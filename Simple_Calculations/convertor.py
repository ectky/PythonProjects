cost = float(input())
from_currency = input()
in_currency = input()
is_bgn = False
bgn = 0.0

if from_currency == "USD":
    bgn = cost * 1.79549
elif from_currency == "EUR":
    bgn = cost * 1.95583
elif from_currency == "GBP":
    bgn = cost * 2.53405
elif from_currency == "BGN":
    bgn = cost

if in_currency == "USD":
    new = bgn / 1.79549
elif in_currency == "EUR":
    new = bgn / 1.95583
elif in_currency == "GBP":
    new = bgn / 2.53405
elif in_currency == "BGN":
    is_bgn = True

if is_bgn:
    print("{0:.2f} BGN".format(bgn))
else:
    print("{0:.2f} {1}".format(new, in_currency))
