""" Faça um programa que leia algo do teclado e mostre na tela
 o seu tipo primitivo e todas as informações possíveis sobre ele """

info = input('Digite algo: ')
print('O tipo primitivo desse valor é: {}'.format(type(info)))
print('É alfanumérico? {}'.format(info.isalnum()))
print('É um número? {}'.format(info.isnumeric()))
print('Está em minúsculas? {}'.format(info.islower()))
print('Está em maiúsculas? {}'.format(info.isupper()))
print('Só tem espaços? {}'.format(info.isspace()))
print('É alfabético? {}'.format(info.isalpha()))
print('Está capitalizado? {}'.format(info.istitle()))
