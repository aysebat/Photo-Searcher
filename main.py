from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')
class MainScreen(Screen):
    def search_images(self):
        # Get user quey from text input
        query = self.manager.current_screen.ids.user_query.text
        #Get Wikipedia images and the first  image url's
        page = wikipedia.page(query,  auto_suggest=False)
        image_link = page.images[0]
        #downloand the images
        headers ={'User-agent':'Mozilla/5.0'}
        req = requests.get(image_link, headers=headers)
        with open ('images/image.jpg', 'wb') as file:
            file.write(req.content)
        #put the image in the widget
        self.manager.current_screen.ids.img.source = 'images/image.jpg'

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()



MainApp().run()
