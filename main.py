import os
from datetime import datetime

import streamlit as st
import requests

apikey = "CJLpUIJ1j07ueap7qPOE6AZmX68NaRAmVVzYZVZ8"
url = f"https://api.nasa.gov/planetary/apod?api_key={apikey}"

def refresh_aid(current_date):
    if not os.path.exists(f"images/img-{current_date}.jpg"):
        json = requests.get(url).json()
        imgUrl = json["url"]
        date = json['date']

        response = requests.get(imgUrl)
        img = response.content
        with open(f"images/img-{date}.jpg", "wb") as f1:
            f1.write(img)
    if not os.path.exists(f"text-data/explanation-{current_date}.txt"):
        with open(f"text-data/explanation-{current_date}.txt", "w") as f1:
            f1.write(requests.get(url).json()["explanation"])


current_date = datetime.now().strftime("%Y-%m-%d")

refresh_aid(current_date)

st.set_page_config(layout='wide')
col1 = st.columns(1)[0]


with col1:
    st.title("Astrology image of the day")
    st.image("images/img.jpg")
    with open(f"text-data/explanation-{current_date}.txt") as f:
        st.info(f.read())
    st.button("Refresh image")
    if st:
        refresh_aid(current_date)



