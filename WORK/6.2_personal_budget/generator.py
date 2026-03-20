import os
import sys
import argparse
from google import genai

def generate_article(theme: str) -> str:
    client = genai.Client()
    model_id = "gemini-3-flash-preview"

    prompt = f"""
Твоя задача — написать статью в стиле Википедии на тему {theme} на русском языке простым и понятным языком.
Статья должна включать:
- Введение с определением темы
- Исторический контекст (если применимо)
- Основные характеристики и факты
- Интересные детали
- Разделы с подзаголовками (используй ## для основных разделов)
- не включай раздел смотри также

Объем: примерно 250-500 слов.
Используй формат Markdown для оформления
"""

    response = client.models.generate_content(
        model=model_id,
        contents=prompt
    )
    
    if response.text:
        return response.text
    else:
        print("Error: Model returned an empty response.")
        return None

def format_article(article: str) -> str:
    return article + """

---
Авторы: Гига Максим, Изиланов Илья\\
Ресурсы: LLM - Google Gemini 
"""


def main():
    if len(sys.argv) < 3:
        print("theme and output filename must be provided")
        return
    theme = sys.argv[1]
    output = sys.argv[2]

    article = generate_article(theme)
    article = format_article(article)

    with open(output, "w", encoding="utf-8") as f:
        f.write(article)
    print(f"saved to {output}")


if __name__ == "__main__":
    main()
