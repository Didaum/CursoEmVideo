"""Crie um programa que leia quanto dinehiro uma pessoa
tem na carteira e mostre quantos Dólares ele pode comprar."""
#Considere US$1,00 = R$3,27

real = float(input('Informe o valor R$ '))
dolar = real / 3.27
print('Você pode comprar US${:.2f}'.format(dolar))
