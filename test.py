import json, random, time
from generate_review import Persona

with open('./full_persona.jsonl', 'r') as f:

    
        persona_dicts = [json.loads(l) for l in f.readlines()]
        random.shuffle(persona_dicts)
        for i, dict in enumerate(persona_dicts[7:20]):
            with open(f'./reviews_02/review0{i}.txt', 'w') as f2:
                persona = Persona(dict)
                title = "My Carで企業宣伝"
                content = """
                ○サービス概要
                自分の普段乗っている車に企業の宣伝ポスターを貼り付け、普段通り運転してもらいます。走行場所や走行距離に応じて貰える報酬が増えます。
                企業側は低コストで広告を打ち出すことができ、運転者は普段通り運転しながら、お金を稼ぐことができます。
                走っているだけでお金が稼げるので運転しながらガソリン代を稼げるようなものです。
                また、お金を稼ぐことで、自分の車にもアンバインドをしていくことができます。
                ○サービスのメリット
                ・低コストで広告を打ち出すことができます。
                ・運転者は普段通り運転しながら、お金を稼ぐことができます。
                ・自分の車にもアンバインドをしていくことができます。
                """
                review = persona.generate_positive_review( title, content )
                f2.write(review + '\n'*2)
                time.sleep(8)
                print("-"*20)