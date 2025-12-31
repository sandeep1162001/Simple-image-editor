import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown('<h1 style="text-align: center;">Image editor</h1>',unsafe_allow_html=True)
st.markdown('---')
image=st.file_uploader("Please upload image to edit",type=['png','jpg','jpeg'])
info = st.empty()
size = st.empty()
format = st.empty()
mode = st.empty()
if image:
    img=Image.open(image)
    info.markdown('<h2 style="text-align: center;">Image information</h2>',unsafe_allow_html=True)
    size.markdown(f'<h6> Size : {img.size}</h6>',unsafe_allow_html=True)
    format.markdown(f'<h6> Format : {img.format}</h6>',unsafe_allow_html=True)
    mode.markdown(f'<h6> Mode : {img.mode}</h6>',unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center;">Resize</h2>',unsafe_allow_html=True)
    width=st.number_input("Width",value=img.width)
    height=st.number_input("height",value=img.height)
    st.markdown('<h2 style="text-align: center;">Rotate</h2>',unsafe_allow_html=True)
    degree=st.number_input("Rotate")
    st.markdown('<h2 style="text-align: center;">Filter</h2>',unsafe_allow_html=True)
    filter=st.selectbox("Filter",options=["None","BLUR","CONTOUR","DETAIL","EDGE_ENHANCE","EMBOSS","FIND_EDGES","SHARPEN","SMOOTH","SMOOTH_MORE"])
    s_btn=st.button("Submit")
    if s_btn:
        edited = img.resize((width,height)).rotate(degree)
        filtered=edited
        if filter !="None":
            if filter=="BLUR":
                filtered=edited.filter(BLUR)
            elif filter =="CONTOUR":
                filtered=edited.filter(CONTOUR)
            elif filter =="DETAIL":
                filtered=edited.filter(DETAIL)
            elif filter =="EDGE_ENHANCE":
                filtered=edited.filter(EDGE_ENHANCE)
            elif filter =="EMBOSS":
                filtered=edited.filter(EMBOSS)
            elif filter =="FIND_EDGES":
                filtered=edited.filter(FIND_EDGES)
            elif filter =="SHARPEN":
                filtered=edited.filter(SHARPEN)
            elif filter =="SMOOTH":
                filtered=edited.filter(SMOOTH)
            else:
                filtered=edited.filter(SMOOTH_MORE)

        st.image(filtered)

