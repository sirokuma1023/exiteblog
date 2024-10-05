import requests
from bs4 import BeautifulSoup
import csv

# URLのリストが保存されているCSVファイルのパス
csv_file = 'url_list.csv'

# URLリストの読み込み
with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    url_list = [row[0] for row in reader]  # CSVの1列目をURLとして取得

# 各URLから記事本文を取得して保存
for idx, url in enumerate(url_list):
    try:
        # ウェブページの内容を取得
        response = requests.get(url)
        
        if response.status_code == 200:
            # BeautifulSoupを使用してHTMLを解析
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # 記事本文を特定（HTML構造に基づき適宜変更）
            article_body = soup.find('div', class_='post-text')
            
            if article_body:
                # テキストを抽出
                article_text = article_body.get_text(strip=True)
                
                # ファイルに保存 (記事番号でファイル名を生成)
                file_name = f'article_{idx+1}.txt'
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(article_text)
                
                print(f'{file_name} に記事が保存されました。')
            else:
                print(f'{url} の記事本文が見つかりませんでした。')
        else:
            print(f'{url} のページ取得に失敗しました。ステータスコード: {response.status_code}')
    
    except Exception as e:
        print(f'{url} の処理中にエラーが発生しました: {e}')