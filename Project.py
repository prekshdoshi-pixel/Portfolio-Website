import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
#Page configuration
st.set_page_config(
    page_title='Preksh Portfolio',
    layout='wide'
)
#Sidebar
page = st.sidebar.radio(
    'Navigation',
    ['Home', 'About Me', 'Projects', 'Skills', 'Contact']
)
#Home Page
if page == 'Home':
    st.title('Welcome to My Portfolio')
    col1, col2 = st.columns([1,2])
    with col1:
        st.image(
            image = Image.open('Preksh_Picture.png'),
            caption='My Photo'
        )
    with col2:
        st.header('Preksh Doshi')
        st.subheader('Leaner | Observer | Coding')
        st.write('''
        I am a dedicated and enthusiastic student who enjoys 
        learning and participating in different activities. 
        I am interested in creativity, technology, and collaborative work. 
        I like taking on new challenges and continuously improving my skills 
        while maintaining a positive attitude. I enjoy building innovative 
        projects that are software to solve real world problems.
        ''')
#About Me Page
elif page == 'About Me':
    st.title('About Me')
    st.write('''
    I am an student in JBCN Internaitonal School with a strong interest
    in Computer Science, Artficial Intellegence and Finance.
    ''')
    st.subheader('Education')
    st.write('''
    - Pursuing IGCSE Certification
    - Experience in Python
    ''')
#Projects Page
elif page == 'Projects':
    st.title('My Projects')
    projects = [
        {
            'name': 'Preksh Portfilio',
            'desc': 'A personal portfolio website built to showcase my projects, creativity, skills, and achievements through a modern and interactive digital experience.'
        },
    ]
    for project in projects:
        st.subheader(project['name'])
        st.write(project['desc'])
#Skill Page
elif page == 'Skills':
    st.title('Skills')
    st.subheader('Programming')
    st.progress(40)
    st.write('Python')
#Contact Page
elif page == 'Contact':
    st.title('Contact Me')
    st.write('📧Email: prekshdoshi@gmail.com')
    st.write('🔗Linkedin: https://linkedin.com/in/yourprofile')
    st.write('💻GitHub: https://github.com/prekshdoshi-pixel')
    st.subheader('Send a Message')
    name = st.text_input('Name')
    email = st.text_input('Email')
    message = st.text_area('Message')
    if st.button('Send'):
        st.success(
            f'Thank you {name}! Your message has been recieved'
        )
#Footer
st.markdown('---')
st.caption('© 2026 Preksh Doshi')