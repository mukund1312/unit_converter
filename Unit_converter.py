# Unit Converter (temp, currency, volume, mass and more) -
# Converts various units between one another. The user enters
#  the type of unit being entered, the type of unit they want to
#  convert to and then the value. The program will then make the
# conversion.
print("Welcome to the converter")
c = int(input("enter 1 for temperaute\nenter 2 for mass\n enter 3 for 12h to 24h clock\n"))
if(c == 1):
    a = int(input("enter 1 for converting c to f or f to c\nenter 2 for converting c to k or k to c\n enter 3 for converting f to k or k to f"))
    temp = int(input("enter the temperature"))
    if (a == 1):
        b = int(input("enter 1 for c to f\nenter 2 for f to c"))
        if(b == 1):
            print(f"the temperature in farenhite is {(temp * (9/5)) + 32 }")
        elif(b == 2):
            print(f"the temperature in celcius is {(temp - 32) * (5/9) }")
        else:
            print("invalid input")
    elif(a == 2):
        b = int(input("enter 1 for c to k\nenter 2 for k to c"))
        if(b == 1):
            print(f"the temperature in kelvin is {temp+ 273.15}")
        elif(b == 2):
            print(f"the temperature in celcius is {temp-273.15}")
        else:
            print("invalid input")
    elif(a == 3):
        b = int(input("enter 1 for f to k\nenter 2 for k to f"))
        if(b == 1):
            print(
                f"the temperature in kelvin is {(temp - 32) * (5/9) + 273.15}")
        elif(b == 2):
            print(
                f"the temperature in farenhite is {(temp- 273.15) *(9/5) + 32}")
        else:
            print("invalid input")
    else:
        print("invalid input")
elif(c == 2):
    a = int(input("enter 1 for converting kgs to lbs or lbs to kgs\nenter 2 for converting g to lbs or lbs to g\nenter 3 for converting kg to ounce or ounce to kg\nenter 4 for converting lbs to ounce or ounce to lbs "))
    mass = int(input("enter the mass"))
    if (a == 1):
        b = int(input("enter 1 for kgs to lbs\nenter 2 for lbs to kgs"))
        if(b == 1):
            print(f"the mass in lbs is {mass*2.20462}")
        elif(b == 2):
            print(f"the mass in kgs is {mass/2.20462}")
        else:
            print("invalid input")
    elif(a == 2):
        b = int(input("enter 1 for g to lbs\nenter 2 for lbs to g"))
        if(b == 1):
            print(f"the mass in lbs is {mass/454}")
        elif(b == 2):
            print(f"the mass in g is {mass*454}")
        else:
            print("invalid input")
    elif(a == 3):
        b = int(input("enter 1 for kgs to ounce\nenter 2 for ounce to kgs"))
        if(b == 1):
            print(f"the mass in ounce is {mass*35.274}")
        elif(b == 2):
            print(f"the mass in kgs is {mass/35.274}")
        else:
            print("invalid input")
    elif(a == 4):

        b = int(input("enter 1 for lbs to ounce\nenter 2 for ounce to lbs"))
        if(b == 1):
            print(f"the mass in ounce is {mass*16}")
        elif(b == 2):
            print(f"the mass in lbs is {mass/16}")
        else:
            print("invalid input")
    else:
        print("invalid input")
elif(c == 3):
    a = int(input("enter 1 for converting 12h to 24h\n enter 2 converting 24h to 12h"))
    time = input("enter the time in this format(HH:MM AM or PM,if 12h)")
    if(a == 1):
        time = input("enter the time in this format(HH:MM AM or PM)")
        a1 = time[0:2]
        b1 = time[3:5]
        c1 = time[6:8]
        if (c1 == "AM" and a1 == "12"):
            print(f"the time in 24h format is 00:00")
        elif(c1 == "AM" and int(a1) < 12):
            print(f"the time in 24h format is {a1}:{b1}")
        elif(c1 == "PM" and a1 == "12"):
            print(f"the time in 24h format is 12:00")
        elif(c1 == "PM" and int(a1) < 12):
            print(f"the time in 24h format is {int(a1)+12}:{b1}")
        else:
            print("invalid input ")
    if(a == 2):
        time = input("enter the time in this format (HH:MM)")
        a1 = time[0:2]
        b1 = time[3:5]
        if (a1 == "00" and b1 == "00"):
            print(f"the time in 12h format is 12:00 AM")
        elif(a1 == "12" and b1 == "00"):
            print(f"the time in 12h format is 12:00 PM")
        elif(int(a1) > 12):
            print(f"the time in 12h format is {int (a1)-12}:{b1} PM")
        elif(int(a1) < 12):
            print(f"the time in 12h format is {a1}:{b1} AM")
        else:
            print("invalid input")


else:
    print("invalid input")
