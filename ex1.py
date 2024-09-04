# Q1: out put :[1,3,5,7,9]
def even_numbers(array):
    even_numbers = []
    for number in array:
        if number % 2 == 1:
            even_numbers.append(number)
    return even_numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_numbers(numbers))