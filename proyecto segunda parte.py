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


   def mostrar_pantalla(palabra_oculta, aciertos, vidas_restantes):
       pantalla= ""
       for letra in palabra_oculta:
          if letra in aciertos:
             pantalla += letra
          else:
              pantalla += "-"
       print(pantalla)

   def jugar_ahorcado():
       palabra_oculta= adivina_la_palabra()
       aciertos=[]
       vidas_restantes= 3

       while vidas_restantes >0:
          mostrar_pantalla(palabra_oculta, aciertos, vidas_restantes)
          letra= input("Introduce una letra: ").lower()