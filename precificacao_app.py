
#demo streamlit by https://www.datacamp.com/tutorial/streamlit?utm_source=google&utm_medium=paid_search&utm_campaignid=21374847033&utm_adgroupid=165153430282&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=720328391448&utm_targetid=aud-1940143831083:dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=1001566&utm_content=&utm_campaign=240617_1-sea~dsa~tofu_2-b2c_3-ptbr-lang-en_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na-bfcm24&gad_source=1&gclid=Cj0KCQiAr7C6BhDRARIsAOUKifjOv4Ea9wOMGJAsJy9QIcq2dLhHTsJESmobWhFI0qQVpfsysL0yZyUaAss9EALw_wcB

import streamlit as st


st.set_page_config(page_title="Page Title", layout="wide")

st.markdown(
    """
    <style>
    .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("App Precificações Pulsar")

st.sidebar.title("Precificação")
st.sidebar.page_link("pages/cadastrarPrecificacao.py", label="Cadastrar")
st.sidebar.page_link("pages/editarPrecificacao.py", label="Editar")
st.sidebar.page_link("pages/listarPrecificacao.py", label="Listar")
st.sidebar.page_link("https://lookerstudio.google.com/reporting/1f5d63fc-8e2b-473b-a96d-66c23f64cdf2/page/CbJ9D", label="Looker")




