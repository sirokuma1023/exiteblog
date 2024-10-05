import requests
from bs4 import BeautifulSoup

# ExciteブログのURLを指定
url = 'your_URL'

# ウェブページの内容を取得
response = requests.get(url)

# レスポンスが成功したか確認
if response.status_code == 200:
    # BeautifulSoupを使用してHTMLを解析
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 記事本文を特定するためにHTMLの構造を確認
    # 例: <div class="post-text"> のような部分に記事本文がある場合
    article_body = soup.find('div', class_='post-main')
    
    # 記事本文が存在する場合
    if article_body:
        # テキストのみを抽出
        article_text = article_body.get_text(strip=True)
        
        # 抽出したテキストをファイルに保存
        with open('article.txt', 'w', encoding='utf-8') as file:
            file.write(article_text)
        
        print('記事の本文が article.txt に保存されました。')
    else:
        print('記事の本文を見つけられませんでした。')
else:
    print(f'ページの取得に失敗しました。ステータスコード: {response.status_code}')
