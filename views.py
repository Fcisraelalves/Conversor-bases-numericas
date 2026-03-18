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

def int_to_hexa(n : int):
    values = {x : y for x, y in zip(range(10, 16), ['A', 'B', 'C', 'D', 'E', 'F'])}
    hexa_digits = []
    result = 16
    while result >= 16:
        result = n // 16
        rest = n % 16
        hexa_digits.append(rest)
        n = result

    hexa_digits.append(result)

    hexa_number = ''
    for char in hexa_digits[::-1]:
        if char <= 9:
            hexa_number += str(char)
        else:
            hexa_number += values[char]

    return hexa_number

def int_to_octal(n : int):
    octal_digits = []
    result = 8
    while result >= 8:
        result = n // 8
        rest = n % 8
        octal_digits.append(rest)
        n = result

    octal_digits.append(result)

    octal_number = 0
    for char in octal_digits[::-1]:
        if char <= 7 and char != 0:
            octal_number *= 10
            octal_number += char
        else:
            octal_number *= 10
    
    return octal_number


