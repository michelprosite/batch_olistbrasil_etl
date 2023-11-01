import subprocess
import os

# Configurações de Path
new_folder_kaggle = 'C:/Users/michel/Documents/batch_olistbrasil_etl/data/kaggle'
download_path = 'C:/Users/michel/Documents/batch_olistbrasil_etl/data/kaggle'

# Nome do conjunto de dados
dataset_name = "michelsouzasantana/brazilian-olist-ecommerce"

# Verificar se o arquivo já existe na pasta de destino
file_name = f"{download_path}/{dataset_name.split('/')[1]}.zip"
if not os.path.exists(file_name):
    # Criando o diretório para receber os arquivos do Kaggle
    os.makedirs(new_folder_kaggle, exist_ok=True)

    # Baixando os dados do Kaggle
    subprocess.run(['kaggle', 'datasets', 'download', '-d', dataset_name, '-p', download_path])

    # Descompactando os arquivos baixados
    subprocess.run(['tar', '-xvf', file_name, '-C', download_path])

    # Deletando o arquivo zip após descompactar
    os.remove(file_name)
else:
    pass
