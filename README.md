# exiteblog
エクサイトブログから本文のテキストだけを抽出するプログラムです。単ページの抽出とURLリストからの抽出が可能です。

前提としてエクサイトブログはスクレいピングが大変難しいサイトです。欲しかったのは本文の抽出だけで良いので以下の流れで本文を抽出することにします。

1. サイトマップが掲載されているURLをさがします。通常は、https://●●●●/sitemap.xml　です。

2. sitemapscraper.pyを開き　# 初回のサイトマップURLを指定の部分のURLを1で探したURLを入れる

3. python sitemapscraper.py　を実行

4. aill_sitemaps_urls.csv　というファイルができるで一度開く

5. 記事本文以外のURLもけいさいされているので、手作業で削除の上、保存

6. URLリストを抽出するために、python scrape_blog_list.py　を実行

7. 本文の記事のURLリストが多いとテキストがどんどん書き出されていきます。

## 今後の展開

あるかどうかわかりませんが、記事が分割してテキストででてきます。
これをまとめるプログラムの作成。現状はchat-gtpさんにやってもらっています。

## 実行方法

- エクサイトブログ単ページの抽出
scrape_blog.pyのpythonファイルにURLを入力して以下のコマンドを実行

python scrape_blog.py

- URLリストからの抽出
python scrape_blog_list.py

- サイトマップから抽出
python sitemapscraper.py


