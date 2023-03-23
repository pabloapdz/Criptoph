#import Requisicoes
import os
from datetime import datetime, timedelta
import websocket
import json

hoje = datetime.now()
dia_atual = hoje.date()
horario_atual = hoje.time()
horario_atual = str(horario_atual)

horario_atual = horario_atual.replace(":", '.')
horario_atual = horario_atual[0:8]






print("pegou o nome do arquivo")
nome_arquivo = "Relatorio de Operacoes - " +  str(dia_atual) + " " + str(horario_atual)

if not os.path.exists('Relatorios/' +nome_arquivo):
	os.makedirs('Relatorios/' +nome_arquivo)
	caminho = 'Relatorios/' +nome_arquivo

	# Cabeçalho de Relatório de Operações
	cabecalho_relatorio = "DATA_INICIO;HORARIO_INICIO;DATA_REALIZACAO;HORA_REALIZACAO;DIA_SEMANA_REALZIACAO;VARIACAO;MENOR_1;MENOR_2;MENOR_3;QNTD_APOSTA_CIMA;QNTD_APOSTA_BAIXO;DIRECAO_APOSTA;VALOR_APOSTADO;RESULTADO;LUCRO_ATUAL;SALDO_ATUAL;ASSERTIVIDADE; \n"

	arquivo = open('Relatorios/' +nome_arquivo +'/Relatorio de Operacoes.csv', 'w+')
	with arquivo:
		arquivo.write(cabecalho_relatorio)
		arquivo.close()

	print("escreveu o cabeçalho")




def Variaveis():
	global caminho, nome_arquivo

	Estrategias = {

	#-----------------------------------------------   VALOR DA APOSTA   -----------------------------------------------#
	'valor_da_aposta_inicial': 0.50,
	'Conta_Real': False,

	#---------------------------------------------- CONFIGURAÇÕES DA APOSTA --------------------------------------------#
	'Mercado': "frxAUDJPY",	#frxAUDJPY ou R_10
	'duracao_da_aposta': 15, #em minutos 


	#---------------------------------------------- CONFIGURAÇÕES DAS VELAS --------------------------------------------#
	'margem_erro':	0.20,	#em % (decimais)	<-	40302010
	'porcentagem_pavio_futuro': 0.03,	#em % (decimais)
	'margem_de_erro_15_minutos': 0.20,	#em % (decimais) <- 
	'margem_de_erro_5_minutos': 0.50,	#em % (decimais) <-
	'margem_de_erro_1_minuto': 0.50, 	#em % (decimais) <-

	#'margem_de_erro_15_minutos': 0.33,	#em % (decimais) <- 
	#'margem_de_erro_5_minutos': 0.19,	#em % (decimais) <-
	#'margem_de_erro_1_minuto': 0.7, 	#em % (decimais) <-


	#----------------------------------------------- PARTE MAIS TÉCNICAS -----------------------------------------------#
	'minimo_de_variacoes': { #Minimo de variacoes possiveis para delta(tamanho_candle, var_pavio_sup e var_pavio_inf)
		"<1": 0,	#quantas vao ser menor que 1 			#antes do dia 15/09/2021 às 21:22 estava 2
		"<2": 1,	#quantas vao ser menor que 2
		"<3": 3,	#quantas vao ser menor que 3
		}
	}
	valor_da_aposta_inicial = Estrategias['valor_da_aposta_inicial']

	Todas_Variaveis = {
	'valor_da_aposta': valor_da_aposta_inicial,
	'Velas_Encontradas': [],
	'Aposta_Acima': 0,
	'Aposta_Abaixo': 0,
	'lucro_atual': 0,
	'Placar_Ganhos': 0,
	'Placar_Perdas': 0,
	'tempo_restante': 1,
	'Entrou': False,
	'Inverter_aposta': False,
	'nome_arquivo': nome_arquivo,
	}

	Todas_Variaveis['minimo_de_variacoes'] = Estrategias['minimo_de_variacoes']

	if Estrategias['Conta_Real'] == False:
		Todas_Variaveis['token'] = {"authorize": "j9lR6oKham5YBnI"}
		Todas_Variaveis['API_URL'] = "wss://ws.binaryws.com/websockets/v3?app_id=23758"
	else:
		Todas_Variaveis['token'] = {"authorize": "cXXtGD001HVCaAY"}
		Todas_Variaveis['API_URL'] = "wss://ws.binaryws.com/websockets/v3?app_id=23829"

	Todas_Variaveis['Caminho'] = caminho

	ws_Balance = websocket.create_connection(Todas_Variaveis['API_URL'], max_queue=1)
	ws_Balance.send(json.dumps(Todas_Variaveis['token']))
	Entrando = json.loads(ws_Balance.recv()) 
	ws_Balance.send(json.dumps({"balance": 1, "subscribe": 0}))
	Saldo = json.loads(ws_Balance.recv()) 
	print(Saldo)
	try:
		Saldo = float(Saldo['balance']['balance'])
		Todas_Variaveis['Saldo'] = Saldo
	except Exception as e:
		ws_Balance.send(json.dumps(TOKEN))
		Saldo = json.loads(ws_Balance.recv()) 
		Saldo = float(Saldo['balance']['balance'])
		Todas_Variaveis['Saldo'] = Saldo
	

	return Todas_Variaveis

