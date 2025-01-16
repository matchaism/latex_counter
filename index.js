async function loadCharacterCount() {
  try {
    // JSONファイルを取得
    const response = await fetch('record.json'); // ファイルパスに応じて変更
    if (!response.ok) throw new Error('Failed to load JSON file.');
    const data = await response.json();
    // データを表示
    document.getElementById("result").textContent = `Previous Count: ${data.previous_count}, Current Count: ${data.current_count} (diff: ${data.difference})`;
    // ポスト(ツイート)の用意
    const target = document.getElementById("tweet").href = "https://twitter.com/intent/tweet?text=" + `論文の文字数${data.previous_count}->${data.current_count} ${location.href}`;
  } catch (error) {
    console.error(error);
    document.getElementById("result").textContent = "データの取得に失敗しました。";
  }
}
