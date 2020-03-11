import cv2
import numpy as np
import os
from os.path import isfile, join
import glob

# pasta onde estão suas imagens
caminhoArquivos= '/home/rodrigo/Documents/jpg-to-mp4/py-convert-mp4/imgs/'

# pasta + nome do arquivo de saída
output= '/home/rodrigo/Documents/jpg-to-mp4/py-convert-mp4/result/result.mp4'

#configuração padrão
width = 1920
height = 1080 
dim = (width, height)
size = (width,height)

fps = 0.5
listaImagens = []

#lê os arquivos na pasta
imagens = [f for f in os.listdir(caminhoArquivos) if isfile(join(caminhoArquivos, f))]

#ordenação dos arquivos pelo nome
imagens.sort(key = lambda x: x[5:-4])


for i in range(len(imagens)):
    # pega o nome do arquivo
    filename=caminhoArquivos + imagens[i]

    #pega o arquivo a partir do nome
    img = cv2.imread(filename)

    #altera a imagem para ficar com tamanho padrão
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    #insere a imagem na lsita de imagens para o video
    listaImagens.append(resized)
    
#declaração do obj utilizado para gerar o video
out = cv2.VideoWriter(output,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
for i in range(len(listaImagens)):
    # inserindo as imagens no video
    out.write(listaImagens[i])
#gerar o video
out.release()