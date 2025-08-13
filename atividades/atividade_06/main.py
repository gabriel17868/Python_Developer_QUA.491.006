"""
# TODO - Atividade: Crie um programa em que o usuário informa um ano e o programa exibe todo o calendário do ano informado pelo usuário.
# NOTE - O usuário poderá informar qualquer ano a partir de 1900.
# NOTE - Use a biblioteca 'calendar'
"""
import calendar

ano = int(input("Informe um ano para exibir o calendário desse ano: "))
if ano < 1900:
    print("Não é possível mostrar anos anteriores a 1900")
else:
    print(calendar.calendar(ano))


