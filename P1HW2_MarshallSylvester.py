#Program Calaculates and Displays Travel Expenses
#2/16/2023
#CTI-110 P1HW2-Travel Expense
#Sylvester Marshall
print('This program calculates and displays travel expenses')
print()
user_num = int(input('Enter Budget: '))
print()
dest = input('Enter your travel destination: ')
print()
fuel = int(input('How much do you think you will you spend on gas? '))
print()
hotel = int(input('Approximately, how much will you need for accomodation/hotel? '))
print()
food = int(input('Last, how much do you need for food? '))
print()


print('------------Travel Expenses------------')
print('Location:', dest)
print('Initial Budget:', user_num)
print()


print('Fuel:', fuel)
print('Accomodation:', hotel)
print('Food:', food)

total = int(fuel + hotel + food)
print()

remain = print('Remaining Balance:', user_num - total)
