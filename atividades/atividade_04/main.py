"""
# TODO - Atividade: Crie um programa que mostre a hora atual sempre sendo atualizada a cada segundo.
# NOTE - Para interromper o programa, use a tecla de atalho Ctrl+C
"""

import datetime 
import os
import time

n = 0
while n < 1:
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    time.sleep(1)
    os.system("cls" if os.name =="nt" else "clear")
    print(hora)


    