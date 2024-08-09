import pandas as pd
import streamlit as st
import json
from functions_for_analysis import count_gender, count_age, calculate_analogy, plot_similarity_heatmap

full_persona_file_path = "./full_persona.jsonl"

personas_dict = {
    "age": [],
    "gender": [],
    "address": [],
    "education_level": [],
    "family": [],
    "salary": [],
    "health": [],
    "daily_routine": [],
    "purchasing_behavior": [],
    "internet_usage": [],
    "hobbies": [],
    "interests": [],
    "values": [],
    "lifestyle": [],
    "tech_proficiency": [],
    "cultural_background": [],
    "current_challenges": [],
    "goals": [],
    "needs": []
}

key_ls = [
    "age", "gender", "address", "education_level", "family", 
    "salary", "health", "daily_routine", "purchasing_behavior", 
    "internet_usage", "hobbies", "interests", "values", 
    "lifestyle", "tech_proficiency", "cultural_background", 
    "current_challenges", "goals", "needs"
]
persona_lines = []
with open(full_persona_file_path, "r", encoding='utf-8') as full_persona_file:
    persona_lines = [json.loads(l) for l in full_persona_file.readlines()]
    for persona_line in persona_lines[:3]:
        for key in key_ls:
            personas_dict[key].append(persona_line[key])

st.header('ペルソナ一覧')
st.data_editor(pd.DataFrame(personas_dict))

st.header('性別')
st.data_editor(pd.DataFrame(count_gender(personas_dict["gender"]), index = [""]))

st.header("年齢")
st.data_editor(pd.DataFrame(count_age(personas_dict["age"]), index = [""]))

st.header("文章類似度")
radio_options = [
    "address", "education_level", "family", 
    "salary", "health", "daily_routine", "purchasing_behavior", 
    "internet_usage", "hobbies", "interests", "values", 
    "lifestyle", "tech_proficiency", "cultural_background", 
    "current_challenges", "goals", "needs"
]
radio_option = st.radio(label="パラメータを選択", options=radio_options, index=1, horizontal=True, label_visibility="visible")
similarity = calculate_analogy(personas_dict[radio_option])
st.pyplot(plot_similarity_heatmap(similarity))