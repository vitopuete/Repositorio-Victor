import random
lanzamiento = random.randint(1,6)

adivinar = int(input('ingrese un numero, del 1 al 10'))

print('pertenecia del 1 al 5')

if lanzamiento==adivinar:
    print('Ganaste')
else: 
    print('Perdiste')
