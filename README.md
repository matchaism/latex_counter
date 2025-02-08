# LaTeX Counter

LaTeXの文字数をカウントするプログラム．論文などの執筆管理に利用できる．

GitHub Pagesで公開することもできる．

## How to Use

1. `config.py`で文字数のカウントの対象となるtexファイルのパスを登録
   - 初回 or 変更があったときのみ
   - ディレクトリパスを書くと，ディレクトリ内のtexファイルを全てが登録される
   - ディレクトリは再帰的に深堀されないので注意
2. `latex_counter.py`を実行
   - `latex_counter.py`を実行する度に更新される
   - `record.json`と`log.csv`に進捗が記録される

- `index.html`に文字数の進行具合を掲載し，GitHub Pagesで公開することも可能
  - 必要に応じて`index.html`を編集
