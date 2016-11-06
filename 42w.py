#!/usr/bin/env python
# 42w 
# Version 0.1.0 Date 09-03-2016
# Edward Ramos
# https://github.com/EdwardRamos2/42w
import sys
import os
print ("42w")
print ("Version 0.1.1  NEW Version 0.2.1")
print ("Edward Ramos")
print ("https://github.com/EdwardRamos2/42w/")
"""
def menu_opcoes():
    menu_wireless = open('menu.txt')
    print(menu_wireless.read())  
    opcao = input('')
    if opcao == '1':
        os.system('ifconfig')
    elif opcao == '2':
        print('Saindo em 3...');print('2..');print('1.')
        sys.exit(1)
menu_opcoes()

def download_interface():
    download_faces = open('interface.txt')
    print(download_faces.read())
         
    opcao_interface = input('(+) Interface: ')
    if opcao_interface == '1':
        print('(+) Interface escolhida: (wlan0) Opcao: %s' % opcao_interface)
        os.system('ifconfig wlan0 down ')
    elif opcao_interface == '2':
        print('(+) Interface escolhida: (wlan1) Opcao: %s' % opcao_interface)
        os.system('ifconfig wlan1 down')
    elif opcao_interface == '3':
        print('(+) Interface escolhida: (wlp3s0) Opcao: %s' % opcao_interface)
        os.system('ifconfig wlp3s0 down')
    elif opcao_interface == '4':
        print('(+) Interface escolhida: (wlp0s20u1) Opcao: %s' % opcao_interface)
        os.system('ifconfig wlp0s20u1 down')
download_interface()
"""

def tipo_attack():
    opcao_attack = open('tipo_attacks.txt')
    print(opcao_attack.read())
    mac_alvo = input('Digite o MAC Router Destino: Exemplo: 54:B8:0A:F3:3F:C3 >>>  ')
    mac_usuario = input('Digite o MAC Cliente Router Destino: Exemplo: B8:5A:73:AC:60:CC >>>  ')
    delimiter = ':'
    mac_alvo = mac_alvo.split(delimiter)
    print(mac_alvo)
    #if opcao_attack == '-0':
   #     os.system()
tipo_attack()


