last_month, this_month = map(int, input().split())
vat = 0.1
rate1 = 1484
rate2 = 1533
rate3 = 1786
rate4 = 2242
rate5 = 2503
rate6 = 2587
used = this_month - last_month
if (used <= 50):
    fee = used * rate1
    print(int(fee * (1 + vat)))
elif (used <= 100):
    fee = 50 * rate1 + (used - 50) * rate2
    print(int(fee * (1 + vat)))
elif (used <= 200):
    fee = 50 * rate1 + 50 * rate2 + (used - 100) * rate3
    print(int(fee * (1 + vat)))
elif (used <= 300):
    fee = 50 * rate1 + 50 * rate2 + 100 * rate3 + (used - 200) * rate4
    print(int(fee * (1 + vat)))
elif (used <= 400):
    fee = 50 * rate1 + 50 * rate2 + 100 * rate3 + 100 * rate4 + (used - 300) * rate5
    print(int(fee * (1 + vat)))
else:
    fee = 50 * rate1 + 50 * rate2 + 100 * rate3 + 100 * rate4 + 100 * rate5 + (used - 400) * rate6
    print(int(fee * (1 + vat)))