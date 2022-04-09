def factorize(n: int, num: dict = None) -> dict:
    '''Factorize a number into its prime factors.
    Return a dictionary of prime factors and their multiplicity.
    Arguments:
        n: the number to factorize
        num: a dictionary of prime factors and their multiplicity'''
    if num == None:
        num = {}
    if n == 1:
        return num
    i = 2 if len(num) == 0 else list(num.keys())[-1]
    while i * i <= n:
        for factor in num.values():
            if i % factor == 0:
                break
        if n % i == 0:
            num[i] = num[i] + 1 if i in num else 1
            return factorize(n // i, num)
        i += 1
    num[n] = num[n] + 1 if n in num else 1
    return num

def main():
    '''Main function'''
    print(factorize(int(input('Enter a number: '))))

if __name__ == '__main__':
    main()