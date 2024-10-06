import requests
import xml.etree.ElementTree as ET
import csv

# サイトマップURLリストが保存されているCSVファイルのパス
sitemap_csv_file = 'sitemap_list.csv'

# URLを保存するリスト
all_urls = []

# 名前空間を指定
namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

# サイトマップを再帰的に処理する関数
def process_sitemap(sitemap_url):
    try:
        response = requests.get(sitemap_url)
        if response.status_code == 200:
            sitemap_xml = ET.fromstring(response.content)
            
            # サブサイトマップが含まれている場合
            if sitemap_xml.tag == '{http://www.sitemaps.org/schemas/sitemap/0.9}sitemapindex':
                for sitemap in sitemap_xml.findall("ns:sitemap", namespaces=namespace):
                    loc = sitemap.find("ns:loc", namespaces=namespace).text
                    print(f'サブサイトマップを処理中: {loc}')
                    process_sitemap(loc)  # サブサイトマップを再帰的に処理
            else:
                # 通常のURLを処理
                for url in sitemap_xml.findall("ns:url", namespaces=namespace):
                    loc = url.find("ns:loc", namespaces=namespace).text
                    all_urls.append(loc)
        else:
            print(f'{sitemap_url} の取得に失敗しました。ステータスコード: {response.status_code}')
    except Exception as e:
        print(f'{sitemap_url} の処理中にエラーが発生しました: {e}')

# CSVファイルからサイトマップURLリストを読み込む
with open(sitemap_csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    sitemap_urls = [row[0] for row in reader]

# 各サイトマップURLを処理
for sitemap_url in sitemap_urls:
    process_sitemap(sitemap_url)

# すべてのURLを一つのCSVファイルに保存
with open('all_sitemaps_urls.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for url in all_urls:
        writer.writerow([url])

print(f'すべてのURLが all_sitemaps_urls.csv に保存されました。')