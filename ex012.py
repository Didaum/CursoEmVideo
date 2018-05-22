"""Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto"""

preço = float(input('Informe o preço do produto R$ '))
desconto = (5 * preço) / 100
print('O preço com desconto de 5% fica R${}'.format(preço - desconto))
