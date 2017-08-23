def Celc2Fahr(x):
    t = x * 1.800 + 32
    print("Celcius: " + str(x) + " Fahrenheit: " + str(t))

def Fahr2Celc(x):
    t = (x - 32)/1.800
    print("Fahrenheit: " + str(x) + " Celcius: " + str(t))

def Celc2Kelvin(x):
    t = x + 273
    print("Celcius: " + str(x) + " Kelvin: " + str(t))


def Kelvin2Celc(x):
    t = x - 273
    print("Kelvin: " + str(x) + " Celcius: " + str(t))

temp1 = input("Enter temperature(C*): ")
Celc2Fahr(int(temp1))
Celc2Kelvin(int(temp1))
temp2 = input("Enter temperature(K)")
Kelvin2Celc(int(temp2))





