import time

class CarmichaelNumber:
  __benchPrime = [3, 5]
  listAllPrimes = [3, 5]

  def __init__(self) -> None:
    self.__max = 100000000

  def computeAllCarmichael(self, max:int) -> None:
    self.__max, start = max, time.time()
    for index in range(2, max // 2):
      isCarmichael = 2 * index + 1
      if self.__testCarmichael(isCarmichael):
        print(isCarmichael)
    print("delay is {} sec".format('{:.2f}'.format(time.time() - start)))

  def computeBigMersenne(self, numberOfMersennePrimes:int):
    listMersennePrimes= [(1, 2, 3), (2, 3, 7), (3, 5, 31)]
    while len(listMersennePrimes) <= numberOfMersennePrimes:
      prime, mersenne = self.__computeNextMersennePrime()
      listMersennePrimes.append((len(listMersennePrimes), prime, mersenne))
      print("le nombre premier de Mersenne de numéro {} est associé au nombre premier {} et contient {} chiffres".format(len(listMersennePrimes), prime, len(str(mersenne))))
      print("il vaut : ", mersenne)
      print()
      
    
  def __computeNextMersennePrime(self):
    next = None
    while True:
      next = CarmichaelNumber.listAllPrimes[-1] + 2 if next == None else next + 2
      listFactors = self.__computeFactors(next, [], CarmichaelNumber.listAllPrimes)
      if len(listFactors) == 1:
        prime, mersenne = listFactors[0], 2 ** listFactors[0] - 1
        if self.testLucasLhemer(prime, mersenne):
          return [prime, mersenne]

  def __testCarmichael(self, isCarmichael:int) -> bool:
    if not self.testFermat(isCarmichael):
      return False
    setFactors = set(self.__computeFactors(isCarmichael, [], CarmichaelNumber.listAllPrimes))
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

  def testLucasLhemer(self, prime:int, mersenne:int):
    index, suiteValue = 1, 4
    while index < prime - 1:
      suiteValue = (suiteValue ** 2 - 2) % mersenne
      index += 1
    return suiteValue == 0

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
object.computeBigMersenne(21)
