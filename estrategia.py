from Operacoes import determinar_direcao_tendencia

def verificar_5minutos(velas_15min_compatíveis, proporcao_aceitacao):
    velas_5min_compatíveis = []
    for i in range(3):
        vela_5min_atual = Requisicoes.requisitar_vela_5minutos(i)

        for vela_15min in velas_15min_compatíveis:
            velas_5min_banco = buscar_velas("5min", vela_15min["timestamp"])
            vela_5min_banco = velas_5min_banco[i]

            velas_compatíveis = filtrar_velas_por_proporcao(
                [vela_5min_banco], proporcao_aceitacao, vela_5min_atual
            )

            if velas_compatíveis:
                velas_5min_compatíveis.append(vela_5min_banco)

    return velas_5min_compatíveis
    
# ...

def verificar_15minutos(vela_1h_atual, velas_1h_compatíveis, proporcao_aceitacao):
    velas_15min_compatíveis = []
    for i in range(4):
        vela_15min_atual = Requisicoes.requisitar_vela_15minutos(i)

        for vela_1h in velas_1h_compatíveis:
            velas_15min_banco = buscar_velas("15min", vela_1h["timestamp"])
            vela_15min_banco = velas_15min_banco[i]

            velas_compatíveis = filtrar_velas_por_proporcao(
                [vela_15min_banco], proporcao_aceitacao, vela_15min_atual
            )

            if velas_compatíveis:
                velas_15min_compatíveis.append(vela_15min_banco)

    return velas_15min_compatíveis

# ...

def Variaveis():
	################################################	PRINCIPAIS VARIÁVEIS	#################################
	Todas_Variaveis = {

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



	############################################################################################################
	return Todas_Variaveis

'''
	'margem_erro':	0.30,	#em % (decimais)
	'margem_de_erro_15_minutos': 0.30,	#em % (decimais)
	'margem_de_erro_5_minutos': 0.60,	#em % (decimais)
	'valor_da_aposta_inicial': 0.35,
	'Conta_Real': False,
	'duracao_da_aposta': 5, #em minutos
	'Mercado': "R_10",	#frxAUDJPY
	'Minimo_Apostas': 2,
	'minimo_de_variacoes': { #Minimo de variacoes possiveis para delta(tamanho_candle, var_pavio_sup e var_pavio_inf)
		"<1": 1,	#quantas vao ser menor que 1 			#antes do dia 15/09/2021 às 21:22 estava 2
		"<2": 3,	#quantas vao ser menor que 2
		"<3": 3,	#quantas vao ser menor que 3
'''

'''
	'margem_erro':	0.30,	#em % (decimais)
	'margem_de_erro_15_minutos': 0.30,	#em % (decimais)
	'margem_de_erro_5_minutos': 0.40,	#em % (decimais)
	'valor_da_aposta_inicial': 0.35,
	'Conta_Real': False,
	'duracao_da_aposta': 5, #em minutos
	'Mercado': "R_10",	#frxAUDJPY
	'Minimo_Apostas': 2,

'''

'''
	'margem_erro':	0.40,	#em % (decimais)
	'margem_de_erro_15_minutos': 0.30,	#em % (decimais)
	'margem_de_erro_5_minutos': 0.40,	#em % (decimais)




	'Minimo_Apostas': 5,

'''

'''
	'margem_erro':	0.50,	#em % (decimais)
	'margem_de_erro_15_minutos': 0.40,	#em % (decimais)
	'margem_de_erro_5_minutos': 0.30,	#em % (decimais)




	'Minimo_Apostas': 5,
'''


'''
	'margem_erro':	0.76,	#em % (decimais)
	'margem_de_erro_15_minutos': 0.51,	#em % (decimais)
	'margem_de_erro_5_minutos': 0.40,	#em % (decimais)



	'Minimo_Apostas': 5,
'''


def Escolher_Direcao(Aposta_Abaixo, Aposta_Acima):
	Apostas = Variaveis()
	Minimo_Apostas = Apostas['Minimo_Apostas']

	if (Aposta_Abaixo != 0) or (Aposta_Acima != 0):
		if (Aposta_Acima > Aposta_Abaixo) and (Aposta_Acima >= Minimo_Apostas) :
			direcao_aposta = "CALL"
			quantidade_ganhadora = Aposta_Acima
		elif (Aposta_Abaixo > Aposta_Acima) and (Aposta_Abaixo >= Minimo_Apostas):
			direcao_aposta = "PUT"
			quantidade_ganhadora = Aposta_Abaixo
		else:
			Aposta_Abaixo = 0
			Aposta_Acima = 0
			return False
	return direcao_aposta


def Pegar_Variacoes(var_tam_candle, var_pavio_sup, var_pavio_inf):
	variacoes = []
	variacoes.append(var_tam_candle)
	variacoes.append(var_pavio_sup)
	variacoes.append(var_pavio_inf)
	print("VARIACOES:	", variacoes)

	menor_3 = 0
	menor_2 = 0
	menor_1 = 0

	for i in variacoes:
		if (i <= 3):	#tamanho da candle
			menor_3 += 1
		if (i <= 2):	#pavio superior
			menor_2 += 1
		if (i <= 1):	#pavio inferior
			menor_1 += 1
	print("menor_1:	", menor_1)
	print("menor_2:	", menor_2)
	print("menor_3:	", menor_3)
	return menor_1, menor_2, menor_3
