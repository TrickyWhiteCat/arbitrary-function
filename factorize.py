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
    for i in (range(list(num.keys())[-1], n + 1) if len(num) > 0 else range(2, n + 1)):
        if i * i > n:
            num[n] = num[n] + 1 if n in num else 1
            return num
        for factor in num.values():
            if i % factor == 0:
                break
        if n % i == 0:
            num[i] = num[i] + 1 if i in num else 1
            return factorize(n // i, num)

def main():
    '''Main function'''
    print(factorize(int(input('Enter a number: '))))

if __name__ == '__main__':
    main()