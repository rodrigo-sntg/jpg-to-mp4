#!/usr/bin/python 
import sys, getopt
import cv2
import numpy as np
import os
from os.path import isfile, join
import glob 

import PySimpleGUI as sg

def main(argv): 
	inputfile = '' 
	outputfile = '' 
	
	sg.theme('DarkAmber')	
	layout = [ [sg.Text('Insira os dados')], [sg.Text('Caminho para pasta vom imagens:'), sg.InputText()],[sg.Text('Caminho e titulo pra o arquivo gerado: (ex C:/resultado.mp4'), sg.InputText()], [sg.Text('Largura'), sg.InputText()], [sg.Text('Altura'), sg.InputText()], [sg.Text('FPS'), sg.InputText()], [sg.Button('Ok'), sg.Button('Cancel')] ] 
					
	# Create the Window 
	window = sg.Window('Window Title', layout)
	#window = sg.Window('Conversor', layout)
	
	# Event Loop to process "events" and get the "values" of the inputs 
	while True: 
		event, values = window.read() 
		if event in (None, 'Cancel'):	
		# if user closes window or clicks cancel 
			break 
		if event in ('Ok'):	
			if values[0] == '' or values[1] == '':
				sg.Popup('Resultado', 'Insira dados válidos.')
				continue
			
			else:
				if not values[0].endswith('/'):
					values[0] = values[0] + '/'

				result = convert(values[0], values[1], values[2], values[3], values[4])
				sg.Popup('Resultado', result)
		
		#print('You entered ', values[0]) 

	window.close()
	
	
def convert(inputFile, outputFile, largura, altura, inputFps):
	
	try:
		
		# pasta onde estão suas imagens #caminhoArquivos= '/home/rodrigo/Documents/jpg-to-mp4/py-convert-mp4/imgs/' 

		caminhoArquivos = inputFile 
		# pasta + nome do arquivo de saída # output= '/home/rodrigo/Documents/jpg-to-mp4/py-convert-mp4/result/result.avi' 
		output = outputFile 
		
		#configuração padrão 
		width = int(largura)
		if largura == '':
			width = 1920 
		
		height = int(altura)
		if altura == '':
			height = 1080 
			
		dim = (width, height) 
		size = (width,height) 
		
		fps = float(inputFps)
		if inputFps == '':
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
		out = cv2.VideoWriter(output,cv2.VideoWriter_fourcc(*'DIVX'), fps, size) 
		for i in range(len(listaImagens)): 
			# inserindo as imagens no video 
			out.write(listaImagens[i]) 
			#gerar o video 
			out.release() 
		return 'Exportação Efetuada com sucesso.'
	except expression as identifier:
		return 'Não foi possível exportar.'
		


if __name__ == "__main__":
   main(sys.argv[1:])
