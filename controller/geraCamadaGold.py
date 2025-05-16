from datetime import datetime
import pandas as pd
import numpy as np

# Caminho para o arquivo JSON da conta de serviço
SERVICE_ACCOUNT_FILE = "./config_param/electric-armor-429218-g7-f95603f613a1.json"
BUCKET_SILVER = "pulsar-transiente-zone"
BUCKET_GOLD = "pulsar-transiente-trust"
PROJECT_NAME = 'electric-armor-429218-g7'

#this variable is set based on the dataset you chose to query
#bf.options.bigquery.location = "us-east4" 
#this variable is set based on the dataset you chose to query
#bf.options.bigquery.project = "electric-armor-429218-g7" 


def getServiceAccountFile():
    return SERVICE_ACCOUNT_FILE

def gravaPrecificacaoDataFile(df,file_name, id):
    
    df['codigo'] = id
    df['data_sessao'] = df['data_sessao']
    
    df_precificacao = pd.read_csv(file_name, sep=';')
    df_precificacao = pd.concat([df_precificacao,df],ignore_index=True)
    df_ordenado = df_precificacao.sort_values(by='codigo', ascending=True)

    df_ordenado.to_csv(file_name, header=True,sep=';',index=False)
    print("Precificacao gravado com sucesso!")
    return id

def editaPrecificacaoDataFile(precificacao,file_name):

    df_precificacao = pd.read_csv(file_name, sep=';')
    df_precificacao = df_precificacao[df_precificacao.codigo != precificacao.codigo.iloc[0]]
    df_precificacao = pd.concat([df_precificacao,precificacao],ignore_index=True)
    df_ordenado = df_precificacao.sort_values(by='codigo', ascending=True)

    df_ordenado.to_csv(file_name, header=True,sep=';',index=False)
    print("Precificacao atualizada com sucesso!")
    return df_precificacao

def gravaItensPrecificacaoDataFile(df_ma, df_ml,df_mn,df_mo,df_ml_eth,df_ml_inv,df_ml_mala,df_ml_mon,df_ml_pio,df_ml_ptch,file_name,cod_precificacao):
    df_item = pd.read_csv(file_name,sep=';')
    ultimo_cod_param_item = df_item.iloc[-1]['codigo']+1

    df = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
    dados_grp_itens = []
    dados_itens = pd.read_csv('data/dados_itens.csv')
    
    if df_ma['qnt'].iloc[0] > 0:
        #@todo buscar no arquivo de itens o codigo referente a descrição
        cod_item = dados_itens[dados_itens['objeto'].isin([df_ma['cod_item'].iloc[0]])]
        
        df_ma['cod_item'].iloc[0] = cod_item.iloc[0]['codigo']
        df_ma['codigo'].iloc[0] = ultimo_cod_param_item
        dados_grp_itens.append([ultimo_cod_param_item,'MA',int(cod_precificacao)])
        ultimo_cod_param_item = ultimo_cod_param_item +1        
        df = pd.concat([df,df_ma],ignore_index=True)
        
        
    if df_ml['qnt'].iloc[0] > 0:
        cod_item = dados_itens[dados_itens['objeto'].isin([df_ml['cod_item'].iloc[0]])]
        df_ml['cod_item'].iloc[0] = cod_item.iloc[0]['codigo']
        df_ml['codigo'].iloc[0] = ultimo_cod_param_item
        dados_grp_itens.append([ultimo_cod_param_item,'ML',int(cod_precificacao)])
        ultimo_cod_param_item = ultimo_cod_param_item +1
        df = pd.concat([df,df_ml],ignore_index=True)

    if df_ml_ptch['qnt'].iloc[0] > 0 and df_ml_ptch['cod_item'].iloc[0] == True:
        #cod_item = bf.read_gbq_query('select t1.codigo from electric-armor-429218-g7.prf_cs.itens t1 where t1.objeto = \''+ str(df_ml_ptch['cod_item'].iloc[0]) + '\'')
        df_ml_ptch['cod_item'].iloc[0] = 12
        df_ml_ptch['codigo'].iloc[0] = ultimo_cod_param_item
        dados_grp_itens.append([ultimo_cod_param_item,'ML',int(cod_precificacao)])
        ultimo_cod_param_item = ultimo_cod_param_item +1
        df = pd.concat([df,df_ml_ptch],ignore_index=True)

    if df_ml_eth['qnt'].iloc[0] > 0 and df_ml_eth['cod_item'].iloc[0] == True:
        #cod_item = bf.read_gbq_query('select t1.codigo from electric-armor-429218-g7.prf_cs.itens t1 where t1.objeto = \''+ str(df_ml_eth['cod_item'].iloc[0]) + '\'')
        df_ml_eth['cod_item'].iloc[0] = 10
        df_ml_eth['codigo'].iloc[0] = ultimo_cod_param_item
        dados_grp_itens.append([ultimo_cod_param_item,'ML',int(cod_precificacao)])
        ultimo_cod_param_item = ultimo_cod_param_item +1
        df = pd.concat([df,df_ml_eth],ignore_index=True)

    if df_ml_inv['qnt'].iloc[0] > 0 and df_ml_inv['cod_item'].iloc[0] == True:
        #cod_item = bf.read_gbq_query('select t1.codigo from electric-armor-429218-g7.prf_cs.itens t1 where t1.objeto = \''+ str(df_ml_inv['cod_item'].iloc[0]) + '\'')
        df_ml_inv['cod_item'].iloc[0] = 11
        df_ml_inv['codigo'].iloc[0] = ultimo_cod_param_item
        dados_grp_itens.append([ultimo_cod_param_item,'ML',int(cod_precificacao)])
        ultimo_cod_param_item = ultimo_cod_param_item +1
        df = pd.concat([df,df_ml_inv],ignore_index=True)

    if df_ml_mala['qnt'].iloc[0] > 0 and df_ml_mala['cod_item'].iloc[0] == True:
        #cod_item = bf.read_gbq_query('select t1.codigo from electric-armor-429218-g7.prf_cs.itens t1 where t1.objeto = \''+ str(df_ml_mala['cod_item'].iloc[0]) + '\'')
        df_ml_mala['cod_item'].iloc[0] = 13
        df_ml_mala['codigo'].iloc[0] = ultimo_cod_param_item
        dados_grp_itens.append([ultimo_cod_param_item,'ML',int(cod_precificacao)])
        ultimo_cod_param_item = ultimo_cod_param_item +1
        df = pd.concat([df,df_ml_mala],ignore_index=True)

    if df_ml_mon['qnt'].iloc[0] > 0 and df_ml_mon['cod_item'].iloc[0] == True:
       #cod_item = bf.read_gbq_query('select t1.codigo from electric-armor-429218-g7.prf_cs.itens t1 where t1.objeto = \''+ str(df_ml_mon['cod_item'].iloc[0]) + '\'')
        df_ml_mon['cod_item'].iloc[0] = 18
        df_ml_mon['codigo'].iloc[0] = ultimo_cod_param_item
        dados_grp_itens.append([ultimo_cod_param_item,'ML',int(cod_precificacao)])
        ultimo_cod_param_item = ultimo_cod_param_item +1
        df = pd.concat([df,df_ml_mon],ignore_index=True)

    if df_ml_pio['qnt'].iloc[0] > 0 and df_ml_pio['cod_item'].iloc[0] == True:
        #cod_item = bf.read_gbq_query('select t1.codigo from electric-armor-429218-g7.prf_cs.itens t1 where t1.objeto = \''+ str(df_ml_pio['cod_item'].iloc[0]) + '\'')
        df_ml_pio['cod_item'].iloc[0] = 14
        df_ml_pio['codigo'].iloc[0] = ultimo_cod_param_item
        dados_grp_itens.append([ultimo_cod_param_item,'ML',int(cod_precificacao)])
        ultimo_cod_param_item = ultimo_cod_param_item +1
        df = pd.concat([df,df_ml_pio],ignore_index=True)

        
    if df_mn['qnt'].iloc[0] > 0 and df_mn['cod_item'].iloc[0] != 'Sem Instalação':
        if df_mn['cod_item'].iloc[0] == 'Eventual':
            df_mn['cod_item'].iloc[0] = 16
        elif df_mn['cod_item'].iloc[0] == 'Recorrente':
            df_mn['cod_item'].iloc[0] = 20
        else: df_mn['cod_item'].iloc[0] = None
        df_mn['codigo'].iloc[0] = ultimo_cod_param_item
        dados_grp_itens.append([ultimo_cod_param_item,'MN',int(cod_precificacao)])
        ultimo_cod_param_item = ultimo_cod_param_item +1
        df = pd.concat([df,df_mn],ignore_index=True)
        
    if df_mo['qnt'].iloc[0] > 0 and df_mo['cod_item'].iloc[0] == True:
        df_mo['cod_item'].iloc[0] = 17
        df_mo['codigo'].iloc[0] = ultimo_cod_param_item
        dados_grp_itens.append([ultimo_cod_param_item,'MO',int(cod_precificacao)])
        ultimo_cod_param_item = ultimo_cod_param_item +1
        df = pd.concat([df,df_mo],ignore_index=True)

    df_itens = pd.read_csv(file_name, sep=';')

    df_itens = pd.concat([df_itens,df],ignore_index=True)

    df_ordenado = df_itens.sort_values(by='codigo', ascending=True)

    df_ordenado.to_csv(file_name, header=True,sep=';',index=False)
    
    df_grp_itens = pd.DataFrame(dados_grp_itens,columns=['cod_param_item','cod_grupo','cod_precificacao'])
    #df_grp_itens['cod_param_item'] = pd.to_numeric(df_grp_itens['cod_param_item'], errors='coerce')
    df_grp_itens['cod_param_item'] = df_grp_itens['cod_param_item'].astype(str)
    __assossiaGrpItemDataFile(df_grp_itens)
    __geraLogPrecificacaoDataFile(cod_precificacao,'I','A')
    print("Itens gravado com sucesso!")

def editaItensPrecificacaoDataFile(df_ma, df_ml,df_mn,df_mo,df_ml_eth,df_ml_inv,df_ml_mala,df_ml_mon,df_ml_pio,df_ml_ptch,file_name,cod_precificacao):
    #pram_item
    df_item = pd.read_csv(file_name,sep=';')

    #recupera grupos para atualização
    df_grp_item = pd.read_csv('data/grp_itens_prf.csv',sep=';')
    
    #remover os grupos de itens que foram alterados
    df_grp_item = df_grp_item.query("cod_precificacao not in @cod_precificacao")
    
    df_grp_item.to_csv('data/grp_itens_prf.csv',sep=';', index=False)
    
    
    #removendo itens que foram alterados
    df_item = df_item[df_item.codigo != df_ma['cod_param_item'].iloc[0]]
    df_item = df_item[df_item.codigo != df_ml['cod_param_item'].iloc[0]]
    df_item = df_item[df_item.codigo != df_ml_ptch['cod_param_item'].iloc[0]]
    df_item = df_item[df_item.codigo != df_ml_eth['cod_param_item'].iloc[0]]
    df_item = df_item[df_item.codigo != df_ml_inv['cod_param_item'].iloc[0]]
    df_item = df_item[df_item.codigo != df_ml_mala['cod_param_item'].iloc[0]]
    df_item = df_item[df_item.codigo != df_ml_mon['cod_param_item'].iloc[0]]
    df_item = df_item[df_item.codigo != df_ml_pio['cod_param_item'].iloc[0]]
    df_item = df_item[df_item.codigo != df_mn['cod_param_item'].iloc[0]]
    df_item = df_item[df_item.codigo != df_mo['cod_param_item'].iloc[0]]

    #atualizando a base de dados com os novos itens
    df_item.to_csv(file_name,sep=';', index=False)

    #removendo param_itens
    df_ma.drop(columns=['cod_param_item'],axis=0,inplace=True)
    df_ml.drop(columns=['cod_param_item'],axis=0,inplace=True)
    df_ml_ptch.drop(columns=['cod_param_item'],axis=0,inplace=True)
    df_ml_eth.drop(columns=['cod_param_item'],axis=0,inplace=True)
    df_ml_inv.drop(columns=['cod_param_item'],axis=0,inplace=True)
    df_ml_mala.drop(columns=['cod_param_item'],axis=0,inplace=True)
    df_ml_mon.drop(columns=['cod_param_item'],axis=0,inplace=True)
    df_ml_pio.drop(columns=['cod_param_item'],axis=0,inplace=True)
    df_mn.drop(columns=['cod_param_item'],axis=0,inplace=True)
    df_mo.drop(columns=['cod_param_item'],axis=0,inplace=True)
    

    __geraLogPrecificacaoDataFile(cod_precificacao,'E','A')
    gravaItensPrecificacaoDataFile(df_ma, df_ml,df_mn,df_mo,df_ml_eth,df_ml_inv,df_ml_mala,df_ml_mon,df_ml_pio,df_ml_ptch,file_name,cod_precificacao)
    print("Itens gravado com sucesso!")

def __assossiaGrpItemDataFile(df):
    df_grp_itens = pd.read_csv('data/grp_itens_prf.csv', sep=';')

    df_grp_itens = pd.concat([df_grp_itens,df],ignore_index=True)
    df_grp_itens['cod_param_item'] = df_grp_itens['cod_param_item'].astype(str)

    df_ordenado = df_grp_itens.sort_values(by='cod_param_item', ascending=True)
    print(df_ordenado.dtypes)
    
    df_ordenado.to_csv('data/grp_itens_prf.csv',header=True,sep=';',index=False)
    print("Grupo Itens gravado com sucesso!")



def __geraLogPrecificacaoDataFile(cod_precificacao,acao,status):
    data_atual = datetime.today()
    dt_atual_str = data_atual.strftime('%d/%m/%y %H:%M:%S')
    print(int(cod_precificacao))
    log_data = [[int(cod_precificacao),acao,status,dt_atual_str,dt_atual_str]]
    
    df_log = pd.DataFrame(data=log_data,columns=['cod_precificacao','acao','status','dt_ultima_atualizacao','dt_criacao'])

    df_log_anteriores = pd.read_csv('data/log_precificacao.csv', sep=';')

    df_log_anteriores = pd.concat([df_log_anteriores,df_log],ignore_index=True)

    df_log_anteriores.to_csv('data/log_precificacao.csv',header=True,sep=';',index=False)
    print("Log gravado com sucesso!")

