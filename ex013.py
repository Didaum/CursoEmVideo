"""Faça um algoritmo que leia o salário de um funcionário e
mostre seu novo salário, com 15% de aumento"""

salario = float(input('Informe o salário R$ '))
aumento = (15 * salario) / 100
print('O salário com aumento de 15% é R${}'.format(salario + aumento))
