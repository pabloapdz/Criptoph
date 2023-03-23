from datetime import datetime, timedelta
import calendar

def Relatorios(Alimentacao_LOG, nome_arquivo):
	arquivo = open('Relatorios/' +str(nome_arquivo) +'/Relatorio de Operacoes.csv', 'a+')

	def Gerar_Relatorio(a={}):
		with arquivo:
			for i in a:
				arquivo.write(i)
				arquivo.close()


	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ RELATORIO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	Data_inicio = str((Alimentacao_LOG['data_hora_inicio']).date())
	Horário_inicio = str((Alimentacao_LOG['data_hora_inicio']).time())
	Data_realizacao = str((Alimentacao_LOG['data_horario_aposta']).date())
	Horario_realizacao = str((Alimentacao_LOG['data_horario_aposta']).time())
	Dia_semana_realizacao = str(calendar.day_name[Alimentacao_LOG['data_horario_aposta'].weekday()])
	#Lista_variacao = str(Alimentacao_LOG['Variacoes_lista'])
	#Maior_1 = str(Alimentacao_LOG['Menor_1'])
	#Maior_2 = str(Alimentacao_LOG['Menor_2'])
	#Maior_3 = str(Alimentacao_LOG['Menor_3'])
	Apostas_Cima = str(Alimentacao_LOG['Qntd_aposta_acima'])
	Apostas_Baixo = str(Alimentacao_LOG['Qnt_aposta_abaixo'])
	Direcao_aposta = str(Alimentacao_LOG['direcao_aposta']['Direcao'])
	Valor_apostado = str(round(Alimentacao_LOG['valor_da_aposta'], 2)).replace(".", ",")
	Resultado_final = str(Alimentacao_LOG['Resultado'])
	Lucro_atualizado = str(round(Alimentacao_LOG['Lucro_Atual'], 2)).replace(".", ",")
	Saldo_atualizado = str(round(Alimentacao_LOG['Saldo_Atual'], 2)).replace(".", ",")
	Assertividade = str(Alimentacao_LOG['Assertividade'])
	#print(Data_inicio,Horário_inicio,Data_realizacao,Horario_realizacao,Dia_semana_realizacao,Lista_variacao,Maior_1,Maior_2,Maior_3,Apostas_Cima,Apostas_Baixo,Direcao_aposta,Valor_apostado,Resultado_final,Lucro_atualizado,Saldo_atualizado,Assertividade)	
	#print("arrumou todas as variaveis")


	
	print("abriu o arquivo")

	string = Data_inicio+ ";" 
	print('1')
	string = string +Horário_inicio+ ";" 
	print('2')
	string = string +Data_realizacao+ ";" 
	print('3')
	string = string +Horario_realizacao+ ";" 
	print('4')
	string = string +Dia_semana_realizacao+ ";" 
	print('5')
	#string = string +Lista_variacao+ ";"
	#print('6')
	#print("primeira string arrumada")
	#string = string +Maior_1+ ";" 
	#print('7')
	#string = string +Maior_2+ ";" 
	#print('8')
	#string = string +Maior_3+ ";" 
	#print('9')
	string = string +Apostas_Cima+ ";" 
	print('10')
	string = string +Apostas_Baixo+ ";" 
	print('11')
	string = string +Direcao_aposta+ ";" 
	print('12')
	string = string +Valor_apostado+ ";"
	print('13')
	print("segunda string arrumada")
	string = string +Resultado_final+ ";" 
	print('14')
	string = string +Lucro_atualizado+ ";"
	print('15')
	string = string +Saldo_atualizado+ ";" 
	print('16')
	string = string +Assertividade+ "\n"
	print('17')
	print("terceira string arrumada")

	'''
	string = Data_inicio+ ";" +Horário_inicio+ ";" +Data_realizacao+ ";" +Horario_realizacao+ ";" +Dia_semana_realizacao+ ";" +Lista_variacao+ ";"
	print("primeira string arrumada")
	string = string +Maior_1+ ";" +Maior_2+ ";" +Maior_3+ ";" +Apostas_Cima+ ";" +Apostas_Baixo+ ";" +Direcao_aposta+ ";" +Valor_apostado+ ";"
	print("segunda string arrumada")
	string = string +Resultado_final+ ";" +Lucro_atualizado+ ";" +Saldo_atualizado+ ";" +Assertividade+ "\n"
	print("terceira string arrumada")
	'''
	print("Colocou tudo em uma só string")

	with arquivo:
		arquivo.write(string)
		arquivo.close()

	print("Escreveu o conteudo")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	return