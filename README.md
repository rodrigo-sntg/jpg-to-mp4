# Conversor de Imagens para MP4

# Como instalar python no windows
Seguir instruções em:
https://www.python.org/downloads/

## Executando
### Windows
Entrar na pasta dist, baixar o arquivo convert-gui-full.exe  
Double click no arquivo para executar.

### Linux
Entrar na pasta dist, baixar o arquivo convert-gui-linux  
Abrir o terminal na pasta onde baixou o arquivo e executar com ./convert-gui-linux
Ou clicar duas vezes no arquivo para abrir.


## chamando a função
### Instalando biblioteca necessária
    pip3 install opencv-python  

### argumentos
    -i - Em qual pasta estão as imagens  
    -o - Nome do arquivo de output ou pasta + nome  

### Exemplo
    python3 convert.py -i '/home/rodrigo/Documents/jpg-to-mp4/py-convert-mp4/imgs/' -o '/home/rodrigo/Documents/jpg-to-mp4/py-convert-mp4/result/teste.avi'