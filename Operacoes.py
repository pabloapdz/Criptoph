import Imprimir_Erro
import estrategia
import Requisicoes
import Variaveis_Principais
import os
import sys
import time
from datetime import datetime, timedelta

Variaveis = Variaveis_Principais.Variaveis()
Saldo_Inicial = Variaveis['Saldo']
Placar_Ganhos = 0
Placar_Perdas = 0


Variaveis = estrategia.Variaveis()
Valor_Inicial = Variaveis['valor_da_aposta_inicial']
Tempo_De_Aposta = Variaveis['duracao_da_aposta']
Mercado_a_Apostar = Variaveis['Mercado']


def determinar_dendencia(velas_1min):
	tendencia_crescente = 0
	tendencia_decrescente = 0
	for i in range(len(velas_1min) - 1):
	    vela_atual = velas_1min[i]
	    vela_proxima = velas_1min[i + 1]

	    if vela_proxima["close"] > vela_atual["close"]:
	        tendencia_crescente += 1
	    elif vela_proxima["close"] < vela_atual["close"]:
	        tendencia_decrescente += 1

	if tendencia_crescente > tendencia_decrescente:
	    return "crescente"
	elif tendencia_decrescente > tendencia_crescente:
	    return "decrescente"
	else:
	    return "indefinida"


def Operar(direcao_aposta, Alimentacao_LOG, valor_da_aposta = Valor_Inicial, duracao_da_aposta = Tempo_De_Aposta, Mercado = Mercado_a_Apostar):
	try:
		print("definindo função de compra")
		realizar_operacao = Requisicoes.Operacao(
												{
												  "buy": 1,
												  "price": valor_da_aposta,
												  "parameters": { 
												    "amount": valor_da_aposta, 
												    "contract_type": direcao_aposta['Direcao'],
												    "basis": "stake", 
												    "currency": "USD",  
												    "duration_unit": "m",
												    "duration": duracao_da_aposta,
												    "symbol": Mercado
												  }
												}
											)
		horario_aposta = datetime.now()
		print('\n\n')
		print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||	HORARIO QUE APOSTOU:	",	horario_aposta )
		print('\n\n')
		print("apostou:	", realizar_operacao)
		print("\n ssssssssssssssssssssssssssssssss \n")
		print(valor_da_aposta, direcao_aposta, duracao_da_aposta,Mercado)
		print("\n ssssssssssssssssssssssssssssssss \n")
		print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
		print("indo pegar o saldo antes do resultado da aposta")
		Saldo_antes_Aposta = Requisicoes.Saldo()
		Saldo_antes_Aposta = float(Saldo_antes_Aposta)
		print('Saldo_antes_Aposta:	', Saldo_antes_Aposta)
		print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
		print("$"*90)
		print(realizar_operacao)
		print("$"*90)
		time.sleep((60 * duracao_da_aposta) + 10)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		erro = str(e) + " 	|| LINHA: " + str(exc_tb.tb_lineno)
		Imprimir_Erro.Printar(str(erro), str('Operacoes.py'), str('Operar'))
		pass
	return True, Saldo_antes_Aposta, horario_aposta, direcao_aposta, valor_da_aposta


def divisoes(n, d):
	return n / d if d else 0


def Resultado_Operacao(Saldo_Real, Direcao, Valor_Aposta):
	print("indo pegar resultado")
	global Saldo_Inicial, Placar_Ganhos, Placar_Perdas, Valor_Inicial
	print("indo pegar saldo")
	Saldo_Real_Atualizado = Requisicoes.Saldo()
	print("pegou saldo")
	print("Saldo_Real: ", Saldo_Real, "	Tipo:	", type(Saldo_Real))
	print("Saldo_Real_Atualizado: ", Saldo_Real_Atualizado, "	Tipo: ", type(Saldo_Real_Atualizado))
	try:
		if Saldo_Real_Atualizado > Saldo_Real:
			resultado_aposta = "Ganho"
			Placar_Ganhos += 1

		elif Saldo_Real_Atualizado <= Saldo_Real:
			resultado_aposta = "Perda"
			Placar_Perdas += 1			

	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		erro = str(e) + " 	|| LINHA: " + str(exc_tb.tb_lineno)
		Imprimir_Erro.Printar(str(erro), str('Operacoes.py'), str('Resultado_Operacao'))
		pass


	lucro_atual = Saldo_Real_Atualizado - Saldo_Inicial
	precisao_sistema = round((divisoes(Placar_Ganhos,(Placar_Ganhos + Placar_Perdas)))*100, 2)

	placar = "GANHOS " + str(Placar_Ganhos) + " x " + str(Placar_Perdas) + " PERDAS"

	caminho = Variaveis_Principais.Variaveis()
	caminho = caminho['Caminho']
	print('$'*500, '\n'*40)
	print("\n===========================================================================================")
	print("                                   RELATÓRIO DE OPERAÇÃO                                   ")
	print("-------------------------------------------------------------------------------------------")
	date = datetime.now()
	data_operacao = str(date.today().day) + "/" + str(date.today().month) + "/" +  str(date.today().year)
	horario_operacao = datetime.now().time()
	print("                    DATA: ", data_operacao,"             HORA:", horario_operacao)
	print("===========================================================================================")
	print("===========================================================================================")
	print("-------------------------------------------------------------------------------------------")
	print("                                     RESULTADO: ", resultado_aposta.upper() )
	print("                                   LUCRO ATUAL: USD", round(lucro_atual, 2) )                
	print("                                   SALDO ATUAL: USD", Saldo_Real_Atualizado)
	print("-------------------------------------------------------------------------------------------")
	print("                                   GANHOS", Placar_Ganhos , "X", Placar_Perdas, "PERDAS")
	print("                               PRECISÃO DO SISTEMA:", precisao_sistema,  "%" )
	print("===========================================================================================\n\n")
	print('$'*500, '\n'*40)

	#arquivo = open(caminho +'/Relatório de Operações.csv', 'a+')
	#string_relatorio = str(data_operacao) + ";" + str(horario_operacao) + ";" + str(Direcao).upper() + ";" + str(Valor_Aposta).replace(".", ",")  + ";" + str(resultado_aposta).upper() + ";" + str(placar) + ";" + str(precisao_sistema) + ";"  + str(lucro_atual).replace(".", ",") + ";"  + str(Saldo_Real).replace(".", ",") + "\n" 

	if resultado_aposta == 'Perda':
		Valor_Aposta = Valor_Aposta * 2
	else:
		Valor_Aposta = Valor_Inicial

	return Valor_Aposta, resultado_aposta, lucro_atual, Saldo_Real_Atualizado, precisao_sistema

