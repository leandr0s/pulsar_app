import math

def calculaCstoFinanceiro(tx_ctso_financeiro,vigencia,csto_hardware):
   investimento = float(csto_hardware)
   tjurospercentagem = float(tx_ctso_financeiro)
   tjuro=tjurospercentagem/100
   meses = int(vigencia)
   varfuturo= investimento*(1+tjuro*meses)
   jurototal = investimento*tjuro*meses
   juromes =investimento*tjuro
   vlr_parcela = (jurototal+csto_hardware)/vigencia
   print('\n\n\t\t O valor futuro é de {:.2f}'.format(varfuturo))
   print('\n\n\t\t O valor da parcela é de {:.2f}'.format(vlr_parcela))
   print('\n\t\t Os juros totais é de {:.2f}'.format(jurototal))
   print('\n\t\t Os juros ao ano é de {:.2f}'.format(juromes))
   
   return juromes