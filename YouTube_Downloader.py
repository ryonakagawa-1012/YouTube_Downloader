from yt_dlp import YoutubeDL
import ffmpeg
import os

# 出力先を指定
Path = "/Users/ryo/Downloads/YouTube"

# yt-dlpのオプションを設定
option = {
        'outtmpl': Path + "/%(title)s",
        'format': 'bestvideo+bestaudio/best ,video.mp4'
    }

# YouTubeのURLを入力
URL = input("Enter URL : ")

# yt-dlpでメタデータを取得(タイトル取得のため)
with YoutubeDL() as ydl:
    res = ydl.extract_info(URL, download=False)

# 動画のダウンロード
YoutubeDL(option).download([URL])

# 入出力ファイルの名前を作成
input_title = res["title"] + ".webm"
output_title = res["title"] + ".mp4"

# 入出力パスを指定
input_path = os.path.join(Path, input_title)
output_path = os.path.join(Path, output_title)

# ffmpegを使用して変換
input_file = ffmpeg.input(input_path)
output_file = ffmpeg.output(input_file, output_path)

ffmpeg.run(output_file, overwrite_output=True)

# 入力ファイルを削除
os.remove(input_path)

print("Video Download and conversion completed")
