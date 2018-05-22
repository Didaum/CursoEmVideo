"""Faça um programa que leia a altura e a largura de uma parede
em metros, calcule a sua área e a quantidade de tinta necessário para
pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrados"""

altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede'))
tinta = (altura * largura) / 2
print('Você vai precisar de {} litros de tinta para pintar a parede.'.format(tinta))
