# Passo a passo do projeto


# 1- Abrir o sistema da empresa
    # abrir navegador
    # entra no site
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
    # pyautogui.click -> clilcar com o mouse
    # pyautogui.write -> escrever um texto 
    # pyautogui.press -> pressionar uma tecla do teclado
    # pyautogui.hotkey -> aperta um conjuto de teclas (ctrl + C, ctrl v, Alt Tab)
 

import pyautogui
import time

pyautogui.PAUSE = 0.5

# abrir navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
# entra no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)
# 2- Fazer login
pyautogui.click(-1160, 468)
pyautogui.write("swer1405@outlook.com")

pyautogui.press("tab")
pyautogui.write("123456789")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# 3- Abrir/ Importa a base de dados de produtos para cadastrar
# pip install pandas numpy openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo" ])
    # 4- Cadastrar um produto
    #Clica na tabela
    pyautogui.click(-1302, 313)
    #preencher o codigo
    pyautogui.write(codigo)
    #passa para o proximo campo
    pyautogui.press("tab")
    #passa para o proximo campo
    pyautogui.write (str(tabela.loc[linha, "marca" ]))
    #passa para o proximo campo
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    #passa para o proximo campo
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    #passa para o proximo campo
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    #passa para o proximo campo
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    #passa para o proximo campo
    pyautogui.press("tab")
    #obs

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":    
        pyautogui.write(obs)
    #passa para o proximo campo
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000) 

    


# 5- Repetir isso tudo até acabar a lista de produtos