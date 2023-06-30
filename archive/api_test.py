#!/Users/simonbricteux/PythonWork/pycharmprojects/api_test/venv/bin/python3.9
from flask import Flask, request, jsonify
from pytube import YouTube
from pytube import Playlist

app = Flask(__name__)
application = app

@app.route("/") #<str:v_url>
def home():
    return "It works!\n Well done, mate!"
    
@app.route("/<v_url>") #<str:v_url>
def get_url(v_url):
    #extra = request.args.get("extra")
    #if extra: #if extra exists
    #test http://127.0.0.1:5000/video_url/zsYIw6RXjfM
    # http://simons-macbook-air.local:5000/video_url/zsYIw6RXjfM
    # 10.0.0.11:5000/video_url/zsYIw6RXjfM
    #  Simons-MacBook-Air:5000/video_url/zsYIw6RXjfM

    url = 'https://www.youtube.com/watch?v=' + v_url

    if 'playlist' in url:
        p = Playlist(url)
        for yt in p.videos:
            yt.streams \
                .filter(progressive=True, file_extension='mp4') \
                .order_by('resolution') \
                .desc() \
                .first() \
                .download('/Users/simonbricteux/Downloads')
    else:
        yt = YouTube(url)
        yt.streams \
            .filter(progressive=True, file_extension='mp4') \
            .order_by('resolution') \
            .desc() \
            .first() \
            .download('/Users/simonbricteux/Downloads')

    return jsonify({"Video url":url}), 200

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
