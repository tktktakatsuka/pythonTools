# Bing用クローラーのモジュールをインポート
from icrawler.builtin import BingImageCrawler

# Bing用クローラーの生成
bing_crawler = BingImageCrawler(
    downloader_threads=4,           # ダウンローダーのスレッド数
    storage={'root_dir': 'images'}) # ダウンロード先のディレクトリ名

# クロール（キーワード検索による画像収集）の実行
bing_crawler.crawl(
    keyword = "Fortnite フォートナイト",   # 検索キーワード（日本語もOK）
    max_num=100)                    # ダウンロードする画像の最大枚数