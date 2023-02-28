#Program Calaculates and Displays Travel Expenses
#3/1/2023
#CTI-110 P2HW1-Travel 
#Sylvester Marshall
print('This program calculates and displays travel expenses')
print()
user_num = float(input('Enter Budget: '))
print()
dest = input('Enter your travel destination: ')
print()
fuel = float(input('How much do you think you will you spend on gas? '))
print()
hotel = float(input('Approximately, how much will you need for accomodation/hotel? '))
print()
food = float(input('Last, how much do you need for food? '))
print()
total = fuel + hotel + food
remain = user_num - total



print('------------Travel Expenses------------')
print(f'Location:           {dest:<20}')
print(f'Initial Budget:     ${user_num:,.2f}')
print(f'Fuel:               ${fuel:,.2f}')
print(f'Accommodation:      ${hotel:,.2f}')
print(f'Food:               ${food:,.2f}')
print('---------------------------------------')
print()
print(f'Remaining Balance:  ${remain:,.2f}')
