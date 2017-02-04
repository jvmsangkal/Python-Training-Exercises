def diamond(n):
    for i in range(n):
        str = ''
        x = i + 1
        for j in range(n - x):
            str += ' '

        for j in range(x):
            str += '1 '

        print(str)

    for i in range(n - 1):
        str = ''
        for j in range(i + 1):
            str += ' '

        for j in range(n - i - 1):
            str += '1 '

        print(str)

# diamond(1)
# diamond(2)
diamond(3)
