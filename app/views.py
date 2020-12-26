from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponseRedirect
from app.models import URLModel
from app.forms import URLForm
import webbrowser
from gtts import gTTS
import os
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import vlc
import requests
import pygame
from playsound import playsound


# Create your views here.
class IndexView(CreateView):
    form_class = URLForm
    template_name = "index.html"
    initial = {'key': 'value'}
    model = URLModel
    success_url = ''

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            try: 
                # <process form cleaned data>
                url = form.cleaned_data['url']
                req = requests.get(url).text
                soup = BeautifulSoup(req, "html.parser")
                print(soup.text)

            except Exception as e:
                print(e)

            finally:
                # print("hi")
                language = 'en'
                speech = gTTS(text = soup.text, lang=language, slow=False)
                speech.save("text.mp3")
                playsound("text.mp3")
                # to_speech = vlc.MediaPlayer("text.mp3")
                # to_speech.play()

                # os.popen("afplay text.mp3")

            return HttpResponseRedirect(url)

        return render(request, self.template_name, {'form': form})
        
    

