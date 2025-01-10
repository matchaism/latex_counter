import os, re, sys

def count_characters(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # コメントやLaTeXコマンドを削除
    content = re.sub(r'%.*', '', content)  # コメント行削除
    content = re.sub(r'\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{[^\}]*\})?', '', content)  # コマンド削除
    content = re.sub(r'[^a-zA-Z0-9\u4e00-\u9fff]', '', content)  # 記号やスペースを削除
    return len(content)

def main(file_paths):
    record_file = 'record.txt'

    # 現在の文字数をカウント
    current_count = 0
    for file_path in file_paths:
        if not os.path.exists(file_path): # ファイルが存在しない場合
            print(f"Error: {file_path} does not exist.")
            return
        if file_path[-4:] == '.tex': # texファイルへの直接のパスの場合
            current_count += count_characters(file_path)
            continue
        for tex_file in os.listdir(file_path):
            if file_path[-4:] == 'tex': # ディレクトリパスの場合
                current_count += count_characters(os.path.join(file_path, tex_file))

    # 前日の文字数を取得
    if os.path.exists(record_file):
        with open(record_file, 'r', encoding='utf-8') as f:
            previous_count = int(f.read().strip())
    else:
        previous_count = 0

    # 増減を計算
    difference = current_count - previous_count
    print(f"Previous count: {previous_count}")
    print(f"Current count: {current_count}")
    print(f"Difference: {difference}")

    # 現在の文字数を記録
    with open(record_file, 'w', encoding='utf-8') as f:
        f.write(str(current_count))

if __name__ == '__main__':
    args = sys.argv
    main(sys.argv[1:])
