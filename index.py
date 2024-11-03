import random

def juego():
   numeroSecreto = random.randint(1, 100)
   intentos = 0
   adivinado = False
   
   print("¡Bienvenido a mi primer proyecto en Python!")
   print("Adivina un número del 1 al 100")
   print("¡BUENA SUERTE!")
   
   while not adivinado:
      adivinanza = input("Ingrese un número del 1 al 100: ")
      
      if adivinanza.isdigit():
         adivinanza = int(adivinanza)
         intentos += 1
         
         if adivinanza < numeroSecreto:
            print(f"El numero secreto es mayor a {adivinanza}")
         elif adivinanza > numeroSecreto:
            print(f"El numero secreto es menor a {adivinanza}")
         else:
            print(f"¡Felicidades, has ganado! el número secreto es: {adivinanza}")
            print(f"Lo hiciste en {intentos} intentos!")
      else:
         print("Por favor ingrese un número y que sea entre el 1 y el 100")   
      
juego()