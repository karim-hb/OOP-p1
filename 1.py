from math import gcd
class Fraction:

    def __init__(self, nom1=0, nom2=0):
        self._nom1 = nom1
        self._nom2 = nom2

    def reduce(self, frac):
        simple=gcd(frac._nom1 , frac._nom2)
        frac._nom1 = frac._nom1  // simple  
        frac._nom2 = frac._nom2 //  simple
        return frac
        
    def get_Nom1(self):
        return self._nom1
    

    def get_Nom2(self):
        return self._nom2

    def __repr__(self):
        return str(self._nom1) + "/" + str(self._nom2)


    def __add__(self,other):
         n1 = self.get_Nom1()*other.get_Nom2() + self.get_Nom2()*other.get_Nom1()
         n2 = self.get_Nom2() * other.get_Nom2()
         return self.reduce(Fraction(n1,n2))
    
    def __sub__(self,other):
         n1 = self.get_Nom1() * other.get_Nom2() - other.get_Nom1() * self.get_Nom2()
         n2 = self.get_Nom1() * other.get_Nom1()
         return self.reduce(Fraction(n1,n2))

    def __mult__(self,other):
         n1 = self.get_Nom1() * other.get_Nom1()
         n2 = self.get_Nom2() * other.get_Nom2()
         return self.reduce(Fraction(n1,n2))
    
    def __truediv__(self,other):
         n1 = self.get_Nom1() * other.get_Nom2()
         n2 = self.get_Nom2() * other.get_Nom1()
         return self.reduce(Fraction(n1,n2))






def getNumbers():
    nom1 = input("enter sorate kasr : ")
    nom2 = input("enter makhraj kasr : ")
    return nom1,nom2

def main():
    nom1 , nom2  = getNumbers()
    fraction1 = Fraction(int(nom1),int(nom2))
    nom1 , nom2  = getNumbers()
    fraction2 = Fraction(int(nom1),int(nom2))
    while True:
          tranz = input(" 1 baray jam 2 baraye tafrigh 3 baray zard 4 baray taghsim  5 baraye khoroj :  ")
          if int(tranz) == 1:
              print(fraction1 + fraction2)
          elif int(tranz) == 2:
              print(fraction1 - fraction2)
          elif int(tranz) == 3:
              print(fraction1 * fraction2)
          elif int(tranz) == 4:
               print(fraction1 / fraction2)
          elif int(tranz) == 5:
                exit()


if __name__ == "__main__":
    main()