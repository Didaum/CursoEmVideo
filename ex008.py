"""Escreva um programa que leia o valor em metros
e o exiba convertido em centímetros e milímetros."""

metro = float(input('Informe a metragem: '))
centimetro = metro * 100
milimetro = metro * 1000
print('{} metros tem {:.0f} centimentros e {:.0f} milimetros'.format(metro, centimetro, milimetro))
