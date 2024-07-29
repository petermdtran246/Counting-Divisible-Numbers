def count_divisible_numbers_of_entries(array, divisor):
    """
    Counts the number of entries in the array that are divisible by the given divisor.

    :parameter:
    --------------------------------------------------------------------------------
        array: A list of integers.
        divisor: A positive integer.

    :return:
    -------------------------------------------------------------------------------
        int: The number of entries in the array that are divisible by the divisor.
    """
    count = 0
    # Iterate through each number in the array
    for num in array:
        # # Check if the current number is divisible by the divisor
        if num % divisor == 0:
            count += 1 # Increment the count if the number is divisible
    return count

if __name__ == "__main__":
    # Ask user to input the number of entries
    array_input = input('Enter the array elements of integers: ')
    array = list(map(int, array_input.split()))

    # Ask user to input the divisor
    divisor = int(input('Enter the positive integer divisor: '))

    result = count_divisible_numbers_of_entries(array, divisor)
    print(f'Number of entries in {array} that are divisible by {divisor}: {result}')


