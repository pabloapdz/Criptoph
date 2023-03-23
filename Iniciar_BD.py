import pymysql 
from config import config

def Bando_de_Dados():
	bd = pymysql.connect(**config, charset='utf8')
	executor_bd = bd.cursor()
	return executor_bd