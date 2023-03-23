import Imprimir_Erro
import Variaveis_Principais
import websocket
import json
import time
import sys

Variaveis = Variaveis_Principais.Variaveis()
TOKEN = Variaveis['token']
API_URL = Variaveis['API_URL']

def Saldo():
	global API_URL, TOKEN
	Tentativas = 0
	ws_Balance = websocket.create_connection(API_URL, max_queue=1)
	ws_Balance.send(json.dumps(TOKEN))
	Entrando = json.loads(ws_Balance.recv()) 
	while True:
		try:
			ws_Balance.send(json.dumps({"balance": 1, "subscribe": 0}))
			resultado_op = json.loads(ws_Balance.recv()) 
			time.sleep(1)
			#Tentativas = 0
			return float(resultado_op['balance']['balance'])
		except Exception as e:
			print("Não conseguiu pegar o saldo ... tentativa: ", Tentativas, "	>>	", resultado_op)
			Tentativas = Tentativas + 1
			ws_Balance = websocket.create_connection(API_URL, max_queue=1)
			time.sleep(1)
			ws_Balance.send(json.dumps(TOKEN))
			ws_Balance.recv()
			
			if Tentativas >= 10:
				try:
					exc_type, exc_obj, exc_tb = sys.exc_info()
					erro = str(e) + " 	|| LINHA: " + str(exc_tb.tb_lineno)
					Imprimir_Erro.Printar(str(erro), str('Requisicoes.py'), str('Saldo'))
					Tentativas = 0
				except Exception as e:
					exc_type, exc_obj, exc_tb = sys.exc_info()
					erro = "LINHA: " + str(exc_tb.tb_lineno)

					Imprimir_Erro.Printar(str(erro), str('Requisicoes.py'), str('Saldo'))		

Saldo_Inicial = Saldo()

def Operacao(mensagem_op):
	global API_URL, TOKEN
	Tentativas = 0
	ws_Operacao = websocket.create_connection(API_URL, max_queue=1)
	ws_Operacao.send(json.dumps(TOKEN))
	Entrando = json.loads(ws_Operacao.recv()) 
	try:
		while True:
			if Tentativas >= 10:
				print("*"*300)
				print("resultado_op:	", resultado_op)
				print("*"*300)
				quit()
			try:
				ws_Operacao.send(json.dumps(mensagem_op))
				resultado_op = json.loads(ws_Operacao.recv()) 
				print("Tentativa...:		", Tentativas,	"COM ESSE RESULTADO_OP:	", resultado_op)
				break
			except Exception as e:
				Tentativas = Tentativas + 1
				ws_Operacao = websocket.create_connection(API_URL, max_queue=1)
				time.sleep(2)
				ws_Operacao.send(json.dumps(TOKEN))
				receber_TOKEN = ws_Operacao.recv()
				print("ENTROU NO EXCEPT POR CONTA DE:	", str(e))
				time.sleep(2)
				continue

		time.sleep(1)
		try:
			if resultado_op['error']['code'] == 'AuthorizationRequired':
				Imprimir_Erro.printar(str(resultado_op['error']['code']), str('Requisicoes.py'), str('Operacao'))
				quit()
		except Exception as e:
			pass
		
		return resultado_op
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		erro = str(e) + " 	|| LINHA: " + str(exc_tb.tb_lineno)
		Imprimir_Erro.Printar(str(erro), str('Requisicoes.py'), str('Operacao'))


		#print("Erro		->", str(e) + " " + str(exc_type) + " " + str(fname) + " " + " //" + str(exc_tb) + " Requisicao: " + str(mensagem_op))



def Buscar_Candle(req_candle):
	global API_URL
	Tentativas = 0
	ws_Buscar_Candle = websocket.create_connection(API_URL, max_queue=1)

	Tentativas = 0
	while True:
		try:
			if Tentativas >= 10:
				try:
					exc_type, exc_obj, exc_tb = sys.exc_info()
					erro = str(e) + " 	|| LINHA: " + str(exc_tb.tb_lineno)
					Imprimir_Erro.Printar(str(erro), str('Requisicoes.py'), str('Buscar_Candle'))
				except Exception as e:
					exc_type, exc_obj, exc_tb = sys.exc_info()
					erro = "LINHA: " + str(exc_tb.tb_lineno)
					Imprimir_Erro.Printar(str(erro), str('Requisicoes.py'), str('Buscar_Candle'))					
			ws_Buscar_Candle.send(json.dumps(req_candle))
			resultado_candle = ws_Buscar_Candle.recv()
			return json.loads(resultado_candle)
		except Exception as e:
			Tentativas = Tentativas + 1
			ws_Buscar_Candle = ''
			ws_Buscar_Candle = websocket.create_connection(API_URL, max_queue=1)
			time.sleep(2)
			pass

