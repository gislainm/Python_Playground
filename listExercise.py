sales_w1 = [7, 3, 42, 19, 15, 35, 9]
sales_w2 = [12, 4, 26, 10, 7, 28]
sales = []
day_7_w2 = input('what was your sale on day7 week2?: ')
sales_w2.append(int(day_7_w2))
sales.extend(sales_w1)
sales.extend(sales_w2)
best_day = max(sales) * 1.5
worst_day = min(sales) * 1.5
total = best_day + worst_day
print(best_day)
print(worst_day)
print(total)
