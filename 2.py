from pprint import pprint

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def get_hour(self):
        return self._hour

    def get_min(self):
        return self._minute

    def get_sec(self):
        return self._second



    def __add__(self, other):
        result = Time()
        result.hour = self.get_hour() + other.get_hour()
        result.minute = self.get_min() + other.get_min()
        result.second = self.get_sec() + other.get_sec()
        if result.second>=60:
            result.second-=60
            result.minute+=1
        if result.minute>=60:
            result.minute-=60
            result.hour+=1
        return result

    def __sub__(self, other):
        result = Time()
        result.hour = self.get_hour() - other.get_hour()
        result.minute = self.get_min() - other.get_min()
        result.second = self.get_sec() - other.get_sec()
        if result.second<0:
            result.minute-=1
            result.second+=60
        if result.minute<0:
            result.hour-=1
            result.minute+=60
        return result

    def convert_to_hours(self, seconds):
        result = Time()
        result.hour = seconds // 3600
        result.minute = (seconds % 3600) // 60
        result.second = (seconds % 3600) % 60
        return result

    def convert_to_sec(self,):
        result = self.get_hour() * 3600 + self.get_min() * 60 + self.get_sec()
        return result

    def show(self):
        return str(self.get_hour())+':'+str(self.get_min())+':'+str(self.second)

def getTimes():
    hour = input("enter hour : ")
    minute = input("enter  minute : ")
    second = input("enter second : ")
   
    return second,minute,hour

def main():
    nom1 , nom2 , nom3  = getTimes()
    time1 = Time(int(nom1),int(nom2),int(nom3))
    nom4 , nom5 , nom6   = getTimes()
    time2 = Time(int(nom4),int(nom5),int(nom6))
    while True:
          tranz = input(" 1 baray jam  /// 2 baraye tafrigh ///  3 tablid be saat (baray avali) ///  4 tablid be saat (baray avali)  /// 5 tablid be sanie (baray avali): /// 5 tablid be sanie (baray dovomi): /// 6 ex ")
          if int(tranz) == 1:
              a = time1 + time2
              print(str(a.hour) + "/" + str(a.minute) + "/" + str(a.second))
          elif int(tranz) == 2:
              a = time1 - time2
              print(str(a.hour) + "/" + str(a.minute) + "/" + str(a.second))
          elif int(tranz) == 3:
              a = time1.convert_to_hours(int(nom3))
              print(str(a))
          elif int(tranz) == 4:
               a = time1.convert_to_hours(int(nom6))
               print(str(a))
          elif int(tranz) == 5:
                print(time1.convert_to_sec())
          elif int(tranz) == 6:
                print(time2.convert_to_sec())
          elif int(tranz) == 7:
                exit()


if __name__ == "__main__":
    main()