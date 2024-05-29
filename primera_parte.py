print("Bienvenidos al juego de ADIVINA LA PALABRA")
nombre= input("¿Cuál es tu nombre?")
print(f"Bienvenido/a {nombre}, ¿comenzamos?")
respuesta = input("\nresponde que SI o NO: ")

if respuesta.upper() == "SI":
   print("COMENZAMOS")
   import random
   def adivina_la_palabra():
        palabras=["estrella", "marciano", "planeta","tierra", "galaxia","estratosfera", "saturno"]
        palabra_azar = random.choice(palabras)
        return palabra_azar
