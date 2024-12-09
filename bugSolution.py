def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    if sum(numbers) == 0:
        return 0 #Handle list with all zeros case 
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [10, 0, 20, 30]
average_with_zero = calculate_average(my_list_with_zero)
print(f"The average with zero: {average_with_zero}")

my_list_all_zeros = [0,0,0]
average_all_zeros = calculate_average(my_list_all_zeros)
print(f"The average with all zeros: {average_all_zeros}")
