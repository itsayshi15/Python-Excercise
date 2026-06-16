def process_numbers(num_list):

    original_list = num_list

    unique_values = list(set(num_list))

    result = {
        "original_list": original_list,
        "unique_values": unique_values,
        "unique_count": len(unique_values)
    }

    return result


numbers = [1, 2, 2, 3, 4, 4, 5]
output = process_numbers(numbers)

print(output)