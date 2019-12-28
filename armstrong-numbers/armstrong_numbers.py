def is_armstrong_number(number):

    order = len(str(number))

    sum = 0
    temp = number

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if number == sum:
        return True
    else:
        return False
