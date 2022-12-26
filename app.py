import os
import re


caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')
arquivos = os.listdir(caminho)
for arquivo in arquivos:
    if 'txt' in arquivo:
        with open(os.path.join(f'{caminho}',f'{arquivo}')) as f:
            valores = f.readlines()
            print(*valores)
   
    