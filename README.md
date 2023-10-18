# YouTube_Downloader
URLを入れるだけでYouTubeの動画を**最高画質**、**最高音質**、**mp4形式**でダウンロードしてくれるpythonのスクリプト。  
~~誤って消してしまった時のバックアップ。~~
## 実行環境
* macOS 14.0
* python 3.11
## 必須ライブラリ
* yt-dlp
* ffmpeg-python
## 使用方法
1. 実行前にファイルの6行目の`Path = "/Users/UserName/Downloads/YouTube"`を任意のパスに書き換える。
2. ファイルを実行すると、`Enter URL or Enter 0 to run : `と表示されるので、URLを入力し、Enterキーを押す。
3. `0`を入力し、Enterキーを押すと実行が始まる。
4. URLの後に`.mp3`を追加すると音声ファイルのみダウンロードされる。
## 処理内容
1. yt-dlpのオプションで、最高画質の動画と最高音質の音声を別々にダウンロードした後、結合するように設定。
2. URLを入力させる。
3. 動画のメタデータを取得。
4. 動画をオプション通りにダウンロード。（この時、「tmpvideo」という名前で、webm形式でダウンロードされる）
5. webm形式の動画とmp4形式の動画のパスを作成。
6. 作成したパスをffmpeg-pythonに渡して、webm形式からmp4形式に変換。
7. 「convertedvideo.mp4」が生成される。
8. webm形式の動画を削除。
9. 「convertedvideo.mp4」の名前を取得したメタデータの中のタイトルに変更。
## 見つけたバグ
* ~~動画タイトルの中に`/`などの特殊文字が含まれていると処理内容9の名前変更時にエラーが出る。~~ ← 特殊文字を`-`で置き換えることで修正  
  ~~タイトルに特殊文字を使うな！！！~~
* Windowsはファイルに使えない文字がMacより多いので、置き換える文字のパターンを増やさなければ正常に動作しない。（名前が「convertedvideo.mp4」から変更されないだけで、ダウンロード自体は正常に行われる。）
## 参考にしたサイト
* [pythonでYouTubeをダウンロードするyt-dlpのコピペコード14本まとめ](https://diy-programming.site/youtube/download/)
* [Pythonでffmpegを使って動画をmp3に変換する方法](https://mekatana.com/python-ffmpeg/)
