import os
import shutil
import pandas as pd

# Diretórios de origem e destino
dir_transiente = '/home/michel/Documentos/batch_olistbrasil_etl/data/transient'
dir_raw = '/home/michel/Documentos/batch_olistbrasil_etl/data/raw'

# Lista de arquivos na pasta 'transient'
arquivos_transiente = os.listdir(dir_transiente)

# Lista de arquivos na pasta 'raw'
arquivos_raw = os.listdir(dir_raw)

# Percorra os arquivos na pasta 'transient'
for arquivo in arquivos_transiente:
    caminho_arquivo_transiente = os.path.join(dir_transiente, arquivo)
    caminho_arquivo_raw = os.path.join(dir_raw, arquivo)

    # Verifique se o arquivo já existe na pasta 'raw'
    if arquivo in arquivos_raw:
        # Se o arquivo já existe na pasta 'raw, faça a concatenação e elimine as duplicatas
        df_transiente = pd.read_csv(caminho_arquivo_transiente)
        df_raw = pd.read_csv(caminho_arquivo_raw)

        # Combine os DataFrames e elimine as duplicatas
        df_combined = pd.concat([df_raw, df_transiente])
        df_combined = df_combined.drop_duplicates()

        # Salve o arquivo atualizado na pasta 'raw'
        df_combined.to_csv(caminho_arquivo_raw, index=False)
        print(f'Arquivo {arquivo} atualizado em raw.')
    else:
        # Se o arquivo não existe na pasta 'raw, crie um novo
        shutil.copy(caminho_arquivo_transiente, caminho_arquivo_raw)
        print(f'Arquivo {arquivo} criado em raw.')

print('Processo concluído.')