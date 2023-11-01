import subprocess
import os

# Configurações de Path
new_folder_kaggle = '/home/michel/Documentos/batch_olistbrasil_etl/data/transient'
download_path = "/home/michel/Documentos/batch_olistbrasil_etl/data/transient"

# Nome do conjunto de dados
dataset_name = "michelsouzasantana/brazilian-olist-ecommerce"

# Verificar se o arquivo já existe na pasta de destino
file_name = f"{download_path}/{dataset_name.split('/')[1]}.zip"
if not os.path.exists(file_name):
    # Criando o diretório para receber os arquivos do Kaggle
    subprocess.run(['mkdir', '-p', new_folder_kaggle])

    # Baixando os dados do Kaggle
    subprocess.run(['kaggle', 'datasets', 'download', '-d', dataset_name, '-p', download_path])

    # Descompactando os arquivos baixados com a opção -o para substituir sem prompt
    subprocess.run(['unzip', '-o', file_name, '-d', download_path])

    # Deletando o arquivo zip após descompactar
    subprocess.run(['rm','-r', file_name, '-d', download_path + '/' + file_name])
else:
    pass
