import time

class CarmichaelNumber:
  benchPrime = [3]
  listAllPrimes = [3]

  def __init__(self) -> None:
    self.numberChecked = 0
    self.__listFactor = []
    self.__max = 0

  def computeAllCarmichael(self, max:int) -> None:
    print("code started")
