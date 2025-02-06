def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage with a list containing a string
my_list = [10, 20, '30', 40]
result = calculate_average(my_list)
print(f"Average: {result}")

#Example usage with a list containing None
my_list = [10, 20, None, 40]
result = calculate_average(my_list)
print(f"Average: {result}")