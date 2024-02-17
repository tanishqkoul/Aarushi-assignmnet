import sys
import math
from collections import Counter

def calculate_statistics(numbers):

    # Calculate a descriptive statistics for a list of numbers.
    # Args:
    #  numbers (list): List of numeric values.
    # Returns:
    # - Tuple containing Average, Maximum, Minimum, Variance, Standard Deviation, Median.

    n = len(numbers)
    if n == 0: 
        return None, None, None, None, None, None
    # Why there are 5 None
    # Average (None): There is no average to calculate if there are no numbers.
    # Maximum (None): There is no maximum value if there are no numbers.
    # Minimum (None): There is no minimum value if there are no numbers.
    # Variance (None): There is no variance to calculate if there are no numbers.
    # Standard Deviation (None): There is no standard deviation to calculate if there are no numbers.
    # Median (None): There is no median to calculate if there are no numbers.

    # Calculate average
    average = sum(numbers) / n
    
    # Calculate variance
    variance = sum((x - average) ** 2 for x in numbers) / n
    
    # Calculate standard deviation
    std_dev = math.sqrt(variance)

    # Sort the numbers for calculating median
    sorted_numbers = sorted(numbers)
    middle = n // 2

    # Calculate median
    if n % 2 == 0:
        median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        median = sorted_numbers[middle]

    return average, max(numbers), min(numbers), variance, std_dev, median

def main():
    # Check if command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: stats_in_python.py <input_file> <column_to_parse>")
        sys.exit(1)

# sys.argv is a Python list that contains the command-line arguments supplied to the script.
# Len(sys.argv) verifies the length of this list.
# The condition len(sys.argv)!= 3 determines if there are precisely three command-line arguments (the script name counts as the first parameter).



    # Extract command-line arguments
    input_file = sys.argv[1]
    column_to_parse = int(sys.argv[2])

    numbers = []  # List to store numeric values from the specified column

    try:
        # Read the input file and extract numeric values from the specified column
        with open(input_file, 'r') as infile:
            for line_number, line in enumerate(infile, start=1):
                try:
                    num = float(line.split("\t")[column_to_parse])
                    numbers.append(num)
                except (IndexError, ValueError) as e:
                    # Handle cases where the numeric value cannot be extracted
                    if isinstance(e, IndexError):
                        print(f"Exiting: There is no valid 'list index' in column {column_to_parse} "
                              f"in line {line_number} in file: {input_file}")
                    elif isinstance(e, ValueError):
                        print(f"Skipping line number {line_number} : {e}")
                    continue

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    # Check if there are valid numbers in the list
    if not numbers:
        print(f"Error: There were no valid number(s) in column {column_to_parse} in file: {input_file}")
        sys.exit(1)

    # Calculate descriptive statistics
    count = len(numbers)
    valid_num = count - numbers.count(math.nan)
    average, max_num, min_num, variance, std_dev, median = calculate_statistics(numbers)

    # Print the results in the specified format
    print(f"    Column: {column_to_parse} \n \n"
          f"        Count     =   {count:.3f}\n\n"
          f"        ValidNum  =   {valid_num:.3f}\n\n"
          f"        Average   =   {average:.3f}\n\n"
          f"        Maximum   =   {max_num:.3f}\n\n"
          f"        Minimum   =   {min_num:.3f}\n\n"
          f"        Variance  =   {variance:.3f}\n\n"
          f"        Std Dev   =   {std_dev:.3f}\n\n"
          f"        Median    =   {median:.3f}")

if __name__ == "__main__":
    main()
