temp = input("Enter temperature: ") 
unit = input("Enter unit in F/f or C/c: ")
if unit == "F" or unit == "f":
  tempC = temp
  tempC = float(tempC)
  tempF = (tempC -32 ) * 5/9
  print(str(tempC) + "° in Celsius is equivalent to " + str(tempF) + "° Fahrenheit.")
if unit == "C" or unit == "c":
  tempF = temp
  tempF = float(tempF)
  tempC = (tempF *9/5) + 32
  print(str(tempF) + "° in Fahrenheit is equivalent to " + str(tempC) + "° Celsius.")
else:
    print(f"Invalid unit ({unit}).")

