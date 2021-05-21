import os

import moviepy.editor
from pytube import YouTube
from youtube_search import YoutubeSearch


def get_url():

    a = 0
    user_query = input("Search here....")
    results = YoutubeSearch(user_query, max_results=5).to_dict()
    results_filtered = dict()
    video_title = list()
    for i in results:
        results_filtered[i['title']
                         ] = 'https://www.youtube.com/'+i['url_suffix']

    result_key = results_filtered.keys()

    for j in result_key:
        a += 1
        print(str(a)+" "+j)
        video_title.append(j)

    user_choice = int(input("Enter the video no. whose audio you want"))-1
    chosen_title = video_title[user_choice]

    url = results_filtered[chosen_title]

    return [url, chosen_title]


def downloadYouTube(final_url, path):
    yt = YouTube(final_url[0])
    yt.streams.get_by_itag(18).download(path)
    # os.chdir(path)
    #os.rename(path+"\\"+final_url[1]+".mp4", path+"\\"+save_name+".mp4")
    # if not os.path.exists(path):
    #     os.makedirs(path)
    # yt.download(path)


def videoToAudio(video_file_name, path):
    video = moviepy.editor.VideoFileClip(path+"\\"+video_file_name+".mp4")
    audio = video.audio
    audio.write_audiofile(path+"\\"+video_file_name+".mp3")




if __name__ == '__main__':
    final_url = get_url()
    path = "D:\\Python programs\\Song_downloads"
    downloadYouTube(final_url, path)
    videoToAudio(final_url[1], "D:\\Python programs\\Song_downloads")
    os.startfile(path+"\\"+final_url[1]+".mp3")