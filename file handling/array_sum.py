def array_numbers(numbers):
    total = 0
    for number in numbers:
        total +=  number
    return total

numbers = [6,5,2,5,10]
sum = array_numbers(numbers)
print(sum)