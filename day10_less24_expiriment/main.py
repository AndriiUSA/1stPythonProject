def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('leap')
            else:
                print('Not leap')
        else:
            print('leap')
    else:
        print('Not leap')

# My adding
year = input('Print year')