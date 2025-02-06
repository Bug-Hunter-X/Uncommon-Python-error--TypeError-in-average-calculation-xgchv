def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage with a list containing a string
my_list = [10, 20, '30', 40]
result = calculate_average(my_list)
print(f"Average: {result}")

#Example usage with a list containing None
my_list = [10, 20, None, 40]
result = calculate_average(my_list)
print(f"Average: {result}")
