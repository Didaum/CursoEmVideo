"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor
do seno, cosseno e tangente desse ângulo"""

from math import cos, sin, tan

angulo = int(input('Digite o ângulo: '))
cosseno = cos(angulo)
seno = sin(angulo)
tangente = tan(angulo)

print('Cosseno: {:.2f}\nSeno: {:.2f}\nTangente: {:.2f}'.format(cosseno, seno, tangente))
