def roman_numerals(dec):
    constants = (
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    )

    res = ''
    for c in constants:
        while dec >= c[0]:
            dec -= c[0]
            res += c[1]

    print(res)

roman_numerals(1432)
