#基本情報 7種
BASE_INFORMATION_PROMPT = f"""
age:あなたは何歳ですか？
gender:あなたの性別は何ですか？男、女、その他から選んでください。
address:あなたはどこに住んでいますか？
education_level:あなたの学歴を教えてください。
family:あなたの家族構成を教えてください。
salary:あなたの給料はどのくらいですか？
health:あなたの今の健康状態について教えてください。
出力形式は以下のフォーマットに合わせ、それ以外の文章は出力しないでください。
{{"age":"", "gender":"", "address":"", "education_level":"", "family":"", "salary":"", "health":""}}
"""

#行動パターン 3種
BEHAVIOR_PATTERN_PROMPT = f"""
daily_routine: あなたの日常生活のルーチンを教えてください。
purchasing_behavior: あなたの購買行動について教えてください。
internet_usage: あなたのインターネットの使用状況を教えてください。
出力形式は以下のフォーマットに合わせ、それ以外の文章は出力しないでください。
{{"daily_routine":"", "purchasing_behavior":"", "internet_usage":""}}
"""

#価値観・興味　６種
VALUES_INTERESTS_PROMPT = f"""
hobbies: あなたの趣味を教えてください。
interests: あなたの関心事について教えてください。
values: あなたの価値観について教えてください。
lifestyle: あなたのライフスタイルについて教えてください。
tech_proficiency: あなたの技術の習熟度について教えてください。
cultural_background: あなたの文化的背景について教えてください。
出力形式は以下のフォーマットに合わせ、それ以外の文章は出力しないでください。
{{"hobbies":"", "interests":"", "values":"", "lifestyle":"", "tech_proficiency":"", "cultural_background":""}}
"""

#課題・目標 3種
CHALLENGES_GOALS_PROMPT = f"""
current_challenges: あなたが現在抱えている問題（プライベート、仕事）について教えてください。
goals: あなたの目標について教えてください。
needs: あなたのニーズについて教えてください。
出力形式は以下のフォーマットに合わせ、それ以外の文章は出力しないでください。
{{"current_challenges":"", "goals":"", "needs":""}}
"""

