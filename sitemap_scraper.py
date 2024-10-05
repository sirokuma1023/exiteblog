import requests
import xml.etree.ElementTree as ET
import csv

# 名前空間を指定
namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

# URLを保存するリスト
all_urls = []

# サイトマップを再帰的に処理する関数
def process_sitemap(sitemap_url):
    try:
        response = requests.get(sitemap_url)
        if response.status_code == 200:
            sitemap_xml = ET.fromstring(response.content)
            
            # サブサイトマップが含まれている場合（sitemapindex タグ）
            if sitemap_xml.tag == '{http://www.sitemaps.org/schemas/sitemap/0.9}sitemapindex':
                for sitemap in sitemap_xml.findall("ns:sitemap", namespaces=namespace):
                    loc = sitemap.find("ns:loc", namespaces=namespace).text
                    print(f'サブサイトマップを処理中: {loc}')
                    process_sitemap(loc)  # サブサイトマップを再帰的に処理
            else:
                # 通常のURLが含まれている場合（url タグ）
                for url in sitemap_xml.findall("ns:url", namespaces=namespace):
                    loc = url.find("ns:loc", namespaces=namespace).text
                    all_urls.append(loc)
        else:
            print(f'{sitemap_url} の取得に失敗しました。ステータスコード: {response.status_code}')
    except Exception as e:
        print(f'{sitemap_url} の処理中にエラーが発生しました: {e}')

# 初回のサイトマップURLを指定
initial_sitemap_url = 'https://takayukik.exblog.jp/sitemap.xml'

# 最初のサイトマップURLを処理
process_sitemap(initial_sitemap_url)

# すべてのURLを一つのCSVファイルに保存
with open('all_sitemaps_urls.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for url in all_urls:
        writer.writerow([url])

print(f'すべてのURLが all_sitemaps_urls.csv に保存されました。')