#!/usr/bin/env python #python3

#pip install git+https://github.com/pytube/pytube --upgrade

import sys
from pytube import YouTube
from pytube import Playlist

url = sys.argv[1]

# for f in sys.stdin:
# 	url = f
if 'playlist' in url:
	p = Playlist(url)
	for yt in p.videos:
		yt.streams\
                .filter(progressive=True, file_extension='mp4')\
		.order_by('resolution')\
    		.desc()\
    		.first()\
    		.download('/Users/simonbricteux/Downloads')
else:
	yt = YouTube(url)
	yt.streams\
	.filter(progressive=True, file_extension='mp4')\
	.order_by('resolution')\
        .desc()\
        .first()\
        .download('/Users/simonbricteux/Downloads')


