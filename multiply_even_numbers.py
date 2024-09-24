# multiply_even_numbers
# Write a function called multiply_even_numbers. This function accepts a list of numbers and returns the product of all even numbers in the list.


def multiply_even_numbers(lst):
    total = 1
    for num in lst:
        if num % 2 == 0:
            total *= num
    return total
    