#!/usr/bin/env python3

import os
from datetime import timedelta

os.system("clear")

'''
HrS = (HrE + HrT) + HrA
'''


def horaDaSaida(saida, entrada="00:00:00", saidaA="00:00:00", voltaA="00:00:00"):

    listaH = entrada.split(":")
    listaSaidaA = saidaA.split(":")
    listaVoltaA = voltaA.split(":")

    HrE = timedelta(hours=int(listaH[0]), minutes=int(
        listaH[1]), seconds=int(listaH[2]))
    HrT = timedelta(hours=8, minutes=00, seconds=00)
    HrVA = timedelta(hours=int(listaVoltaA[0]), minutes=int(
        listaVoltaA[1]), seconds=int(listaVoltaA[2]))
    HrSA = timedelta(hours=int(listaSaidaA[0]), minutes=int(
        listaSaidaA[1]), seconds=int(listaSaidaA[2]))
    HrA = (HrVA.total_seconds() - HrSA.total_seconds())
    HrS = ((HrE.total_seconds() + HrT.total_seconds()) + HrA)

    Saida = timedelta(seconds=HrS)

    if saida == '':
        HrTb = ((HrS - HrE.total_seconds()) - HrA)
        HorasTrabalhadas = timedelta(seconds=HrTb)
    else:
        listaSaida = saida.split(":")
        HrPS = timedelta(hours=int(listaSaida[0]), minutes=int(
            listaSaida[1]), seconds=int(listaSaida[2]))
        HrTb = ((HrPS.total_seconds() - HrE.total_seconds()) - HrA)
        HorasTrabalhadas = timedelta(seconds=HrTb)

    print(f"""
-------------------------------------
Hora da entrada............: {HrE}
Hora da saída para almoço..: {HrSA}
Hora da volta do almoço....: {HrVA}
Hora que deverá sair.......: {Saida}    
-------------------------------------
Ponto batido de saída......: {saida}
Horas trabalhadas no dia...: {HorasTrabalhadas}
      """)


print("A hora deve ser no formato hh:mm:ss\n")
entradaH = input("Entrada....................: ")
saidaAlmoco = input("Saída para almoço..........: ")
voltaAlmoco = input("Volta do almoço............: ")
pontoDeSaida = input("Hora da saída(opcional)....: ")

horaDaSaida(pontoDeSaida, entradaH, saidaAlmoco, voltaAlmoco)
