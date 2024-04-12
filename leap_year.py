def leap_year():
    año= int(input("ingrese un año: "))
    if año >= 100 and año%400==0:
        print(f"El año {año} es bisiesto")
    elif año<100 and año%4==0:
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")
