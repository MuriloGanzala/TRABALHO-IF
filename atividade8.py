#Faça um programa que leia 2 notas de um aluno, verifique se as notas são validas e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina.4

nota1= float(input('Digite a nota 1:'))
nota2= float(input('Digite a nota 2:'))

media= (nota1+nota2) /2

if 0.0<= nota1 <= 10.0 and 0.0 <=nota2 <=10.0:
    print(f'{media} essa é sua média')
else:
    print('A nota informada é invalida')