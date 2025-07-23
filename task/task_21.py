for i in range(33, 127):  # ASCII range for '!' to '~'
    char = chr(i)
    decimal_value = i
    hexadecimal_value = hex(i)

    print(f"{char} {decimal_value} {hexadecimal_value}", end='\t')

    if (i - 32) % 5 == 0: 
        print()
