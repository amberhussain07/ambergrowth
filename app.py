#streamlit

import streamlit as st

st.set_page_config(page_title= "growth mindset project", project_icon="★")
st.title("Growth mindset Chanllenge: Web App with Streamlit")

st.header("🚀 Welcome to Your Growth Journey!")
st.write("The **Growth Mindset Challenge Journey** is a transformative experience designed to cultivate resilience, adaptability, and continuous learning. Through daily challenges and reflections, participants embrace failures as learning opportunities, reframe setbacks as stepping stones, and develop a mindset that fuels personal and professional growth. This journey empowers individuals to unlock their full potential by fostering curiosity, perseverance, and a positive outlook on challenges. 🚀")

#quote section
st.header("💡Today's Growth Mindset Quote")
st.write("Success is not final, failure is not total: it is the courage to continue that count.-Wiston Churchill!")

st.header(" 🎯What's your Challenge Today?")
user_input = st.text_input("describe a Challenge you're facing:")

#condition
if user_input:
      st.success(f"💪Your re facing: {user_input}. keep pushing forward toward your goals! 🚀")
else:
      st.warning("Tell us about your challenge to get started")

      #reflection
      st.header("Reflection on your Learning")
      reflection = st.text_input("Write your reflection here:")

      if reflection:
            st.success(f"✨Great Insight! Your reflection: {reflection}")
      else:
            st.info("reflection on past experience help you grow! Share your difficulties")

      #achivment
      st.header("🏆 Celebrate Your Wins!")    
      achivment = st.text_input("Share you've recently accomplished:")

      if achivment:
            st.success(f"💫 Amazing! you achieved:{achivment}")
      else:
            st.info("Big or small , every achivment count! Share one now 😍")

       #footer
            st.write("---")
            st.write("🚀 Keep believing in youself. Growth is a journey not a destination!🌟")
            st.write("**⛔ Created by Amber Iqbal**")
               
       
       
     
             

            

