from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.lang import Builder
from youtube_search import YoutubeSearch
from pytube import YouTube
import moviepy.editor
import os

Window.clearcolor = (0, 0, 0, 1)
Window.size = (500, 640)

Builder.load_file('box.kv')


class MainLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.video_title = list()
        self.playIndex = 0
        self.path = "D:\\Python programs\\Song_downloads"
        self.url = ""
        self.results_filtered = dict()

    def clear(self):
        self.ids.UserQuery.text = ""
        self.ids.result1.text = ""
        self.ids.result2.text = ""
        self.ids.result3.text = ""
        self.ids.result4.text = ""
        self.ids.result5.text = ""


    def show_result(self):
        a = 0
        user_query = self.ids.UserQuery.text
        results = YoutubeSearch(user_query, max_results=5).to_dict()

        for i in results:
            self.results_filtered[i['title']
            ] = 'https://www.youtube.com/' + i['url_suffix']

        result_key = self.results_filtered.keys()

        for j in result_key:
            a += 1
            print(str(a) + " " + j)
            self.video_title.append(j)

        self.ids.result1.text = self.video_title[0]
        self.ids.result2.text = self.video_title[1]
        self.ids.result3.text = self.video_title[2]
        self.ids.result4.text = self.video_title[3]
        self.ids.result5.text = self.video_title[4]

    def indexNo(self, aindex):
        self.playIndex = aindex
        self.url = self.results_filtered[self.video_title[aindex]]
        print(self.url)

    def playSong(self):

        yt = YouTube(self.url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(
            self.path)
        video = moviepy.editor.VideoFileClip(self.path + "\\" + self.video_title[self.playIndex] + ".mp4")
        audio = video.audio
        audio.write_audiofile(self.path + "\\" + self.video_title[self.playIndex] + ".mp3")
        os.startfile(self.path + "\\" + self.video_title[self.playIndex] + ".mp3")


class SastaSpotify(App):
    def build(self):
        return MainLayout()


if __name__ == '__main__':
    SastaSpotify().run()
