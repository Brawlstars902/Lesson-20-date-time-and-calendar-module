def hotel_cost(nights):
    return 140*nights
def plane_cost(city):
    if 'Charlotte'==city:
        return 183
    elif 'Tampa'==city:
        return 220
    elif 'Pittsburgh'==city:
        return 222
    elif 'Los Angeles'==city:
        return 475
    else:
        print('Only options are \'Charlotte\',\'Tampa\',\'Pittsburgh\',\'Los Angeles\'. Please run again.')
def rental_car_cost(days):
    if days>=7:
        return 40*days-50
    elif days>=3:
        return 40*days-20
    else:
        return 40*days
    
def trip_cost(city,days,spending_money):
    return plane_cost(city)+hotel_cost(days)+rental_car_cost(days)+spending_money

x=input('What city are you going to? The only options are \'Charlotte\',\'Tampa\',\'Pittsburgh\',\'Los Angeles\'.\n  ')
y=int(input('How many days are you staying?\n  '))
z=int(input('How much extra money are you planning to spend on food and shopping?\n  '))

print('Total flight cost:  ',plane_cost(x))
print('Total hotel cost:  ',hotel_cost(y))
print('Total rental car cost:  ',rental_car_cost(y))

print('Total cost of the trip:',trip_cost(x,y,z))