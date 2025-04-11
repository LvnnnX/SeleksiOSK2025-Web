import streamlit as st

def clear_background():
    """
    Clear the background of the Streamlit app.
    """
    st.markdown(
    """
<style>
[data-testid^="stAppViewContainer"]{
    background-color=black;

}
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
[data-testid^="stFormSubmitButton"] > button:first-child {
    background-color: transparent;
    text-align: center;
    margin: 10;
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
[data-testid^="stFormSubmitButton"]:hover > button:first-child {
    border-color: green;
}

[class^="st-b"]  {
    color: white;
}
[data-testid^="stMarkdownContainer"]{
    background-color: transparent;
    size: 20px;
    color: white;
    weight: bold;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

[class^="main css-k1vhr4 egzxvld3"]{
    background-color:#0e1117;
}

</style>
""",
    unsafe_allow_html=True,
)

def popup_clear_background():
    st.markdown(
    """
<style>
div[data-modal-container='true'][key='Demo key'] > div:first-child > div:first-child{
    background-color:#0e1117;
}
</style>
""", unsafe_allow_html=True)
    
    
def clearfirstOption():
    st.markdown(
        """
    <style>
        div[role=radiogroup] label:first-of-type {
            visibility: hidden;
            height: 0px;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
    
def writeDescription(text: str = '', type:str=None):
    """
    Write a paragraph to the Streamlit app.
    """
    list_to_br = [
        ';','begin','do','then'
    ]
    if type=='Pemrograman':
        for item in list_to_br:
            text = text.replace(item, f'{item}<br>')
        text = text.replace('else', '<br>else<br>')
        
    st.markdown(
        f"""
        <div style="background-color: #000000; padding: 10px; border-radius: 10px; border: 1px solid #2e7bcf;">
            <p style="text-align: justify; font-size: 20px; color: white; padding:-10px">
                {text}
            </p>
        </div>
        
        """,
        unsafe_allow_html=True,
    )
    
def writeQuestion(text: str=''):
    """
    Write a question to the Streamlit app.
    """
    
    
    st.markdown(
        f"""
        <p style="text-align: justify; font-size: 16px; color: white; padding=0px">
            {text}
        </p>
        """,
        unsafe_allow_html=True,
    )