import pyautogui
import pandas as pd
import time

#importando base de dados
tabela = pd.read_csv("produtos.csv")
print(tabela) 


#pausa para cada comando
pyautogui.PAUSE = 0.5 

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
#sistema espera um pouco
time.sleep(2)
pyautogui.click(x=745, y=652)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(5)
pyautogui.click(x=807, y=504)
pyautogui.write("meuemail@gmail.com")
pyautogui.press("tab")
pyautogui.write("minhasenha123")
pyautogui.press("tab")
pyautogui.press("enter")

#percorrendo as linhas da tabela
#para cada linha insere um produto
for linha in tabela.index:
    pyautogui.click(x=721, y=358)
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
