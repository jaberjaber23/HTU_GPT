import streamlit as st 
import openai 
import os 
from PIL import Image 

# Set the OpenAI API key 
os.environ["OPENAI_API_KEY"] = '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' 
openai.api_key = os.environ["OPENAI_API_KEY"] 

# Set page configuration
st.set_page_config(
    page_title="HTUGPT", 
    page_icon="🤖", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Load image
img = Image.open("C:/Users/yazan/rock-paper-scissors/rock_paperr_scissor/openai/5.png") 

# Display the image
st.image(img, width=150)

# Add a title and set the font size and color
st.markdown("<h1 style='text-align: center; font-size: 80px;'><span style='color: red;'>HTU</span><span style='color: white;'>GPT</span></h1>", unsafe_allow_html=True)

# Set the font and background color of the website
st.markdown( """ 
    <style> 
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            background-color: #F8F8F8;
            font-size: 28px;
            direction: rtl;
        } 
    </style> 
""", unsafe_allow_html=True)

# Define a function to generate an article from a given keyword
def generate_article(keyword):
    with st.spinner('...جارٍ توليد الرد'):
        response = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=keyword, 
            max_tokens=2048, 
            n=1, 
            stop=None, 
            temperature=0.7
        )
        message = response.choices[0].text.strip()
    return message 

# Add a text input and a slider to the website
keyword = st.text_input("الموضوع", )
word_count = st.slider("عدد الكلمات", min_value=20, max_value=1000, value=300)

# Add a submit button to the website
submit_button = st.button("!إرسال الطلب")

# Generate an article when the submit button is clicked
if submit_button:
    message = st.empty()
    article = generate_article(keyword)
    
    # Set the font size of the article and add some padding
    st.write(f"<p style='font-size: 34px; padding: 29px;'>{article}</p>", unsafe_allow_html=True)
    
    # Add a download button to download the article as a text file
    st.download_button(label='تحميل المقالة', data=article, file_name='article.txt', mime='text/plain')
