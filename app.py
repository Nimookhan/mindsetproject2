import streamlit as st import random import time from streamlit_extras.let_it_rain import rain from streamlit_extras.animated_text import animated_text from streamlit_extras.badges import badge from PIL import Image

App Title

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌟", layout="wide")

Custom CSS for animations and colors

st.markdown( """ <style> body { background-color: #1e1e2f; color: white; } .challenge-box { border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #ff9a9e, #fad0c4); color: black; text-align: center; font-size: 24px; font-weight: bold; animation: fadeIn 2s ease-in-out; } @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } } </style> """, unsafe_allow_html=True, )

Growth Mindset Challenges

challenges = [ "🚀 Accept failures as learning steps!", "🎯 Try something new and embrace the challenge!", "💡 Seek feedback and grow from it!", "🔥 Turn 'I can't' into 'I can with effort'!", "🌟 Learn from someone you admire today!", "💖 Practice gratitude and stay positive!", "🌍 Push beyond your comfort zone today!", ]

Header Section

st.title("🌈 Growth Mindset Challenge") animated_text("Develop a powerful mindset with daily challenges! ✨")

Display Random Challenge

if st.button("🔮 Get Today's Challenge"): challenge = random.choice(challenges) st.markdown(f'<div class="challenge-box">{challenge}</div>', unsafe_allow_html=True) rain(emoji="🌟", font_size=30, falling_speed=3, animation_length=2)

Footer with Badge

st.markdown("---") st.write("Made with ❤️ using Streamlit") badge(type="github", name="YourGitHubUsername", url="https://github.com/YourGitHubUsername")
