#オブジェクト指向でお願いします。
import google.generativeai as genai
import json, re ,os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def extract_json(text):
    match = re.search(r'\{.*?\}', text, re.DOTALL)
    if match:
        return match.group(0)
    else:
        return None
    
class Persona:
    def __init__(self, persona_dict):
        self.persona_dict = persona_dict
        self.job = persona_dict["job"]
        self.age = persona_dict["age"]
        self.gender = persona_dict["gender"]
        #self.address = persona_dict["address"]
        self.education_level = persona_dict["education_level"]
        self.family = persona_dict["family"]
        self.salary = persona_dict["salary"]
        self.health = persona_dict["health"]
        self.daily_routine = persona_dict["daily_routine"]
        self.purchasing_behavior = persona_dict["purchasing_behavior"]
        self.internet_usage = persona_dict["internet_usage"]
        self.hobbies = persona_dict["hobbies"]
        self.interests = persona_dict["interests"]
        self.values = persona_dict["values"]
        self.lifestyle = persona_dict["lifestyle"]
        self.tech_proficiency = persona_dict["tech_proficiency"]
        self.cultural_background = persona_dict["cultural_background"]
        self.current_challenges = persona_dict["current_challenges"]
        self.goals = persona_dict["goals"]
        self.needs = persona_dict["needs"]
        self.model = genai.GenerativeModel('gemini-1.5-pro')


    def generate_positive_review(self, service_titile, service_content):
        prompt = f"""
        {self.persona_dict}
        これはあなたのペルソナです。あなたは今から{service_titile}というサービスを利用します。サービス内容の詳細は次の通りです。{service_content}
        このサービスを利用した上でのレビューを書いてください。
        あなたのパーソナルデータがあるので、それを参考にしてレビューすることを重視して下さい。使ったときにどう感じるかの感情的な部分からの分析も一部織り込んでください。
        以下はレビューに加える内容とその出力例です。json形式で出力し、キーの内容について書き込んでください。
        です。ます。調で書き、レビューサイトに書き込むような文章にして下さい
        {{"このサービスを使おうと思ったきっかけ": "", "良かった点": "", "悪い点": "", "総評": ""}}
        """
        review = self.model.generate_content(prompt)
        print(review.text)
        review_dict = extract_json(review.text)
        print(review_dict)
        print("-----------------")
        return json.loads(review_dict)

    def generate_negative_review():
        pass

"""
ChatGPTに顧客心理を考えさせたいときは「～～に帰結することが納得できる思考回路を言語化してください」と指示すると良い。
顧客の心の動きをステップごとに言語化してくれるのでマーケティングプランやセールスプランの策定に非常に役に立つ。
"""