# queation2 :Output: [1, 2, 3]
def positive_numbers(number):
    positive_numbers =[]
    for numbers in number:
        if numbers > 0:
            positive_numbers.append(numbers)
    return positive_numbers
numbers = [-3, -2, -1, 0, 1, 2, 3] 
print(positive_numbers(numbers)) 



