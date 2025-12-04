import math


def p_quadrato():
    lato = float(input('Inserisci lato: '))
    return lato * 4

def p_cerchio():
    raggio = float(input('Inserisci raggio:'))
    return 2 * math.pi * raggio

def p_rettangolo():
    base = float(input('Inserisci la base'))
    altezza = float(input('Inserisci altezza'))
    return base *2 + altezza *2
    
print( 'Calcola il perimetro di una figura geometrica')

print('-Quadrato:1')
print ('-cerchio:2')

print ('-rettangolo:3')


print('Inserire la scelta')
scelta = int(input('-'))

if scelta == 1:
        risultato = p_quadrato()
        
        print(f'Il perimetro è {risultato}')

elif scelta == 2:
        risultato= p_cerchio()
        print(input(f'scegli raggio'))
        print('La circonferenza è: {risultato}')
elif scelta == 3:
        print(input(f'Scegli base:'))
        print(input(f'scegli altezza'))
        risultato = p_rettangolo
        print (f'La circonferenza è {risultato}')

else:
        print('errore')




   



        


                    




