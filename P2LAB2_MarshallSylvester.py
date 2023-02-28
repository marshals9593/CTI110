num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())



product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4) / 4

rounded_product_int = int(round(product))
rounded_average_int = int(round(average))

float_product = float(product)
float_average = float(average)

print(f'{rounded_product_int:.0f} {rounded_average_int:.0f}')
print(f'{float_product:.3f} {float_average:.3f}')
