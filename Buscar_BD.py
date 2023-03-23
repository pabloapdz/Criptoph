import sys, os
from datetime import datetime, timedelta
import pymysql
import Requisicoes
import pausar
import estrategia
import Iniciar_BD
import time
import math
import Imprimir_Erro


def filtrar_velas_por_proporcao(velas, proporcao, vela_atual):
    velas_filtradas = []
    for vela in velas:
        if (
            vela["open"] * (1 - proporcao) <= vela_atual["open"] <= vela["open"] * (1 + proporcao)
            and vela["close"] * (1 - proporcao) <= vela_atual["close"] <= vela["close"] * (1 + proporcao)
            and vela["high"] * (1 - proporcao) <= vela_atual["high"] <= vela["high"] * (1 + proporcao)
            and vela["low"] * (1 - proporcao) <= vela_atual["low"] <= vela["low"] * (1 + proporcao)
        ):
            velas_filtradas.append(vela)
    return velas_filtradas

    
def Candle_Temporaria ():
	tempo = datetime.now()
	#print(tempo, 'INICIO: Candle_Temporaria')
	req_candle_temporaria_1_hora = {}
	Continuar = pausar.Verificar_Necessidade_Pausa()
	Variaveis = estrategia.Variaveis()
	Mercado = Variaveis['Mercado']
	Mercado = str(Mercado)
	#print('1- ',Mercado, ' Continuar:', Continuar)
	if Continuar == True:
		try:
			req_candle_temporaria_1_hora = {
				"ticks_history": Mercado,
				"count": 1,
			 	"end": "latest",
				"granularity": 3600,
				"style": "candles"
			}

			#print(Mercado)
			resultado_candle_temporaria_1_hora = Requisicoes.Buscar_Candle(req_candle_temporaria_1_hora)

			try:
				close_temporario_1_hora = (resultado_candle_temporaria_1_hora['candles'][0]['close'])
			except:
				resultado_candle_temporaria_1_hora = Requisicoes.Buscar_Candle(req_candle_temporaria_1_hora)

			close_temporario_1_hora = (resultado_candle_temporaria_1_hora['candles'][0]['close'])
			epoch_temporario_1_hora = (resultado_candle_temporaria_1_hora['candles'][0]['epoch'])
			high_1hora_atual = (resultado_candle_temporaria_1_hora['candles'][0]['high'])
			low_temporario_1_hora = (resultado_candle_temporaria_1_hora['candles'][0]['low'])
			open_temporario_1_hora = (resultado_candle_temporaria_1_hora['candles'][0]['open'])

			tam_candle_temporaria_1_hora = (math.sqrt((resultado_candle_temporaria_1_hora['candles'][0]['open'] - resultado_candle_temporaria_1_hora['candles'][0]['close'])**2))
			if resultado_candle_temporaria_1_hora['candles'][0]['open'] < resultado_candle_temporaria_1_hora['candles'][0]['close']: ##Green resultado_candle_temporaria_1_hora
				pavio_superior_temporario_1_hora = (math.sqrt((resultado_candle_temporaria_1_hora['candles'][0]['high'] - resultado_candle_temporaria_1_hora['candles'][0]['close'])**2))
				pavio_inferior_temporario_1_hora = (math.sqrt((resultado_candle_temporaria_1_hora['candles'][0]['open'] - resultado_candle_temporaria_1_hora['candles'][0]['low'])**2))
			else: ##Red resultado_candle_temporaria_1_hora
				pavio_superior_temporario_1_hora = (math.sqrt((resultado_candle_temporaria_1_hora['candles'][0]['high'] - resultado_candle_temporaria_1_hora['candles'][0]['open'])**2))
				pavio_inferior_temporario_1_hora = (math.sqrt((resultado_candle_temporaria_1_hora['candles'][0]['close'] - resultado_candle_temporaria_1_hora['candles'][0]['low'])**2))

			time.sleep(2)

			req_candle_temporaria_15_minutos = {
				"ticks_history": Mercado,
				#"count": 8760,
				"count": 1,
			 	"end": "latest",
				"granularity": 900,
				"style": "candles"
			}

			resultado_candle_temporaria_15_minutos = Requisicoes.Buscar_Candle(req_candle_temporaria_15_minutos)

			try:
				close_temporario_15_minutos = (resultado_candle_temporaria_15_minutos['candles'][0]['close'])
			except:
				resultado_candle_temporaria_15_minutos = Requisicoes.Buscar_Candle(req_candle_temporaria_15_minutos)

			close_temporario_15_minutos = (resultado_candle_temporaria_15_minutos['candles'][0]['close'])
			epoch_temporario_15_minutos = (resultado_candle_temporaria_15_minutos['candles'][0]['epoch'])
			high_temporario_15_minutos = (resultado_candle_temporaria_15_minutos['candles'][0]['high'])
			low_temporario_15_minutos = (resultado_candle_temporaria_15_minutos['candles'][0]['low'])
			open_temporario_15_minutos = (resultado_candle_temporaria_15_minutos['candles'][0]['open'])

			tam_candle_temporaria_15_minutos = (math.sqrt((resultado_candle_temporaria_15_minutos['candles'][0]['open'] - resultado_candle_temporaria_15_minutos['candles'][0]['close'])**2))
			if resultado_candle_temporaria_15_minutos['candles'][0]['open'] < resultado_candle_temporaria_15_minutos['candles'][0]['close']: ##Green resultado_candle_temporaria_15_minutos
				pavio_superior_temporario_15_minutos = (math.sqrt((resultado_candle_temporaria_15_minutos['candles'][0]['high'] - resultado_candle_temporaria_15_minutos['candles'][0]['close'])**2))
				pavio_inferior_temporario_15_minutos = (math.sqrt((resultado_candle_temporaria_15_minutos['candles'][0]['open'] - resultado_candle_temporaria_15_minutos['candles'][0]['low'])**2))
			else: ##Red resultado_candle_temporaria_15_minutos
				pavio_superior_temporario_15_minutos = (math.sqrt((resultado_candle_temporaria_15_minutos['candles'][0]['high'] - resultado_candle_temporaria_15_minutos['candles'][0]['open'])**2))
				pavio_inferior_temporario_15_minutos = (math.sqrt((resultado_candle_temporaria_15_minutos['candles'][0]['close'] - resultado_candle_temporaria_15_minutos['candles'][0]['low'])**2))


			time.sleep(2)

			req_candle_temporaria_5_minutos = {
				"ticks_history": Mercado,
				#"count": 8760,
				"count": 1,
			 	"end": "latest",
				"granularity": 300,
				"style": "candles"
			}

			resultado_candle_temporaria_5_minutos = Requisicoes.Buscar_Candle(req_candle_temporaria_5_minutos)

			try:
				close_temporario_5_minutos = (resultado_candle_temporaria_5_minutos['candles'][0]['close'])
			except:
				resultado_candle_temporaria_5_minutos = Requisicoes.Buscar_Candle(req_candle_temporaria_5_minutos)

			close_temporario_5_minutos = (resultado_candle_temporaria_5_minutos['candles'][0]['close'])
			epoch_temporario_5_minutos = (resultado_candle_temporaria_5_minutos['candles'][0]['epoch'])
			high_temporario_5_minutos = (resultado_candle_temporaria_5_minutos['candles'][0]['high'])
			low_temporario_5_minutos = (resultado_candle_temporaria_5_minutos['candles'][0]['low'])
			open_temporario_5_minutos = (resultado_candle_temporaria_5_minutos['candles'][0]['open'])

			tam_candle_temporaria_5_minutos = (math.sqrt((resultado_candle_temporaria_5_minutos['candles'][0]['open'] - resultado_candle_temporaria_5_minutos['candles'][0]['close'])**2))
			if resultado_candle_temporaria_5_minutos['candles'][0]['open'] < resultado_candle_temporaria_5_minutos['candles'][0]['close']: ##Green resultado_candle_temporaria_5_minutos
				pavio_superior_temporario_5_minutos = (math.sqrt((resultado_candle_temporaria_5_minutos['candles'][0]['high'] - resultado_candle_temporaria_5_minutos['candles'][0]['close'])**2))
				pavio_inferior_temporario_5_minutos = (math.sqrt((resultado_candle_temporaria_5_minutos['candles'][0]['open'] - resultado_candle_temporaria_5_minutos['candles'][0]['low'])**2))
			else: ##Red resultado_candle_temporaria_5_minutos
				pavio_superior_temporario_5_minutos = (math.sqrt((resultado_candle_temporaria_5_minutos['candles'][0]['high'] - resultado_candle_temporaria_5_minutos['candles'][0]['open'])**2))
				pavio_inferior_temporario_5_minutos = (math.sqrt((resultado_candle_temporaria_5_minutos['candles'][0]['close'] - resultado_candle_temporaria_5_minutos['candles'][0]['low'])**2))


			time.sleep(2)

			req_candle_temporaria_1_minuto = {
				"ticks_history": Mercado,
				#"count": 8760,
				"count": 1,
			 	"end": "latest",
				"granularity": 60,
				"style": "candles"
			}

			resultado_candle_temporaria_1_minuto = Requisicoes.Buscar_Candle(req_candle_temporaria_1_minuto)

			try:
				close_temporario_1_minuto = (resultado_candle_temporaria_1_minuto['candles'][0]['close'])
			except:
				resultado_candle_temporaria_1_minuto = Requisicoes.Buscar_Candle(req_candle_temporaria_1_minuto)


			close_temporario_1_minuto = (resultado_candle_temporaria_1_minuto['candles'][0]['close'])
			epoch_temporario_5_minutos = (resultado_candle_temporaria_1_minuto['candles'][0]['epoch'])
			high_temporario_1_minuto = (resultado_candle_temporaria_1_minuto['candles'][0]['high'])
			low_temporario_1_minuto = (resultado_candle_temporaria_1_minuto['candles'][0]['low'])
			open_temporario_1_minuto = (resultado_candle_temporaria_1_minuto['candles'][0]['open'])

			tam_candle_temporaria_1_minuto = (math.sqrt((resultado_candle_temporaria_1_minuto['candles'][0]['open'] - resultado_candle_temporaria_1_minuto['candles'][0]['close'])**2))


			if resultado_candle_temporaria_1_minuto['candles'][0]['open'] < resultado_candle_temporaria_1_minuto['candles'][0]['close']: ##Green 
				pavio_superior_temporario_5_minutos = (math.sqrt((resultado_candle_temporaria_1_minuto['candles'][0]['high'] - resultado_candle_temporaria_1_minuto['candles'][0]['close'])**2))
				pavio_inferior_temporario_5_minutos = (math.sqrt((resultado_candle_temporaria_1_minuto['candles'][0]['open'] - resultado_candle_temporaria_1_minuto['candles'][0]['low'])**2))
			else: ##Red 
				pavio_superior_temporario_5_minutos = (math.sqrt((resultado_candle_temporaria_1_minuto['candles'][0]['high'] - resultado_candle_temporaria_1_minuto['candles'][0]['open'])**2))
				pavio_inferior_temporario_5_minutos = (math.sqrt((resultado_candle_temporaria_1_minuto['candles'][0]['close'] - resultado_candle_temporaria_1_minuto['candles'][0]['low'])**2))





			tempo = datetime.now()
			#print(tempo, 'FIM: Candle_Temporaria')


			return tam_candle_temporaria_5_minutos, pavio_superior_temporario_5_minutos, pavio_inferior_temporario_5_minutos, tam_candle_temporaria_15_minutos, pavio_superior_temporario_15_minutos, pavio_inferior_temporario_15_minutos, tam_candle_temporaria_1_hora, pavio_superior_temporario_1_hora, pavio_inferior_temporario_1_hora,close_temporario_1_hora,high_1hora_atual,low_temporario_1_hora,open_temporario_1_hora,close_temporario_15_minutos,high_temporario_15_minutos,low_temporario_15_minutos,open_temporario_15_minutos,close_temporario_5_minutos,high_temporario_5_minutos,low_temporario_5_minutos,open_temporario_5_minutos, close_temporario_1_minuto,high_temporario_1_minuto,low_temporario_1_minuto,open_temporario_1_minuto
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			#print("erro aqui, linha 107 buscar bd")
			try:
				if resultado_candle_temporaria_1_hora: print(resultado_candle_temporaria_1_hora)
				if resultado_candle_temporaria_15_minutos: print(resultado_candle_temporaria_15_minutos)
				if resultado_candle_temporaria_5_minutos: print(resultado_candle_temporaria_5_minutos)
				if resultado_candle_temporaria_1_minuto: print(resultado_candle_temporaria_1_minuto)
			except:
				pass


			erro = str(e) + " 	|| LINHA: " + str(exc_tb.tb_lineno)
			Imprimir_Erro.Printar(str(erro), str('Buscar_BD.py'), str('Candle_Temporaria'))



def divisoes(n, d):
	return n / d if d else 0

def Comparar_BD():
	##print("indo comparar bd")
	Velas_Encontradas = []
	Verificacao = {}
	Aposta_Acima = 0
	Aposta_Abaixo = 0
	Variaveis = estrategia.Variaveis()
	executor_bd = Iniciar_BD.Bando_de_Dados()

	Velas_Encontradas = []
	Verificacao = {}
	Aposta_Acima = 0
	Aposta_Abaixo = 0

	try:
		#print("verificando se pode continuar")
		Continuar = pausar.Verificar_Necessidade_Pausa()

		if Continuar == True:
			#print("vai continuar")
			Saldo_Real = Requisicoes.Saldo()
			#print("Saldo_Real:	", Saldo_Real)

			data_hora_inicio_analise = datetime.now()

			print("Atualizado:	", str(data_hora_inicio_analise))

			tam_candle_temporaria_5_minutos, pavio_superior_temporario_5_minutos, pavio_inferior_temporario_5_minutos, tam_candle_temporaria_15_minutos, pavio_superior_temporario_15_minutos, pavio_inferior_temporario_15_minutos, tam_candle_temporaria_1_hora, pavio_superior_temporario_1_hora, pavio_inferior_temporario_1_hora, close_temporario_1_hora,high_1hora_atual,low_temporario_1_hora,open_temporario_1_hora,close_temporario_15_minutos,high_temporario_15_minutos,low_temporario_15_minutos,open_temporario_15_minutos,close_temporario_5_minutos,high_temporario_5_minutos,low_temporario_5_minutos,open_temporario_5_minutos, close_temporario_1_minuto,high_temporario_1_minuto,low_temporario_1_minuto,open_temporario_1_minuto = Candle_Temporaria()
			#print('\n\n')
			#print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||	HORARIO QUE PEGOU A VELA DE 5 MINUTOS, 15 MINUTOS E 1 HORA:	", data_hora_inicio_analise)
			#print('\n\n')


			margem_erro_1h = Variaveis['margem_erro']

			margem_erro_15min = Variaveis['margem_de_erro_15_minutos']

			margem_erro_5min = Variaveis['margem_de_erro_5_minutos']

			margem_erro_1min = Variaveis['margem_de_erro_1_minuto']

			valor_da_aposta_inicial = Variaveis['valor_da_aposta_inicial']

			porcentagem_pavio_futuro = Variaveis['porcentagem_pavio_futuro']

			#minimo_de_apostas = Variaveis['Minimo_Apostas']


			###################################################### 1 hora

			tam_candle_atual = tam_candle_temporaria_1_hora
			pavio_superior_atual = pavio_superior_temporario_1_hora
			pavio_inferior_atual = pavio_inferior_temporario_1_hora
			prop_sup_atual = divisoes(tam_candle_atual, pavio_superior_atual)
			prop_inf_atual =  divisoes(tam_candle_atual, pavio_inferior_atual)
			prop_geral_atual = prop_sup_atual + prop_inf_atual

			
			open_atual_1h = open_temporario_1_hora
			high_1h_atual = high_1hora_atual
			low_atual_1h = low_temporario_1_hora
			close_atual_1h = close_temporario_1_hora

			'''
			query_geral = executor_bd.execute("SELECT * FROM `1hora` WHERE `High` >= "+ str(high_1h_atual -  high_1h_atual*margem_erro_1h) +" AND `High` <= " + str(high_1h_atual + high_1h_atual*margem_erro_1h)  +" AND `Low` >= " + str(low_atual_1h - low_atual_1h*margem_erro_1h)  +" AND `Low` <= " + str(low_atual_1h + low_atual_1h*margem_erro_1h)+" AND `Close` >= " + str(close_atual_1h - close_atual_1h*margem_erro_1h)  +" AND `Close` <= " + str(close_atual_1h + close_atual_1h*margem_erro_1h)+" AND `Open` >= " + str(open_atual_1h - open_atual_1h*margem_erro_1h)  +" AND `Open` <= " + str(open_atual_1h + open_atual_1h*margem_erro_1h))
			'''

			###################################################### 15 minutos
			
			open_atual_15min = open_temporario_15_minutos
			high_15min_atual = high_temporario_15_minutos
			low_atual_15min = low_temporario_15_minutos
			close_atual_15min = close_temporario_15_minutos
			'''
			query_geral = executor_bd.execute("SELECT * FROM `15_minutos` WHERE `High` >= "+ str(high_15min_atual -  high_15min_atual*margem_erro_15min) +" AND `High` <= " + str(high_15min_atual + high_15min_atual*margem_erro_15min)  +" AND `Low` >= " + str(low_atual_15min - low_atual_15min*margem_erro_15min)  +" AND `Low` <= " + str(low_atual_15min + low_atual_15min*margem_erro_15min)+" AND `Close` >= " + str(close_atual_15min - close_atual_15min*margem_erro_15min)  +" AND `Close` <= " + str(close_atual_15min + close_atual_15min*margem_erro_15min)+" AND `Open` >= " + str(open_atual_15min - open_atual_15min*margem_erro_15min)  +" AND `Open` <= " + str(open_atual_15min + open_atual_15min*margem_erro_15min))
			'''
			###################################################### 5 minutos

			open_atual_5min = open_temporario_5_minutos
			high_5min_atual = high_temporario_5_minutos
			low_atual_5min = low_temporario_5_minutos
			close_atual_5min = close_temporario_5_minutos
			'''
			query_geral = executor_bd.execute("SELECT * FROM `5_minutos` WHERE `High` >= "+ str(high_5min_atual -  high_5min_atual*margem_erro_5min) +" AND `High` <= " + str(high_5min_atual + high_5min_atual*margem_erro_5min)  +" AND `Low` >= " + str(low_atual_5min - low_atual_5min*margem_erro_5min)  +" AND `Low` <= " + str(low_atual_5min + low_atual_5min*margem_erro_5min)+" AND `Close` >= " + str(close_atual_5min - close_atual_5min*margem_erro_5min)  +" AND `Close` <= " + str(close_atual_5min + close_atual_5min*margem_erro_5min)+" AND `Open` >= " + str(open_atual_5min - open_atual_5min*margem_erro_5min)  +" AND `Open` <= " + str(open_atual_5min + open_atual_5min*margem_erro_5min))
			'''
			###################################################### 1 minuto
			open_atual_1min = open_temporario_1_minuto
			high_1min_atual = high_temporario_1_minuto
			low_atual_1min = low_temporario_1_minuto
			close_atual_1min = close_temporario_1_minuto



			## Localizando os candles que batem com a pesquisa

			tempo = datetime.now()
			#print("Vai procurar velas de 1 hora", tempo)

			executor_bd = Iniciar_BD.Bando_de_Dados()
			while True:
				try:
					query_geral = executor_bd.execute("SELECT * FROM `1hora` WHERE `prop_geral` BETWEEN "+ str((prop_geral_atual*(1 - margem_erro_1h))) + "AND "+ str((prop_geral_atual*(1 + margem_erro_1h))) + " AND( `prop_sup` BETWEEN "+ str((prop_sup_atual*(1 - margem_erro_1h))) +" AND "+ str((prop_sup_atual*(1 + margem_erro_1h))) +" AND( `prop_inf` BETWEEN "+ str((prop_inf_atual*(1 - margem_erro_1h))) +" AND "+ str((prop_inf_atual*(1 + margem_erro_1h))) +" ) )")
					break
				except Exception as e:
					executor_bd = Iniciar_BD.Bando_de_Dados()
					time.sleep(5)
					#print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n																				RECONECTANDO AO BANCO DE DADOS\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
					continue

			tempo = datetime.now()
			#print("Finalizou a busca das velas de 1hora", tempo)
			#print("pegou a query geral")

			Quantidade_Resultados = int(query_geral)
			if Quantidade_Resultados == 0:
				#print("nao foi viavel")
				return {'Viavel': False}, 0, 0, 0
			else:
				print("Quantidade de velas encontradas de 1 hora:	", Quantidade_Resultados)
				pass
				

			query_geral = executor_bd.fetchall()

			'''

			## Localizando os candles que batem com a pesquisa

			tempo = datetime.now()
			#print("Vai procurar velas de 1 hora", tempo)

			executor_bd = Iniciar_BD.Bando_de_Dados()
			while True:
				try:
					query_geral = executor_bd.execute("SELECT * FROM `1hora` WHERE `High` >= "+ str(high_1h_atual -  high_1h_atual*margem_erro_1h) +" AND `High` <= " + str(high_1h_atual + high_1h_atual*margem_erro_1h)  +" AND `Low` >= " + str(low_atual_1h - low_atual_1h*margem_erro_1h)  +" AND `Low` <= " + str(low_atual_1h + low_atual_1h*margem_erro_1h)+" AND `Close` >= " + str(close_atual_1h - close_atual_1h*margem_erro_1h)  +" AND `Close` <= " + str(close_atual_1h + close_atual_1h*margem_erro_1h)+" AND `Open` >= " + str(open_atual_1h - open_atual_1h*margem_erro_1h)  +" AND `Open` <= " + str(open_atual_1h + open_atual_1h*margem_erro_1h))
					break
				except Exception as e:
					executor_bd = Iniciar_BD.Bando_de_Dados()
					time.sleep(5)
					#print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n																				RECONECTANDO AO BANCO DE DADOS\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
					continue

			tempo = datetime.now()
			##print("Finalizou a busca das velas de 1hora", tempo)
			##print("pegou a query geral")

			Quantidade_Resultados = int(query_geral)
			if Quantidade_Resultados == 0:
				#print("nao foi viavel")
				return {'Viavel': False}, 0, 0, 0
			else:
				#print("Quantidade de velas encontradas de 1 hora:	", Quantidade_Resultados)
				#pass
				
			query_geral = executor_bd.fetchall()
			'''

			##print("\nQuantidade_Resultados:", Quantidade_Resultados)
			#print("Vai procurar velas de 15 min", tempo)
			for i in range(Quantidade_Resultados):
				##print("valor1:	", end='	')
				##print(i)
				data_candle_1hora = query_geral[i][0]
				##print("valor2:	query_geral =	", query_geral, '		data_candle_1hora:	', data_candle_1hora)
				horario_candle_1hora = query_geral[i][1]
				##print("valor3:	",	horario_candle_1hora)

				################################################ 15 MINUTOS ################################################

				pavio_superior_15min = pavio_superior_temporario_15_minutos
				pavio_inferior_15min = pavio_inferior_temporario_15_minutos

				horario_candle_15min = datetime.strptime(horario_candle_1hora, "%H:%M:%S")
				horario_candle_15min = horario_candle_15min + timedelta(minutes=45)
				horario_candle_15min = str(horario_candle_15min)[11:]
				horario_candle_15min = datetime.strptime(horario_candle_15min, "%H:%M:%S").time()
				tempo = datetime.now()


				tam_candle_15min = tam_candle_temporaria_15_minutos
				prop_sup_15min = divisoes(tam_candle_15min, pavio_superior_15min)
				prop_inf_15min =  divisoes(tam_candle_15min, pavio_inferior_15min)
				prop_geral_15min = prop_sup_15min + prop_inf_15min



				## Localizando os candles que batem com a pesquisa
				query = executor_bd.execute("SELECT * FROM `15_minutos` WHERE `Date` = "+ str(data_candle_1hora) + " AND `Timestamp` = '" + str(horario_candle_15min) + "' AND `prop_geral` BETWEEN "+ str((prop_geral_15min*(1 - margem_erro_15min))) + "AND "+ str((prop_geral_15min*(1 + margem_erro_15min))) + " AND `prop_sup` BETWEEN "+ str((prop_sup_15min*(1 - margem_erro_15min))) +" AND "+ str((prop_sup_15min*(1 + margem_erro_15min))) +" AND `prop_inf` BETWEEN "+ str((prop_inf_15min*(1 - margem_erro_15min))) +" AND "+ str((prop_inf_15min*(1 + margem_erro_15min))) +" ")
				Quantidade_Resultados_15_minutos = query


		
				## Localizando os candles que batem com a pesquisa
				##print("data_candle_1hora: ", data_candle_1hora)
				##print("query de 15 minutos: ", "SELECT * FROM `15_minutos` WHERE `Date` = "+ str(data_candle_1hora) + " AND `Timestamp` = " + str(horario_candle_15min) +" AND `High` >= "+ str(high_15min_atual -  high_15min_atual*margem_erro_15min) +" AND `High` <= " + str(high_15min_atual + high_15min_atual*margem_erro_15min)  +" AND `Low` >= " + str(low_atual_15min - low_atual_15min*margem_erro_15min)  +" AND `Low` <= " + str(low_atual_15min + low_atual_15min*margem_erro_15min)+" AND `Close` >= " + str(close_atual_15min - close_atual_15min*margem_erro_15min)  +" AND `Close` <= " + str(close_atual_15min + close_atual_15min*margem_erro_15min)+" AND `Open` >= " + str(open_atual_15min - open_atual_15min*margem_erro_15min)  +" AND `Open` <= " + str(open_atual_15min + open_atual_15min*margem_erro_15min))
				

				#query = executor_bd.execute("SELECT * FROM `15_minutos` WHERE `Date` = "+ str(data_candle_1hora) + " AND `Timestamp` = '" + str(horario_candle_15min) +"' AND `High` >= "+ str(high_15min_atual -  high_15min_atual*margem_erro_15min) +" AND `High` <= " + str(high_15min_atual + high_15min_atual*margem_erro_15min)  +" AND `Low` >= " + str(low_atual_15min - low_atual_15min*margem_erro_15min)  +" AND `Low` <= " + str(low_atual_15min + low_atual_15min*margem_erro_15min)+" AND `Close` >= " + str(close_atual_15min - close_atual_15min*margem_erro_15min)  +" AND `Close` <= " + str(close_atual_15min + close_atual_15min*margem_erro_15min)+" AND `Open` >= " + str(open_atual_15min - open_atual_15min*margem_erro_15min)  +" AND `Open` <= " + str(open_atual_15min + open_atual_15min*margem_erro_15min))

				#Quantidade_Resultados_15_minutos = int(query)
				##print("Quantidade_Resultados_15_minutos:", Quantidade_Resultados_15_minutos)

				##print("|1h: ", i, "	/	", Quantidade_Resultados, end='	')
				tempo = datetime.now()
				
				if Quantidade_Resultados_15_minutos == 0:
					if i == Quantidade_Resultados:
						return {'Viavel': False}, 0, 0, 0
					else:
						continue
				else:
					##print('achou alguma')
					pass
					##print("15 	"*7)
					##print("15 	"*13)
					##print("15 	"*24)
					print("					Quantidade de velas encontradas de 15 minutos:	", Quantidade_Resultados_15_minutos)
					print("Finalizou a busca das velas de 15 min", tempo)
					##print("15 	"*24)
					##print("15 	"*13)
					##print("15 	"*7)
				query = executor_bd.fetchall()

				################################################ 5 MINUTOS ################################################
				#print("começando a de 5 minutos")
				horario_candle_5min = query_geral[i][1]
				horario_candle_5min = datetime.strptime(horario_candle_5min, "%H:%M:%S")
				horario_candle_5min = horario_candle_5min + timedelta(minutes=55)
				horario_candle_5min = str(horario_candle_5min)[11:]
				horario_candle_5min = datetime.strptime(horario_candle_5min, "%H:%M:%S").time()

				pavio_superior_5min = pavio_superior_temporario_5_minutos
				pavio_inferior_5min = pavio_inferior_temporario_5_minutos



				tam_candle_5min = tam_candle_temporaria_5_minutos
				prop_sup_5min = divisoes(tam_candle_5min, pavio_superior_5min)
				prop_inf_5min =  divisoes(tam_candle_5min, pavio_inferior_5min)
				prop_geral_5min = prop_sup_5min + prop_inf_5min



				tempo = datetime.now()
				#print("Vai procurar velas de 5 min", tempo)

				## Localizando os candles que batem com a pesquisa
				query = executor_bd.execute("SELECT * FROM `5_minutos` WHERE `Date` = "+ str(data_candle_1hora) + " AND `Timestamp` = '" + str(horario_candle_5min) + "' AND `prop_geral` BETWEEN "+ str((prop_geral_5min*(1 - margem_erro_5min))) + "AND "+ str((prop_geral_5min*(1 + margem_erro_5min))) + " AND( `prop_sup` BETWEEN "+ str((prop_sup_5min*(1 - margem_erro_5min))) +" AND "+ str((prop_sup_5min*(1 + margem_erro_5min))) +" AND( `prop_inf` BETWEEN "+ str((prop_inf_5min*(1 - margem_erro_5min))) +" AND "+ str((prop_inf_5min*(1 + margem_erro_5min))) +" ) )")
				Quantidade_Resultados_5_minutos = query

				#query_geral = executor_bd.execute("SELECT * FROM `5_minutos` WHERE `Date` = "+ str(data_candle_1hora) + " AND `Timestamp` = '" + str(horario_candle_5min) +"' AND `High` >= "+ str(high_5min_atual -  high_5min_atual*margem_erro_5min) +" AND `High` <= " + str(high_5min_atual + high_5min_atual*margem_erro_5min)  +" AND `Low` >= " + str(low_atual_5min - low_atual_5min*margem_erro_5min)  +" AND `Low` <= " + str(low_atual_5min + low_atual_5min*margem_erro_5min)+" AND `Close` >= " + str(close_atual_5min - close_atual_5min*margem_erro_5min)  +" AND `Close` <= " + str(close_atual_5min + close_atual_5min*margem_erro_5min)+" AND `Open` >= " + str(open_atual_5min - open_atual_5min*margem_erro_5min)  +" AND `Open` <= " + str(open_atual_5min + open_atual_5min*margem_erro_5min))


				#Quantidade_Resultados_5_minutos = query
				print("Quantidade_Resultados_5_minutos:", Quantidade_Resultados_5_minutos)

				tempo = datetime.now()
				#print("Finalizou a busca das velas de 5 min", tempo)


				if Quantidade_Resultados_5_minutos == 0:
					if i == Quantidade_Resultados:
						return {'Viavel': False}, 0, 0, 0
					else:
						continue
				else:
					pass
					#print("5 	"*7)
					#print("5 	"*13)
					#print("5 	"*24)
					#print("							Quantidade de velas encontradas de 5 minutos:	", Quantidade_Resultados_5_minutos)
					#print("5 	"*24)
					#print("5 	"*13)
					#print("5 	"*7)
				query = executor_bd.fetchall()

				################################################ 	  1 MINUTO 	   ################################################
				horario_candle_1min = query_geral[i][1]
				horario_candle_1min = datetime.strptime(horario_candle_1min, "%H:%M:%S")
				horario_candle_1min = horario_candle_1min + timedelta(minutes=60)
				horario_candle_1min = str(horario_candle_1min)[11:]
				horario_candle_1min = datetime.strptime(horario_candle_1min, "%H:%M:%S").time()


				query = executor_bd.execute("SELECT * FROM `1minuto` WHERE `Date` = "+ str(data_candle_1hora) + " AND `Timestamp` = '" + str(horario_candle_1min)+"'")
				query = executor_bd.fetchall()

				##print("AQUI QUE TA DANDO ERRO "*90)
				#print(query)

				Open_1min_bd = query[0][2]
				High_1min_bd = query[0][3]
				Low_1min_bd = query[0][4]
				Close_1min_bd = query[0][5]

				if (High_1min_bd >= (high_1min_atual - high_1min_atual*margem_erro_1min)) and (High_1min_bd <= (high_1min_atual + high_1min_atual*margem_erro_1min)):

					if (Low_1min_bd >= (low_atual_1min - low_atual_1min*margem_erro_1min)) and (Low_1min_bd <= (low_atual_1min + low_atual_1min*margem_erro_1min)):

						if (Close_1min_bd >= (close_atual_1min - close_atual_1min*margem_erro_1min)) and (Close_1min_bd <= (close_atual_1min + close_atual_1min*margem_erro_1min)):

							if (Open_1min_bd >= (open_atual_1min - open_atual_1min*margem_erro_1min)) and (Open_1min_bd <= (open_atual_1min + open_atual_1min*margem_erro_1min)):

								#pass
								print("1 	"*7)
								print("1 	"*13)
								print("1 	"*24)
								print("		VIÁVEL		")
								print("1 	"*24)
								print("1 	"*13)
								print("1 	"*7)
							else:
								print("ULTIMO AQUI NÃO FOI VIÁVEL"*777)
								return {'Viavel': False}, 0, 0, 0
						else:
							print("PENULTIMO AQUI NÃO FOI VIÁVEL"*777)
							return {'Viavel': False}, 0, 0, 0
					else:
						print("SEGUNDO AQUI NÃO FOI VIÁVEL"*777)
						return {'Viavel': False}, 0, 0, 0
				else:
					#print("PRIMEIRO AQUI NÃO FOI VIÁVEL"*777)
					return {'Viavel': False}, 0, 0, 0


				################################################ FUTUROS 5 MINUTOS ################################################
				#	COLOQUEI TUDO COMENTADO PARA TESTAR UM NEGOCIO NO DIA 15/08/2022
				'''
				horario_candle_1min_passado_recente = str(query_geral[i][1])
				horario_candle_1min_passado_recente = datetime.strptime(horario_candle_1min_passado_recente, "%H:%M:%S")
				horario_candle_1min_passado_recente = horario_candle_1min_passado_recente + timedelta(minutes=55)
				horario_candle_1min_passado_recente = str(horario_candle_1min_passado_recente)[11:]
				horario_candle_1min_passado_recente = datetime.strptime(horario_candle_1min_passado_recente, "%H:%M:%S").time()

				query = executor_bd.execute("SELECT * FROM `1minuto` WHERE `Date` = "+ str(data_candle_1hora) + " AND `Timestamp` = '" + str(horario_candle_1min_passado_recente)+"'")
				query = executor_bd.fetchall()

				Open_1min_passado_recente = query[0][2]
				High_1min_passado_recente = query[0][3]
				Low_1min_passado_recente = query[0][4]
				Close_1min_passado_recente = query[0][5]

				horario_candle_2min_passado_recente = str(query_geral[i][1])
				horario_candle_2min_passado_recente = datetime.strptime(horario_candle_2min_passado_recente, "%H:%M:%S")
				horario_candle_2min_passado_recente = horario_candle_2min_passado_recente + timedelta(minutes=56)
				horario_candle_2min_passado_recente = str(horario_candle_2min_passado_recente)[11:]
				horario_candle_2min_passado_recente = datetime.strptime(horario_candle_2min_passado_recente, "%H:%M:%S").time()

				query = executor_bd.execute("SELECT * FROM `1minuto` WHERE `Date` = "+ str(data_candle_1hora) + " AND `Timestamp` = '" + str(horario_candle_2min_passado_recente)+"'")
				query = executor_bd.fetchall()

				Open_2min_passado_recente = query[0][2]
				High_2min_passado_recente = query[0][3]
				Low_2min_passado_recente = query[0][4]
				Close_2min_passado_recente = query[0][5]

				horario_candle_3min_passado_recente = str(query_geral[i][1])
				horario_candle_3min_passado_recente = datetime.strptime(horario_candle_3min_passado_recente, "%H:%M:%S")
				horario_candle_3min_passado_recente = horario_candle_3min_passado_recente + timedelta(minutes=57)
				horario_candle_3min_passado_recente = str(horario_candle_3min_passado_recente)[11:]
				horario_candle_3min_passado_recente = datetime.strptime(horario_candle_3min_passado_recente, "%H:%M:%S").time()


				query = executor_bd.execute("SELECT * FROM `1minuto` WHERE `Date` = "+ str(data_candle_1hora) + " AND `Timestamp` = '" + str(horario_candle_3min_passado_recente)+"'")
				query = executor_bd.fetchall()

				Open_3min_passado_recente = query[0][2]
				High_3min_passado_recente = query[0][3]
				Low_3min_passado_recente = query[0][4]
				Close_3min_passado_recente = query[0][5]


				horario_candle_4min_passado_recente = str(query_geral[i][1])
				horario_candle_4min_passado_recente = datetime.strptime(horario_candle_4min_passado_recente, "%H:%M:%S")
				horario_candle_4min_passado_recente = horario_candle_4min_passado_recente + timedelta(minutes=58) 
				horario_candle_4min_passado_recente = str(horario_candle_4min_passado_recente)[11:]
				horario_candle_4min_passado_recente = datetime.strptime(horario_candle_4min_passado_recente, "%H:%M:%S").time()

				query = executor_bd.execute("SELECT * FROM `1minuto` WHERE `Date` = "+ str(data_candle_1hora) + " AND `Timestamp` = '" + str(horario_candle_4min_passado_recente)+"'")
				query = executor_bd.fetchall()

				Open_4min_passado_recente = query[0][2]
				High_4min_passado_recente = query[0][3]
				Low_4min_passado_recente = query[0][4]
				Close_4min_passado_recente = query[0][5]


				horario_candle_5min_passado_recente = str(query_geral[i][1])
				horario_candle_5min_passado_recente = datetime.strptime(horario_candle_5min_passado_recente, "%H:%M:%S")
				horario_candle_5min_passado_recente = horario_candle_5min_passado_recente + timedelta(minutes=59)
				horario_candle_5min_passado_recente = str(horario_candle_5min_passado_recente)[11:]
				horario_candle_5min_passado_recente = datetime.strptime(horario_candle_5min_passado_recente, "%H:%M:%S").time()

				query = executor_bd.execute("SELECT * FROM `1minuto` WHERE `Date` = "+ str(data_candle_1hora) + " AND `Timestamp` = '" + str(horario_candle_5min_passado_recente)+"'")
				query = executor_bd.fetchall()

				Open_5min_passado_recente = query[0][2]
				High_5min_passado_recente = query[0][3]
				Low_5min_passado_recente = query[0][4]
				Close_5min_passado_recente = query[0][5]

				'''
				######################## DUAS VELAS POSTERIORES AO "MOMENTO DIVISOR" ########################
				
				#O HORARIO DA QUERY GERAL = O HORÁRIO DE 1 HORA ATRÁS
				horario_candle_1min_futuro = str(query_geral[i][1])
				horario_candle_1min_futuro = datetime.strptime(horario_candle_1min_futuro, "%H:%M:%S")
				horario_candle_1min_futuro = horario_candle_1min_futuro + timedelta(minutes=61)
				horario_candle_1min_futuro = str(horario_candle_1min_futuro)[11:]
				horario_candle_1min_futuro = datetime.strptime(horario_candle_1min_futuro, "%H:%M:%S").time()

				query = executor_bd.execute("SELECT * FROM `1minuto` WHERE `Date` = "+ str(data_candle_1hora) + " AND `Timestamp` = '" + str(horario_candle_1min_futuro)+"'")
				query = executor_bd.fetchall()

				Open_1min_futuro = query[0][2]
				High_1min_futuro = query[0][3]
				Low_1min_futuro = query[0][4]
				Close_1min_futuro = query[0][5]

				#Green candle
				if Close_1min_futuro > Open_1min_futuro:
					Aposta_Acima += 1
					Tamanho_candle_1min_futuro = Close_1min_futuro - Open_1min_futuro
					Pavio_superior_1min_futuro = High_1min_futuro - Close_1min_futuro
					Pavio_inferior_1min_futuro = Open_1min_futuro - Low_1min_futuro

				#Red Candles
				elif Open_1min_futuro > Close_1min_futuro:
					Aposta_Abaixo += 1
					Tamanho_candle_1min_futuro = Open_1min_futuro - Close_1min_futuro
					Pavio_superior_1min_futuro = High_1min_futuro - Open_1min_futuro
					Pavio_inferior_1min_futuro = Open_1min_futuro - Low_1min_futuro

				else:
					print("		CLOSE 1 MIN = OPEN 1 MIN : ", str(query))
					print(" Close 1 min = ", str(Close_1min_futuro))
					print(" Open 1 min = ", str(Open_1min_futuro))

					Aposta_Acima = 0
					Aposta_Abaixo = 0
					#print("		CLOSE 1 MIN = OPEN 1 MIN : " + str(query), *77)
					Tamanho_candle_1min_futuro = 0
					Pavio_superior_1min_futuro = 9999
					Pavio_inferior_1min_futuro = 9999

				horario_candle_2min_futuro = str(query_geral[i][1])
				horario_candle_2min_futuro = datetime.strptime(horario_candle_2min_futuro, "%H:%M:%S")
				horario_candle_2min_futuro = horario_candle_2min_futuro + timedelta(minutes=62)
				horario_candle_2min_futuro = str(horario_candle_2min_futuro)[11:]
				horario_candle_2min_futuro = datetime.strptime(horario_candle_2min_futuro, "%H:%M:%S").time()

				query = executor_bd.execute("SELECT * FROM `1minuto` WHERE `Date` = "+ str(data_candle_1hora) + " AND `Timestamp` = '" + str(horario_candle_2min_futuro)+"'")
				query = executor_bd.fetchall()

				Open_2min_futuro = query[0][2]
				High_2min_futuro = query[0][3]
				Low_2min_futuro = query[0][4]
				Close_2min_futuro = query[0][5]

				if Close_2min_futuro > Open_2min_futuro:
					Aposta_Acima += 1
				elif Open_2min_futuro > Close_2min_futuro:
					Aposta_Abaixo += 1
				else:
					print("		CLOSE 1 MIN = OPEN 1 MIN : ", str(query))
					print(" Close 1 min = ", str(Close_1min_futuro))
					print(" Open 1 min = ", str(Open_1min_futuro))
					Aposta_Acima = 0
					Aposta_Abaixo = 0

				''' TAVA ASSIM, ARRUMEI DIA 15/08/2022

				if Close_1min_futuro > Open_1min_futuro:
					Aposta_Acima += 1
				elif Open_1min_futuro < Close_1min_futuro:
					Aposta_Abaixo += 1
				else:
					print("		CLOSE 1 MIN = OPEN 1 MIN : ", str(query))
					print(" Close 1 min = ", str(Close_1min_futuro))
					print(" Open 1 min = ", str(Open_1min_futuro))
					Aposta_Acima = 0
					Aposta_Abaixo = 0
				'''


				print("			CHEGOU ATÉ AQUI PARA FAZER A APOSTA 		"*10)
				print('*'*69)
				print('Aposta_Acima = ', Aposta_Acima)
				print('Aposta_Abaixo = ', Aposta_Abaixo)
				print('Tamanho_candle_1min_futuro = ', str(Tamanho_candle_1min_futuro))
				if Tamanho_candle_1min_futuro != 0:
					if (Tamanho_candle_1min_futuro >= porcentagem_pavio_futuro*Pavio_superior_1min_futuro) and (porcentagem_pavio_futuro*Tamanho_candle_1min_futuro >= Pavio_inferior_1min_futuro) and (Aposta_Acima == 2 or Aposta_Abaixo == 2) : 

						if Aposta_Acima >= 1:
							direcao_aposta = "CALL"

						elif posta_Abaixo >= 1:
							direcao_aposta = "PUT"
						
						#print("verificou o maior")
						return {'Viavel': True, 'Direcao': direcao_aposta}, data_hora_inicio_analise, Aposta_Abaixo, Aposta_Acima

			else:
				#Não irá fazer a operacao
				return {'Viavel': False}, 0, 0, 0

	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		erro = str(e) + " 	|| LINHA: " + str(exc_tb.tb_lineno)
		Imprimir_Erro.Printar(str(erro), str('Buscar_BD.py'), str('Comparar_BD'))


		 