def factorize(n: int, factors: dict = None) -> dict:
    '''Factorize a number into its prime factors.\n
    Return a dictionary of prime factors and their multiplicity.\n
    Arguments:
        n: the number to factorize
        factors: a dictionary of prime factors and their multiplicity'''
    if factors == None:
        factors = {}
    if n == 1:
        return factors
    i = 2 if len(factors) == 0 else list(factors.keys())[-1]
    while i * i <= n:
        for factor in factors.values():
            if i % factor == 0:
                break
        if n % i == 0:
            factors[i] = factors[i] + 1 if i in factors else 1
            return factorize(n // i, factors)
        i += 1
    factors[n] = factors[n] + 1 if n in factors else 1
    return factors

def main():
    '''Main function'''
    print(factorize(int(input('Enter a number: '))))

if __name__ == '__main__':
    main()