import requests
from bs4 import BeautifulSoup
import csv

# 1. ニュースサイトのURL
url = "https://news.yahoo.co.jp/"

# 2. ページを取得
response = requests.get(url)
response.encoding = response.apparent_encoding

# 3. BeautifulSoupで解析
soup = BeautifulSoup(response.text, "html.parser")

# 4. 見出しを取得（クラス名は変わる可能性があるので調整必要）
headlines = soup.find_all("a")

results = []
for link in headlines:
    text = link.text.strip()
    href = link.get("href")
    if text and href and href.startswith("https://news.yahoo.co.jp/pickup"):  # Yahooのピックアップニュース例
        results.append([text, href])

# 5. コンソールに表示
for i, item in enumerate(results):
    print(f"{i+1}: {item[0]} - {item[1]}")

# 6. CSVに保存
with open("news_headlines.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["見出し", "URL"])
    writer.writerows(results)

print("✅ news_headlines.csv に保存しました")