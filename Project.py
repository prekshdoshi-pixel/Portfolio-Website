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
        st.subheader('Robotics | Embedded Systems | AI | 3D Printing')
        st.write('''
        I am passionate about Robotics, Embedded Systems, 
        Articifial Intellegence and Product Development.
        I enjoy building innovative projects that combine 
        hardware and software to solve real world problems.
        ''')
#About Me Page
elif page == 'About Me':
    st.title('About Me')
    st.write('''
    I am an M.sc. Computer Science student with a strong interest
    in Robotics, Embedded Systems, Machine Learning and IoT.
    I have conducted robotics workshops, developed embedded
    systems projects and worked on AI based solutions.
    ''')
    st.subheader('Education')
    st.write('''
    - M.Sc. Computer Science
    - Experience in Python, ESP32, Arduino, ML and CAD Design
    ''')
#Projects Page
elif page == 'Projects':
    st.title('My Projects')
    projects = [
        {
            'name': 'Proxiglow',
            'desc': 'Wearable Safety Device using ESP32'
        },
        {
            'name': 'Pathfinder',
            'desc': 'Smart Cane for visually impaired individuals'
        }
    ]
    for project in projects:
        st.subheader(project['name'])
        st.write(project['desc'])
        st.divider()
#Skill Page
elif page == 'Skills':
    st.title('Skills')
    st.subheader('Programming')
    st.progress(90)
    st.write('Python, C++, Arduino')
    st.subheader('Embedded Systems')
    st.progress(85)
    st.subheader('Machine Learning')
    st.progress(80)
    st.subheader('CAD & 3D Printing')
    st.progress(75)
#Contact Page
elif page == 'Contact':
    st.title('Contact Me')
    st.write('📧Email: prekshdoshi@gmail.com')
    st.write('🔗Linkedin: https://linkedin.com/in/yourprofile')
    st.write('💻GitHub: https://github.com/yourusername')
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