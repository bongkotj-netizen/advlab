from yt_dlp import YoutubeDL

url = input("กรูณาใส่ URL ของ YouTube: ")
options = {
    'outtmpl': '%(title)s.%(ext)s',
}

with YoutubeDL(options) as ydl:
    ydl.download([url])

    print("ดาวน์โหลดเสร็จเรียบร้อยแล้ว")