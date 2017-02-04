def prime_numbers(numbers):
    def is_prime(x):
        if x == 1:
            return False

        for i in range(2, int(x/2) + 1):
            if (x % i == 0):
                return False

        return True

    return [n for n in numbers if is_prime(n)]

print(prime_numbers(range(1, 1000)))
