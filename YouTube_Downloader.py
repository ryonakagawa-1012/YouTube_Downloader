from yt_dlp import YoutubeDL
import ffmpeg
import os
import re

# 出力先を指定
Path = "/Users/UserName/Downloads/YouTube"

# url変数,Inputed_url変数の宣言
url = []
Inputed_url = []

# YouTubeの動画のURLを入力
while True:
    Input = input("Enter URL or Enter 0 to run : ")
    if Input == "0":
        break
    Inputed_url.append(Input)

# プレイリストのURLならプレイリストの中の動画のURLを取得
for i in range(len(Inputed_url)):
    if "playlist" in Inputed_url[i]:
        # プレイリストのURLを指定
        playlist_url = Inputed_url[i]

        # yt-dlpの設定を指定
        ydl_opts = {
            'quiet': True,  # 冗長な出力を非表示にする
        }

        # yt-dlpインスタンスを作成
        ydl = YoutubeDL(ydl_opts)

        # プレイリスト内の動画のURLを取得
        with ydl:
            result = ydl.extract_info(playlist_url, download=False)
            if 'entries' in result:
                playlist_videos = result['entries']
                for video in playlist_videos:
                    url.append(video['webpage_url'])

    else:
        url.append(Inputed_url[i])

for URL in url:
    # yt-dlpで動画のメタデータを取得(動画のタイトル取得のため)
    with YoutubeDL() as ydl:
        res = ydl.extract_info(URL.replace(".mp3", ""), download=False)

    # yt-dlpのオプションを設定
    option = {
        'outtmpl': Path + "/tmpvideo",
        'format': 'bestvideo+bestaudio/best'
    }

    only_mp3_option = {
        'outtmpl': Path + '/%(title)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # 変換したい形式を指定
            'preferredquality': '192'  # ビットレートを指定
        }]
    }

    # 動画のダウンロード
    if ".mp3" in URL:
        YoutubeDL(only_mp3_option).download([URL.replace(".mp3", "")])
        print("Audio download completed")
        continue
    else:
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

    print("*" + res["title"] + " Download and conversion completed")
