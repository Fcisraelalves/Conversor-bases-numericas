def int_to_binary(n : int):

    binary_digits = []
    result = 0
    while result != 1:
        result = n // 2
        rest = n % 2
        binary_digits.append(rest)
        n = result

    binary_digits.append(1)
    

    binary_number = 0
    for char in binary_digits[::-1]:
        if char == 1:
            binary_number *= 10
            binary_number += 1
        else:
            binary_number *= 10
    
    return binary_number




