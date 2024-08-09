from flask import Flask, render_template, url_for, request, send_file
import json, random, time
from io import BytesIO
from generate_review import Persona
import pandas as pd


"""
レビュー用プロンプト改善（出力フォーマット作る）・日本用ペルソナ生成・PDF書き込みコード・エラーハンドリング
"""
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/middle", methods=['GET', 'POST'])
def middle():
    if request.method == 'POST':
        if request.referrer.split('/')[-1] == "":
            service_title = request.form.get('service_title')
            service_content = request.form.get('service_content')
            service_dict = {"title": service_title, "content": service_content}

            with open("./full_persona.jsonl", "r", encoding="utf-8") as f1:
                persona_dicts = [json.loads(l) for l in f1.readlines()]
                job_ls = []
                age_ls = []
                review_ls = []
                random.shuffle(persona_dicts)
                persona_dict = persona_dicts[0]
                generate_persona_flag = True
                while generate_persona_flag:
                    try:
                        persona = Persona(persona_dict)
                        review = persona.generate_positive_review(service_title, service_content)
                        #time.sleep(16)
                        job_ls.append(persona_dict["job"])
                        age_ls.append(persona_dict["age"])
                        review_ls.append(review)
                        data_dict = {"job": job_ls, "age": age_ls, "review": review_ls}
                        generate_persona_flag = False
                    except Exception as e:
                        print(e)
                        return "エラー発生" #ここでエラー用のページを作る
                    
        elif request.referrer.split('/')[-1] == "middle":
            service_dict = json.loads(request.form.get('service_dict').replace("'", '"'))
            print(f"'リクエスト部分〜〜〜〜〜〜〜〜〜〜'{service_dict}")
            print(f"'リクエスト部分〜〜〜〜〜〜〜〜〜〜'{type(service_dict)}")
            service_title = service_dict["title"]
            service_title = service_dict["title"]
            service_content = service_dict["content"]
            service_dict = {"title": service_title, "content": service_content}
            with open("./full_persona.jsonl", "r", encoding="utf-8") as f1:
                persona_dicts = [json.loads(l) for l in f1.readlines()]
                job_ls = []
                age_ls = []
                review_ls = []
                random.shuffle(persona_dicts)
                persona_dict = persona_dicts[0]
                generate_persona_flag = True
                while generate_persona_flag:
                    try:
                        persona = Persona(persona_dict)
                        review = persona.generate_positive_review(service_title, service_content)
                        #time.sleep(16)
                        job_ls.append(persona_dict["job"])
                        age_ls.append(persona_dict["age"])
                        review_ls.append(review)
                        data_dict = {"job": job_ls, "age": age_ls, "review": review_ls}
                        generate_persona_flag = False
                    except Exception as e:
                        print(e)
                        return "エラー発生" #ここでエラー用のページを作る
                    
        return render_template("middle.html", job_ls=job_ls, age_ls=age_ls, review_ls=review_ls, data_dict=data_dict, service_dict=service_dict)
    else:
        return "情報ない"

@app.route('/output', methods=['GET', 'POST'])
def output():
    if request.method == 'POST':
        # フォームデータの取得
        service_title = request.form.get('service_title')
        service_content = request.form.get('service_content')

        with open("./full_persona.jsonl", "r", encoding="utf-8") as f1:
            data_json_str = request.form.get('data').replace("'", '"')
            data_json = json.loads(data_json_str)
            job_ls = data_json["job"]
            age_ls = data_json["age"]
            review_ls = data_json["review"]
            df = pd.DataFrame({'職業': job_ls, '年齢': age_ls, 'レビュー': review_ls})
                # メモリ上でExcelファイルを作成
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='商品レビュー')
            output.seek(0)
            
        return send_file(output,
                             download_name='product_review.xlsx',
                             as_attachment=True,
                             mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    else:
        return "This is the output page. Use the form to submit data."


if __name__ == "__main__":
    app.run(debug=True)