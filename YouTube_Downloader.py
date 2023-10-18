from yt_dlp import YoutubeDL
import ffmpeg
import os
import re

# 出力先を指定
Path = "/Users/UserName/Downloads/YouTube"

# yt-dlpのオプションを設定
option = {
        'outtmpl': Path + "/tmpvideo",
        'format': 'bestvideo+bestaudio/best ,video.mp4'
    }

# url変数,Input変数の宣言
url = []
Input = ""

# YouTubeの動画のURLを入力
while True:
    Input = input("Enter URL or Enter 0 to run : ")
    if Input != "0":
        break
    url.append(Input)


for URL in url:
    # yt-dlpで動画のメタデータを取得(動画のタイトル取得のため)
    with YoutubeDL() as ydl:
        res = ydl.extract_info(URL, download=False)

    # 動画のダウンロード
    YoutubeDL(option).download([URL])

    # 入出力パスを指定
    input_path = os.path.join(Path, "tmpvideo.webm")
    output_path = os.path.join(Path, "convertedvideo.mp4")

    # ffmpegを使用してwebmからmp4へ変換
    input_file = ffmpeg.input(input_path)
    output_file = ffmpeg.output(input_file, output_path)

    ffmpeg.run(output_file, overwrite_output=True)

    # 入力ファイルを削除
    os.remove(input_path)

    # 動画ファイルの名前を変更
    os.rename(Path + "/convertedvideo.mp4", Path + "/" + re.sub(r'[/|]', '-', res["title"]) + ".mp4")
    # Windowsの場合、re.sub（）のパターンを'[\\|/|:|?|.|"|<|>|\|]'に変更したら正常に動作する

    print("Video Download and conversion completed")
