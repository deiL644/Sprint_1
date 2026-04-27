def digit_root(num):
    while num >= 10:
        sum_digits = 0
        for digit in str(num):
            sum_digits += int(digit)
        num = sum_digits
    return num

# Проверка
num = 97569
print(f"{num} корень равен {digit_root(num)}")