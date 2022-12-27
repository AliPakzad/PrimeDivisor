def isPrime(num):
    sqrtNum = int(num**0.5)
    if num > 1:
        for i in range(2,sqrtNum+1):
            if num%i == 0:
                return False
        return True

def CountPrimeFactors(num):
    limit = num
    PrimeFactors = set()
    if num > 1:
        while num%2 == 0:
            num = num/2
            PrimeFactors.add(2)
        for i in range(3,limit+1,2):
            if (isPrime(i) and num%i == 0):
                PrimeFactors.add(i)
                num = num/i

    return len(PrimeFactors)

numList = []

NumOfPrimeDivisors = 0

for i in range(1,11):
    inputNum = int(input())
    if CountPrimeFactors(inputNum) > NumOfPrimeDivisors:
        NumWithMaxPrimeDivisors = inputNum
        NumOfPrimeDivisors = CountPrimeFactors(inputNum)
        
    if CountPrimeFactors(inputNum) == NumOfPrimeDivisors and inputNum >NumWithMaxPrimeDivisors:
        NumWithMaxPrimeDivisors = inputNum
        NumOfPrimeDivisors = CountPrimeFactors(inputNum)


print(f"{NumWithMaxPrimeDivisors} {NumOfPrimeDivisors}")
