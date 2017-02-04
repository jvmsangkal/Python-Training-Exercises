def castle(n):
    for i in range(n):
        str = ''
        x = i + 1
        for j in range(x):
            str += '1'

        for j in range(n - x):
            str += ' '
        for j in range(n - x):
            str += ' '

        for j in range(x):
            str += '1'

        print(str)

