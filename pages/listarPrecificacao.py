
#demo streamlit by https://www.datacamp.com/tutorial/streamlit?utm_source=google&utm_medium=paid_search&utm_campaignid=21374847033&utm_adgroupid=165153430282&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=720328391448&utm_targetid=aud-1940143831083:dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=1001566&utm_content=&utm_campaign=240617_1-sea~dsa~tofu_2-b2c_3-ptbr-lang-en_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na-bfcm24&gad_source=1&gclid=Cj0KCQiAr7C6BhDRARIsAOUKifjOv4Ea9wOMGJAsJy9QIcq2dLhHTsJESmobWhFI0qQVpfsysL0yZyUaAss9EALw_wcB

import pandas as pd
import streamlit as st
import numpy as np
import altair as alt



with st.container():    
    st.write("Aguardando aprovação:")

    #df = pd.DataFrame(np.random.randn(10, 2), columns=['Contratante', 'UF'])
    df = pd.DataFrame(
        {
            "name": ["1° BATALHAO DE ENGENHARIA", "TRIBUNAL DE JUSTIÇA DO MARANHÃO", "DEFENSORIA PUBLICA DA BAHIA"],
            "uf": ["MS", "MA", "BA"],
            "status": ["Em Precificacao", "Em Revisão", "Em Precificação"],
            "url": ["https://extras.streamlit.app", "https://extras.streamlit.app", "https://extras.streamlit.app"]
        }
    )
    st.dataframe(
        df,
        column_config={
            "name": "Contratante",
            "uf": "UF",
            "status": "Status",
            "url": st.column_config.LinkColumn("Modificar")
        },
        hide_index=True,
    )
    #st.table(df)


