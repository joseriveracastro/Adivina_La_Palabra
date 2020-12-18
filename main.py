#Juego de adivina la palabra
#Libreria para realizar el random
import random 
#Lista de palabras 
lista = ['buenos','dias','zapato','ojo','arbol']

#Para escoger la palabra
palabra = random.choice(lista)

#Tiene 3 oportunidades para adivinar
print('Bienvenido al juego adivina la palabra')
print('Tiene tres(3) oportunidades para adivinar')
conteo = 0
#While para las oportunidades
print('La cantidad de letras es' ,len(palabra))
while conteo != 3:
  conteo +=1
  palabra_adivinar = input('Adivine la palabra: ')
  if palabra.lower() != palabra_adivinar:
    print('No es la palabra')
    print(f'Le restan {3-conteo} oportunidades')
    if conteo == 1:
      print('La palabra termina con',palabra[-1])
    elif conteo ==2:
      print('La palabra comienza con',palabra[0])
    else:
      print('Fallo.. la palabra era',palabra)
  else:
    print('Adivino... felicidades')
    break


print('Fin del juego')
  
  
