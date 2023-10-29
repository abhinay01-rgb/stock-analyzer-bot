import streamlit as st
import tools
from tools.fetch_stock_info import Anazlyze_stock
import streamlit as st
from PIL import Image




st.write('''<style>
"<style>.st-emotion-cache-1v0mbdj.e115fcil1 {
    max-width: 200px;
    display: flex;
} </style>''', unsafe_allow_html=True)
image = Image.open('photo1.jpeg')
new_image = image.resize((400, 200))
st.image(image)
st.title("Stock Analysis bot by iHUB and HCI Foundation IIT MANDI")
st.write("Bot scraps and gathers real time stock realted information and analyzes it using Large Language Model - LLM")

query = st.text_input('Input your investment related query:') 

Enter=st.button("Enter")
clear=st.button("Clear")

if clear:
    print(clear)
    st.markdown(' ')

if Enter:
    import time
    with st.spinner('Gathering all required information and analyzing. Be patient!!!!!'):
        out=Anazlyze_stock(query)
    st.success('Done!')
    st.write(out)


