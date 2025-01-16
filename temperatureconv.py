def temperature(tempType,convert,temp):
    if tempType == 'K':
        if convert == "C":
            return temp - 273.15
        elif convert == "F":
            return 9 / 5 * (temp - 273.15) + 32
        elif convert =="K":
            return temp
    elif tempType =='C':
        if convert == "C":
            return temp
        elif convert == "F":
            return 9 / 5 * temp + 32
        elif convert == "K":
            return temp+273.15
    elif tempType =='F':
        if convert == "C":
            return 5/9*(temp - 32)
        elif convert == "F":
            return temp
        elif convert == "K":
            return 5/9*(temp-32)+273.15
    else:
        return "Invalid Input"
print("*"*30+"Temperature conversion"+"*"*30)

tempType=input("Enter to convert from 'K' for kelvin, 'C' for centigrade and 'F' for fahrenheit:")
tempType=tempType.upper()
temp=int(input("Enter temperature in "+tempType+": "))
convert=input("Enter the type to be converted to 'K' for kelvin, 'C' for centigrade and 'F' for fahrenheit:")
convert=convert.upper()


print(f"{temp} {tempType} = {temperature(tempType,convert,temp):.3f} {convert}")