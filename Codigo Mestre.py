import sys, os
from datetime import datetime, timedelta
import Imprimir_Erro
import Buscar_BD
import Variaveis_Principais
import Operacoes
import estrategia
import Log_Relatorios

Variaveis = Variaveis_Principais.Variaveis()
Saldo_Real = Variaveis['Saldo']
nome_arquivo = Variaveis['nome_arquivo']
Variaveis = estrategia.Variaveis()
Valor_Aposta = Variaveis['valor_da_aposta_inicial'] 
Alimentacao_LOG = {}




print("Inicio da AI CRIPTOPH:	", str(datetime.now()))
print('----------------------------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------------------------')
print("                                    	  SALDO INICIAL: ", Saldo_Real)
print('----------------------------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------------------------\n')


while True:
	try:
		Verificacao, Alimentacao_LOG['data_hora_inicio'], Alimentacao_LOG['Qnt_aposta_abaixo'], Alimentacao_LOG['Qntd_aposta_acima'] = Buscar_BD.Comparar_BD()

		if Verificacao['Viavel'] == False:
			continue
		else:
			print("Indo apostar")
			Apostar, Saldo_Real, Alimentacao_LOG['data_horario_aposta'], Alimentacao_LOG['direcao_aposta'], Alimentacao_LOG['valor_da_aposta'] = Operacoes.Operar(Verificacao, Alimentacao_LOG, Valor_Aposta)
			print("apostou")
			Valor_Aposta, Alimentacao_LOG['Resultado'], Alimentacao_LOG['Lucro_Atual'], Alimentacao_LOG['Saldo_Atual'], Alimentacao_LOG['Assertividade'] = Operacoes.Resultado_Operacao(Saldo_Real, Verificacao, Valor_Aposta)
			chamar_arquivo = Log_Relatorios.Relatorios(Alimentacao_LOG, nome_arquivo)
			print("resetou")
	except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			erro = str(e) + " 	|| LINHA: " + str(exc_tb.tb_lineno)
			Imprimir_Erro.Printar(str(erro), str('Buscar_BD.py'), str('Candle_Temporaria'))


