#!/usr/bin/env python3
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
	layout = [ [sg.Text('Insira os dados')], [sg.Text('Caminho para pasta com imagens:', size=(50, 1), auto_size_text=False, justification='left'), sg.InputText('Pasta'), sg.FolderBrowse()], [sg.Text('Caminho para pasta de destino:', size=(50, 1), auto_size_text=False, justification='left'), sg.InputText('Pasta'), sg.FolderBrowse()], [sg.Text('Nome do arquivo: (default = result.mp4)', size=(50,1)), sg.InputText()], [sg.Text('Largura',size=(50,1)), sg.InputText()], [sg.Text('Altura', size=(50,1)), sg.InputText()], [sg.Text('FPS', size=(50,1)), sg.InputText()], [sg.Button('Ok'), sg.Button('Cancel')], [sg.Text('Powered By github.com/rodrigo-sntg')] ] 
					
	# Create the Window 
	window = sg.Window('Conversor User Interface', layout)
	#window = sg.Window('Conversor', layout)
	
	# Event Loop to process "events" and get the "values" of the inputs 
	while True: 
		event, values = window.read() 
		if event in (None, 'Cancel'):	
		# if user closes window or clicks cancel 
			break 
		if event in ('Ok'):	
			if values[0] == '':
				sg.Popup('Resultado', 'Insira dados válidos.')
				continue
			
			else:
				if not values[0].endswith('/'):
					values[0] = values[0] + '/'

				result = convert(values[0], values[1], values[3], values[4], values[5], values[2])
				sg.Popup('Resultado', result)
		
		#print('You entered ', values[0]) 

	window.close()
	
	
def convert(inputFile, outputFile, largura, altura, inputFps, nome):
	
	try:
		
		# pasta onde estão suas imagens #caminhoArquivos= '/home/rodrigo/Documents/jpg-to-mp4/py-convert-mp4/imgs/' 

		caminhoArquivos = inputFile 
		# pasta + nome do arquivo de saída # output= '/home/rodrigo/Documents/jpg-to-mp4/py-convert-mp4/result/result.avi' 
		if nome == '':
			nome = 'result.mp4'

		if outputFile == 'Pasta':
			outputFile = inputFile
		else:
			outputFile = outputFile + '/'

		output = outputFile + nome
		
		
		#configuração padrão 
		if largura == '':
			largura = 1080
		width = int(largura)
		
		if altura == '':
			altura = 720
		height = int(altura)
			
		dim = (width, height) 
		size = (width,height) 
		
		if inputFps == '':
			inputFps = 1.0
		fps = float(inputFps)
			
		listaImagens = [] 
		
		#lê os arquivos na pasta 
		imagens = []
		relevant_path = caminhoArquivos
		included_extensions = ['jpg','jpeg', 'bmp', 'png', 'gif']
		imagens = [fn for fn in os.listdir(relevant_path) if any(fn.endswith(ext) for ext in included_extensions)]
		
		
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
