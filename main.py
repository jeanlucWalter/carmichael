import time

class CarmichaelNumber:
  __benchPrime = [3, 5]
  listAllPrimes = [3, 5]

  def __init__(self) -> None:
    self.__max = 0

  def computeAllCarmichael(self, max:int) -> None:
    self.__max, start = max, time.time()
    for index in range(2, max // 2):
      isCarmichael = 2 * index + 1
      if self.__testCarmichael(isCarmichael):
        print(isCarmichael)
    print("delay is {} sec".format('{:.2f}'.format(time.time() - start)))

  def __testCarmichael(self, isCarmichael) -> bool:
    if not self.testFermat(isCarmichael):
      return False
    setFactors = set(self.__computeFactors(isCarmichael, [], self.listAllPrimes))
    if len(setFactors) < 3:
      return False
    for prime in setFactors:
      if (isCarmichael - 1) % (prime - 1) != 0:
        return False
    return True

  def __computeFactors(self, isCarmichael:int, listFactors:'list(int)', listAllPrimes:'list[int]') -> 'list(int)':
    prime = listAllPrimes[0]
    if prime ** 2 > isCarmichael:
      if isCarmichael ** 2 < self.__max and isCarmichael > listAllPrimes[-1]:
        self.listAllPrimes.append(isCarmichael)
      return listFactors + [isCarmichael]
    while isCarmichael % prime == 0:
      listFactors.append(prime)
      isCarmichael //= prime
      if isCarmichael == 1:
        return listFactors
    if len(listAllPrimes) == 1:
      return listFactors  + [isCarmichael]
    return self.__computeFactors(isCarmichael, listFactors, listAllPrimes[1:])

  def testFermat(self, numberTested:int) -> bool:
        for prime in CarmichaelNumber.listAllPrimes:
            if numberTested % prime != 0:
              return CarmichaelNumber.expModular(prime, numberTested - 1, numberTested) == 1

  def testRabinMiller(self, numberTested:int) -> bool:
    expTwo = self.__computeExpTwo(numberTested - 1)
    for prime in CarmichaelNumber.listAllPrimes[:2]:
      if numberTested % prime != 0:
        expMod = CarmichaelNumber.expModular(prime, (numberTested - 1) // (2 * expTwo), numberTested)
        if expMod in [numberTested - 1,1]:
          return True
        while expTwo:
          expMod = CarmichaelNumber.expModular(expMod, 2, numberTested)
          if expMod == 1:
            return True
          expTwo -= 1
      return False

  def __computeExpTwo(self, numberTested:int, exp:int = 0) -> int:
    if numberTested % 2:
      return exp
    return self.__computeExpTwo(numberTested // 2, exp + 1)

  def expModular(base:int, exponent:int, modular:int) -> int:
    if exponent == 0: 
        return 1
    mulFactor = 1 if exponent % 2 == 0 else base
    return (CarmichaelNumber.expModular(base, exponent // 2, modular) ** 2 * mulFactor) % modular



object = CarmichaelNumber()
object.computeAllCarmichael(1000000)
