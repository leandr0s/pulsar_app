import enum

class Entidade(enum.Enum):
    PRECIFICACAO = 1
    PARAM_ITENS = 2
    LOG = 3
    GRP_ITEM = 4

# Using enum as keys in a dictionary
file_name = {
    Entidade.PRECIFICACAO: 'precificacao99.csv',
    Entidade.PARAM_ITENS: 'param_itens99.csv',
    Entidade.LOG: 'log_precificacao99.csv',
    Entidade.GRP_ITEM: 'grp_itens_prf99.csv'

}

table_name = {
    Entidade.PRECIFICACAO: 'prf_cs.precificacao',
    Entidade.PARAM_ITENS: 'prf_cs.param_itens',
    Entidade.LOG: 'prf_cs.log_precificacao',
    Entidade.GRP_ITEM: 'prf_cs.grp_itens_prf'
}
print(table_name[Entidade.PRECIFICACAO])  # Output: 'Meeting'