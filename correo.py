#programa que permite creación correo

edad = int(input("Ingrese su edad: "))

if edad >=8:
    nombre = input("ingrese su primer nombre o nombre favorito: ")
    print("Su correo es: "+nombre+"@gmail.com")
else:
    print("Tas muy chiqui para hablar por hotmail")