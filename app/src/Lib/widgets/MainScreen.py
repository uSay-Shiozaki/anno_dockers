from tracemalloc import start
from webbrowser import BackgroundBrowser
from kivy.uix.boxlayout import BoxLayout
from widgets.MyGridLayout import MyGridLayout
from widgets.StartSpinner import StartSpinner
from kivy.uix.button import Button
import os
import subprocess
from kivy.network.urlrequest import UrlRequest
import asyncio
import utils
import shutil
from widgets.PopupRaiseError import PopupRaiseError

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Main Screen Launched")
        
    def on_success(self, req, res):
        print("Posted successfully")
        print(req)
        
    def on_failure(self, req, res):
        print("Failed Posting")
        print(req)
        print(res)

    def on_error(self, req, res):
        print("Error occured!")
        print(req)
        print(res)

    def on_progress(self, req, current_size, total_size):
        print("On progress")
        
    def export(self):
        savePath = utils.saveDialog()
        if savePath:
            if os.path.exists('/database/cluster_map.json'):
                shutil.copyfile('/database/cluster_map.json', savePath)
            else:
                # raise FileNotFoundError("Please classify your data before export")
                
                pop = PopupRaiseError(
                    title='Raise Error',
                    size_hint = (0.4, 0.3),
                    pos_hint = {'x': 0.3, 'y': 0.35},
                    message = "Please classify your data before export."
                )
                pop.bind(
                    on_yes=pop.dismiss
                )
                pop.open()

        
