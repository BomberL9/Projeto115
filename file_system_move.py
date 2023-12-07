import os

source = 'main.txt'
dest = 'newfile.txt'

os.rename(source, dest)

print('O caminho de origem foi renomeado para arquivo de destino com sucesso.')