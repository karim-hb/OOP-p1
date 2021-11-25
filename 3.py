class ComplexNumber:
    def __init__(self, real=0, imaginary=0):
        self._nom1 = real
        self._nom2 = imaginary


    def get_Nom1(self):
        return self._nom1
    

    def get_Nom2(self):
        return self._nom2


    def __add__(self, other):
        result = ComplexNumber()
        result.real = self.get_Nom1() + other.get_Nom1()
        result.imaginary = self.get_Nom2() + other.get_Nom2()
        return result

    def __sub__(self, other):
        result = ComplexNumber()
        result.real = self.get_Nom1() - other.get_Nom1()
        result.imaginary = self.get_Nom2() - other.get_Nom2()
        return result

    def __mult__(self, other):
        result = ComplexNumber()
        result.real = self.get_Nom1() * other.get_Nom1() + self.get_Nom2() * -other.get_Nom2()
        result.imaginary = self.get_Nom1() * other.get_Nom2() + self.get_Nom2() * other.get_Nom1()
        return result

    def show(self):
        if self.get_Nom2() < 0:
            print(f"{self.get_Nom1()} - {-self.get_Nom2()}i")
        else:
            print(f"{self.get_Nom1()} + {self.get_Nom2()}i")



def getNumbers():
    nom1 = input("enter haghighi : ")
    nom2 = input("enter majazi : ")
    return nom1,nom2

def main():
    nom1 , nom2  = getNumbers()
    fraction1 = ComplexNumber(int(nom1),int(nom2))
    nom1 , nom2  = getNumbers()
    fraction2 = ComplexNumber(int(nom1),int(nom2))
    while True:
          tranz = input(" 1 baray jam 2 baraye tafrigh 3 baray zard  5 baraye khoroj :  ")
          if int(tranz) == 1:
              print(fraction1 + fraction2)
          elif int(tranz) == 2:
              print(fraction1 - fraction2)
          elif int(tranz) == 3:
              print(fraction1 * fraction2)
          elif int(tranz) == 5:
                exit()


if __name__ == "__main__":
    main()