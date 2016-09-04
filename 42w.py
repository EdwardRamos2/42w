# 42w 
# Version 0.1.0 Date 09-03-2016
# Edward Ramos
# https://github.com/EdwardRamos2/42w

print ("42w")
print ("Version 0.1.1")
print ("Edward Ramos")
print ("https://github.com/EdwardRamos2/42w/")
import os

print ("MENU")
opcao1 = (raw_input("ENTER (1) - PARA VERFICAR INTERFACES:  "))

if opcao1 == '1':
 onl = os.system("iw dev")
 print onl


opcao2 = (raw_input("ENTER (2) - check PROCESSOS ATIVOS:  "))
if opcao2 == '2':
	fina = os.system("airmon-ng check")
	print fina
	
opcao3 = (raw_input("ENTER (3) - kill PROCESSOS ATIVOS:  "))
if opcao3 == '3':
	morte = os.system("airmon-ng check kill")	
	print morte

opcao4 = (raw_input("DIGITE NOME SUA  INTERFACE: "))
print ("wlan1 e wlan0 aceitos")

if opcao4 == 'wlan1':
	uppp = os.system("ifconfig wlan1 up")
	print uppp
elif opcao4 == 'wlan0':
	uppp2 = os.system("ifconfig wlan0 up")
	print uppp2	

listar2 = os.system("ifconfig")	
print listar2

sair = (raw_input("ENTER (5) - PARA SAIR:  "))
 
if sair == '5':
	print ("Saindo em 3.2.1")
	exit
else:
	print ("error, digite o valor solicitado :)")




