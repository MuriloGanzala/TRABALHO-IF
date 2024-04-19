#Escreva um programa que, dada a idade de um atleta da categoria bocha rolada em cancha de terra, classifique-o em uma das seguintes categorias:

idade= float(input('Digite sua idade'))

if idade >=5 and idade <=7:
    print('Voce é da categoria infantil A')
elif idade>=8 and idade<=10:
    print('Sua categoria é infantil b')
elif idade>=11 and idade<=13:
    print('Juvenil A')
elif idade>=14 and idade<=17:
    print('Sua categoria é juvenil B')
else:
    print('categoria senior')