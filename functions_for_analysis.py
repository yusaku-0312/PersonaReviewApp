import re
import numpy as np
from sentence_transformers import SentenceTransformer, util
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
def count_gender(gender_ls):
    man_count = 0
    woman_count = 0
    others_count = 0
    for gender in gender_ls:
        if "男" in gender and not "女" in gender:
            man_count += 1
        if "女" in gender and not "男" in gender:
            woman_count += 1
        else:
            others_count += 1
    total = man_count + woman_count + others_count
    return {"男": man_count, "女": woman_count, "その他": others_count, "合計": total}

def count_age(age_ls):
    age_ranges = [(0, 9), (10, 19), (20, 29), (30, 39), 
                  (40, 49), (50, 59), (60, 69), (70, 79)]
    age_dict = {f"{start}~{end}歳": 0 for start, end in age_ranges}
    age_dict["80歳以上"] = 0

    for age in age_ls:
        cleaned_age = re.sub(r"\D", "", age)
        if cleaned_age:  # 空文字列でないことを確認
            age = int(cleaned_age)
            for start, end in age_ranges:
                if start <= age <= end:
                    age_dict[f"{start}~{end}歳"] += 1
                    break
            else:
                age_dict["80歳以上"] += 1
    return age_dict

def calculate_analogy(persona_ls):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    num_personas = len(persona_ls)
    similarity_matrix = np.zeros((num_personas, num_personas))

    for i in range(num_personas):
        text1 = persona_ls[i]
        embeddings1 = model.encode(text1, convert_to_tensor=True)
        for j in range(num_personas):
            text2 = persona_ls[j]
            embeddings2 = model.encode(text2, convert_to_tensor=True)
            cosine_score = util.pytorch_cos_sim(embeddings1, embeddings2)[0][0].item()
            similarity_matrix[i, j] = cosine_score
    return similarity_matrix

def plot_similarity_heatmap(similarity_matrix):
    fig, ax = plt.subplots(figsize=(15, 12))
    sns.heatmap(similarity_matrix, cmap='Blues', annot=False, ax=ax)
    return fig