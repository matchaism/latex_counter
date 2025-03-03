import os, re, json, csv
from datetime import datetime
import config

def count_characters(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # コメントやLaTeXコマンドを削除
    content = re.sub(r'%.*', '', content)  # コメント行削除
    content = re.sub(r'\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{[^\}]*\})?', '', content)  # コマンド削除
    content = re.sub(r'[^a-zA-Z0-9\u4e00-\u9fff]', '', content)  # 記号やスペースを削除

    return len(content)

def listup_tex_file(targets):
    file_paths = []

    for target in targets:
        # ファイルが存在しない場合
        if not os.path.exists(target):
            print(f'Error: {target} does not exist.')
            continue

        # texファイルへの直接のパスの場合
        if os.path.isfile(target) and target[-4:] == '.tex':
            file_paths.append(target)
            continue

        # ディレクトリパスの場合
        if os.path.isdir(target):
            for filename in os.listdir(target):
                file_path = os.path.join(target, filename)
                if os.path.isfile(file_path) and file_path[-4:] == '.tex':
                    file_paths.append(file_path)

    return file_paths

def main():
    record_file = 'record.json'
    log_file = 'log.csv'

    # texファイルのパスをリストアップ
    file_paths = listup_tex_file(config.targets)

    # 現在の文字数をカウント
    current_count = 0
    for file_path in file_paths:
        current_count += count_characters(file_path)

    # 前日の文字数を取得
    previous_count = 0
    if os.path.exists(record_file):
        with open(record_file, 'r', encoding='utf-8') as f:
            d = json.load(f)
            previous_count = int(d['current_count'])

    # 増減を計算
    difference = current_count - previous_count
    print(f'Previous count: {previous_count}')
    print(f'Current count: {current_count}')
    print(f'Difference: {difference}')

    # JSON形式で結果を出力
    result = {
        'previous_count': previous_count,
        'current_count': current_count,
        'difference': difference
    }
    with open(record_file, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    # ログを出力
    rows = [[datetime.now().strftime('%Y-%m-%d'), previous_count, current_count, difference]]
    if not os.path.exists(log_file):
        rows = [['date', 'previous_count', 'current_count', 'difference']] + rows
    with open(log_file, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(rows)

if __name__ == '__main__':
    main()
