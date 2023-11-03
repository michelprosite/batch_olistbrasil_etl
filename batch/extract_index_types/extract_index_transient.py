import pandas as pd
import os

# Defina o caminho da pasta onde estão os arquivos CSV
pasta = '/home/michel/Documentos/batch_olistbrasil_etl/data/transient'

# Crie um DataFrame vazio para armazenar as informações
informacoes = pd.DataFrame(columns=['Arquivo', 'Coluna', 'Tipo'])

# Percorra os arquivos na pasta
for arquivo in os.listdir(pasta):
    if arquivo.endswith('.csv'):
        caminho_arquivo = os.path.join(pasta, arquivo)
        
        # Leia o arquivo CSV
        df = pd.read_csv(caminho_arquivo)
        
        # Obtém o nome das colunas e seus tipos
        colunas = df.columns
        tipos = df.dtypes
        
        # Crie um DataFrame temporário com as informações do arquivo atual
        temp_df = pd.DataFrame({'Arquivo': [arquivo] * len(colunas), 'Coluna': colunas, 'Tipo': tipos})
        
        # Adicione as informações ao DataFrame principal
        informacoes = pd.concat([informacoes, temp_df], ignore_index=True)

# Salve as informações em um arquivo CSV
informacoes.to_csv('/home/michel/Documentos/batch_olistbrasil_etl/data/table_indices_types/tabela_index_types_transientt.csv', index=False)