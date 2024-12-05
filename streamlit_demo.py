
#demo streamlit by https://www.datacamp.com/tutorial/streamlit?utm_source=google&utm_medium=paid_search&utm_campaignid=21374847033&utm_adgroupid=165153430282&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=720328391448&utm_targetid=aud-1940143831083:dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=1001566&utm_content=&utm_campaign=240617_1-sea~dsa~tofu_2-b2c_3-ptbr-lang-en_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na-bfcm24&gad_source=1&gclid=Cj0KCQiAr7C6BhDRARIsAOUKifjOv4Ea9wOMGJAsJy9QIcq2dLhHTsJESmobWhFI0qQVpfsysL0yZyUaAss9EALw_wcB

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import graphviz
import pickle  # to load a saved modelimport base64  # to handle gif encoding

st.title("This is the app title")
st.header("This is the header")
st.markdown("This is the markdown")
st.subheader("This is the subheader")
st.caption("This is the caption")
st.code("x = 2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.checkbox('Yes')
st.button('Click Me')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick a fruit', ['Apple', 'Banana', 'Orange'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)

st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Traveling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

st.balloons()  # Celebration balloonsst.progress(10)  # Progress barwith st.spinner('Wait for it...'):    time.sleep(10)  # Simulating a process delay

st.success("You did it!")
st.error("Error occurred")
st.warning("This is a warning")
st.info("It's easy to build a Streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

st.sidebar.title("Sidebar Title")
st.sidebar.markdown("This is the sidebar content")
st.sidebar.radio('Pick gender', ['Male', 'Female'])
st.sidebar.button('Me')
st.sidebar.selectbox('A fruit', ['Apple', 'Banana', 'Orange'])
st.sidebar.multiselect('A planet', ['Jupiter', 'Mars', 'Neptune'])
st.sidebar.select_slider('A mark', ['Bad', 'Good', 'Excellent'])


with st.container():    
    st.write("This is inside the container")
    st.write("This is inside the container2")

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.area_chart(df)

df = pd.DataFrame(np.random.randn(500, 3), columns=['x', 'y', 'z'])
chart = alt.Chart(df).mark_circle().encode(    x='x', y='y', size='z', color='z', tooltip=['x', 'y', 'z'])
st.altair_chart(chart, use_container_width=True)

st.graphviz_chart('''    digraph {        Big_shark -> Tuna        Tuna -> Mackerel        Mackerel -> Small_fishes        Small_fishes -> Shrimp    }''')

df = pd.DataFrame(    np.random.randn(500, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(df)


