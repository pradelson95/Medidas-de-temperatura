#created by pradelson francois 24/1/2021

from time import sleep


print("1.De Celsius a Fahrenheit\n")
print("2.De Fahrenheit a Celsius\n")

def medidasDetemperatura():

   choose = float(input("ingrese una opción de menú con numeros:"))

   if choose==1:
     Celsius = float(input("por favor, introduzca la temperatura en Celsius:"))
     sleep(1)

     CelsiusAfahrenheit = Celsius*(9/5) + 32

     print(f"{Celsius} grados Celsius a Fahrenheit es igual a {CelsiusAfahrenheit}")

   else: 
    Fahrenheit = float(input("por favor, introduzca la temperatura en Fahrenheit:"))

    FahrenheitAcelsius = (Fahrenheit-32)*(5/9)

    print(f"{Fahrenheit} grados Fahrenheit en Celsius es igual a {FahrenheitAcelsius}")


medidasDetemperatura()


