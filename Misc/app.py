import gradio as gr
import streamlit as st

api_key = "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"
# gr.Interface.load("models/harithapliyal/autotrain-titanic-survival-50974121235", api_key=api_key).launch()

def sketch_recognition(img):
    
    return 3**3
    
gr.Interface(fn=sketch_recognition, inputs="sketchpad", outputs="label")

a=st.text()
b=st.checkbox("I Agree")