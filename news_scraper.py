import requests
from bs4 import BeautifulSoup
import csv

#  ニュースサイトのURL
url = "https://news.yahoo.co.jp/"

#  ページを取得
response = requests.get(url)
response.encoding = response.apparent_encoding

#  BeautifulSoupで解析
soup = BeautifulSoup(response.text, "html.parser")

#  見出しを取得
headlines = soup.find_all("a")

seen = set()  # すでに追加したURLを記録するための集合
results = []
for link in headlines:
    text = link.text.strip()
    href = link.get("href")
    if text and href and href.startswith("https://news.yahoo.co.jp/pickup"):  # Yahooのピックアップニュース例
        if href not in seen:  # まだ追加していないURLだけを追加
            results.append([text, href])
            seen.add(href)  # 記録

#  コンソールに表示
for i, item in enumerate(results):
    print(f"{i+1}: {item[0]} - {item[1]}")

#  CSVに保存
with open("news_headlines.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["見出し", "URL"])
    writer.writerows(results)

print("✅ news_headlines.csv に保存しました")