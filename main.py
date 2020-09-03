temp = input("Enter temperature: ") 
unit = input("Enter unit in F/f or C/c: ")
if unit == "F" or unit == "f":
  tempC = temp
  tempC = float(tempC)
  tempF = (tempC -32 ) * 5/9
  print(str(tempC) + "° in Fahrenheit is equivalent to " + str(tempF) + "° Celsius.")
elif unit == "C" or unit == "c":
  tempF = temp
  tempF = float(tempF)
  tempC = (tempF *9/5) + 32
  print(str(tempF) + "° in Celsius is equivalent to " + str(tempC) + "° Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")

#a
