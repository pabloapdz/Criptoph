import Imprimir_Erro
import sys
from datetime import datetime, timedelta
import estrategia
import time
 
def Verificar_Necessidade_Pausa():
	try:
		Variaveis = estrategia.Variaveis()
		Mercado = Variaveis['Mercado']
		hoje = datetime.now()
		dia_atual = hoje.date()
		horario_atual = hoje.time()
		dia_da_semana = dia_atual.isocalendar()[2]  
		#print(dia_da_semana)

		if Mercado == 'frxAUDJPY':
			horario_abertura_mercado = '20:59:59'
			horario_fechamento_mercado = '18:00:00'
		else:
			dia_da_semana = 20
			horario_abertura_mercado = '01:59:59'
			horario_fechamento_mercado = '01:59:50'

		horario = horario_atual.strftime('%H:%M:%S')
		formato = '%H:%M:%S'	

		if (dia_da_semana == 6 ):
			Motivo = 'Fim de semana'
			tempo_restante = (datetime.strptime(horario_abertura_mercado, formato) - datetime.strptime(horario, formato)).total_seconds() + 86401 
			Entrou = True

			# Domingo
		elif (dia_da_semana == 7 ):
			Motivo = 'fim de semana'
			tempo_restante = (datetime.strptime(horario_abertura_mercado, formato) - datetime.strptime(horario, formato)).total_seconds() + 1 
			Entrou = True

		#else:
		#	Imprimir_Erro.Printar(str(e), str('Pausar.py'), str('Verificar_Necessidade_Pausa 	|| 		ERRO NO TRATAMENTO DO HORÁRIO DE OPERAÇÕES'))


			if (Entrou == True):
				print('----------------------------------------------------------------------------------------------------------')
				print('----------------------------------------------------------------------------------------------------------')
				print('                                       FORA DO HORÁRIO DE OPERAÇÃO                                        ')
				print('----------------------------------------------------------------------------------------------------------')
				print('                                          Motivo:', Motivo)
				print('                         Aguarde por', tempo_restante, 'segundos para o reinício do sistema              ')
				print('----------------------------------------------------------------------------------------------------------')
				print('----------------------------------------------------------------------------------------------------------\n')

				Entrou = False
				Motivo = ''
				
			time.sleep(tempo_restante)	
			tempo_restante = 0
		return True

		'''
		if (((dia_da_semana == 1 ) or  (dia_da_semana == 2) or  (dia_da_semana == 3) or  (dia_da_semana == 4)) and (int(horario_atual.hour) >= 18) and int(horario_atual.hour) <= 20 and int(horario_atual.hour) < 59) or ((dia_da_semana == 5 ) and (int(horario_atual.hour) >= 18)) or (dia_da_semana == 6 ) or ((dia_da_semana == 7 ) and (int(horario_atual.hour) <= 20) and ((horario_atual.minute <= 59))):

			# Segunda-feira à Quinta-feira
			if (((dia_da_semana == 1 ) or  (dia_da_semana == 2) or  (dia_da_semana == 3) or  (dia_da_semana == 4)) and ((int(horario_atual.hour) >= 18) and int(horario_atual.hour) <= 20 and int(horario_atual.hour) < 59)):
				Motivo = 'Dia de semana anterior a sexta após 21h'
				tempo_restante = (datetime.strptime(horario_abertura_mercado, formato) - datetime.strptime(horario, formato)).total_seconds() + 1
				Entrou = True

			# Sexta-feira
			elif (dia_da_semana == 5 ) and (int(horario_atual.hour) >= 18):
				Motivo = 'Dia de semana, sexta feira após 21h'
				tempo_restante = (datetime.strptime(horario_abertura_mercado, formato) - datetime.strptime(horario, formato)).total_seconds() + 172801 
				Entrou = True

			# Sábado
			elif (dia_da_semana == 6 ):
				Motivo = 'Fim de semana'
				tempo_restante = (datetime.strptime(horario_abertura_mercado, formato) - datetime.strptime(horario, formato)).total_seconds() + 86401 
				Entrou = True

			# Domingo
			elif (dia_da_semana == 7 ):
				Motivo = 'fim de semana'
				tempo_restante = (datetime.strptime(horario_abertura_mercado, formato) - datetime.strptime(horario, formato)).total_seconds() + 1 
				Entrou = True

			else:
				Imprimir_Erro.Printar(str(e), str('Pausar.py'), str('Verificar_Necessidade_Pausa 	|| 		ERRO NO TRATAMENTO DO HORÁRIO DE OPERAÇÕES'))


			if (Entrou == True):
				print('----------------------------------------------------------------------------------------------------------')
				print('----------------------------------------------------------------------------------------------------------')
				print('                                       FORA DO HORÁRIO DE OPERAÇÃO                                        ')
				print('----------------------------------------------------------------------------------------------------------')
				print('                                          Motivo:', Motivo)
				print('                         Aguarde por', tempo_restante, 'segundos para o reinício do sistema              ')
				print('----------------------------------------------------------------------------------------------------------')
				print('----------------------------------------------------------------------------------------------------------\n')

				Entrou = False
				Motivo = ''
				
			time.sleep(tempo_restante)	
			tempo_restante = 0
		return True
		'''
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		erro = str(e) + " 	|| LINHA: " + str(exc_tb.tb_lineno)
		Imprimir_Erro.Printar(str(erro), str('Pausar.py'), str('Verificar_Necessidade_Pausa'))