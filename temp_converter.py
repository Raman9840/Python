#temperature converter: celcius to fahrenheit, fahrenheit to celcius
#ask user for temperature value and also for unit
#convert to vice versa

class calculator:
  def __init__(self,temp:float,unit:str):
    self.temp=temp
    self.unit=unit
  def cel_to_fah(self):
      x= (self.temp * 9/5) + 32
      print(x)
  def fah_to_cel(self):
      y= (self.temp - 32) * 5/9
      print(y)
  def convert(self):
    if self.unit=="c":
      self.cel_to_fah()
    else:
      self.fah_to_cel()
def main():
  units=['c','f']
  val=int(input("Enter the temperature"))
  unit=input("Enter the unit")
  if unit.lower() in units:
    cal:calculator=calculator(val,unit)
    cal.convert()
  else:
    print("Invalid unit")

if __name__=="__main__":
  main()