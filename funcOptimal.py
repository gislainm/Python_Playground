def num_days(month):
    longer = ['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec']
    mid = ['apr', 'jun', 'sep', 'nov']
    shorter = ['feb']
    if month in longer:
        print('number of days in', month, 'is', 31)
    elif month in shorter:
        print('number of days in', month, 'is', 28)
    elif month in mid:
        print('number of days in', month, 'is', 30)


num_days('feb')
# optimize/shorten the code in the function
# try to reduce the number of conditionals
