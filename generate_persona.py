import re, json, time, os
from dotenv import load_dotenv
import google.generativeai as genai
from persona_prompts import (
    BASE_INFORMATION_PROMPT,
    BEHAVIOR_PATTERN_PROMPT,
    VALUES_INTERESTS_PROMPT,
    CHALLENGES_GOALS_PROMPT
)
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def extract_json(text):
    match = re.search(r'\{.*?\}', text, re.DOTALL)
    if match:
        return match.group(0)
    else:
        return None

persona_file_path = "/Users/shibayuusaku/Downloads/PersonaReviewApp/filtered_persona.jsonl"
full_persona_file_path = "/Users/shibayuusaku/Downloads/PersonaReviewApp/full_persona.jsonl"

with open(persona_file_path, "r", encoding='utf-8') as persona_file, open(full_persona_file_path, "a+", encoding='utf-8') as full_persona_file:
    persona_lines = [json.loads(l) for l in persona_file.readlines()]
    start_index = len([json.loads(l) for l in full_persona_file.readlines()])
    for persona_line in persona_lines[420:]:
        print(persona_line)
        job = persona_line["persona"]
        base_word = f"job={job}の人になりきったつもりで、以下の質問に答えてください。個人情報などの質問についてはjobから予測される内容を生成し、その際、多様性を考慮してください。\n"
        base_information_prompt = base_word + BASE_INFORMATION_PROMPT
        behavior_pattern_prompt = base_word + BEHAVIOR_PATTERN_PROMPT
        values_interests_prompt = base_word + VALUES_INTERESTS_PROMPT
        challenges_goals_prompt = base_word + CHALLENGES_GOALS_PROMPT
        full_persona_dict = {"job": job}
        generate_persona_flag = True
        while generate_persona_flag:
            try:
                print("実行中")
                base_information_response = model.generate_content(base_information_prompt)
                time.sleep(10)
                behavior_pattern_response = model.generate_content(behavior_pattern_prompt)
                time.sleep(10)
                values_interests_response = model.generate_content(values_interests_prompt)
                time.sleep(10)
                challenges_goals_response = model.generate_content(challenges_goals_prompt)

                base_information_text = extract_json(base_information_response.text)
                behavior_pattern_text = extract_json(behavior_pattern_response.text)
                values_interests_text = extract_json(values_interests_response.text)
                challenges_goals_text = extract_json(challenges_goals_response.text)

                if not (base_information_text and behavior_pattern_text and values_interests_text and challenges_goals_text):
                    raise ValueError("One or more responses did not contain valid JSON.")

                base_information_dict = json.loads(base_information_text)
                behavior_pattern_dict = json.loads(behavior_pattern_text)
                values_interests_dict = json.loads(values_interests_text)
                challenges_goals_dict = json.loads(challenges_goals_text)

            except json.decoder.JSONDecodeError as e:
                print("Error decoding JSON:", e)
            except ValueError as e:
                print("Error:", e)
            #except genai.GenerativeAIError as e: #ここをどうにかしないと動かない attributeerror
            #    time.sleep(30)
            #    print("Error generating content:", e)
            except Exception as e:
                print("An unexpected error occurred:", e)
            else:
                full_persona_dict.update(base_information_dict)
                full_persona_dict.update(behavior_pattern_dict)
                full_persona_dict.update(values_interests_dict)
                full_persona_dict.update(challenges_goals_dict)
                full_persona_file.write(json.dumps(full_persona_dict, ensure_ascii=False) + '\n')
                time.sleep(5)
                break

persona_file.close()

"""
# persona.jsonlの前処理用コード
def contains_kanji(text):
    # テキストに漢字が含まれているかどうかを判断する関数
    return bool(re.search(r'[\u4e00-\u9fff]', text))

count = 0

with open("/Users/shibayuusaku/Downloads/PersonaReviewApp/persona.jsonl", "r", encoding='utf-8') as f1:
    with open("/Users/shibayuusaku/Downloads/PersonaReviewApp/filtered_persona.jsonl", "w", encoding='utf-8') as f2:
        for line in f1:
            data = json.loads(line)
            filtered_data = {}

            for key, value in data.items():
                if isinstance(value, str):
                    if contains_kanji(value):
                        count += 1
                    else:
                        filtered_data[key] = value
                        if len(value.split(" ")) > 5:
                            f2.write(json.dumps(filtered_data, ensure_ascii=False) + '\n')
                        else:
                            count += 1
                else:
                    count += 1
print(count)
"""