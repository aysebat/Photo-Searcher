from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')
class MainScreen(Screen):
    def get_image(self):
        # Get user query from text input
        query = self.manager.current_screen.ids.user_query.text
        #Get Wikipedia images and the first  image url's
        page = wikipedia.page(query,  auto_suggest=False)
        image_link = page.images[0]
        return image_link
    def download_image(self):
        #downloand the images
        headers ={'User-agent':'Mozilla/5.0'}
        req = requests.get(self.get_image(), headers=headers)
        imagePath = 'images/image.jpg'
        with open (imagePath, 'wb') as file:
            file.write(req.content)
        return imagePath
    def set_image(self):
        #put the image in the widget
        self.manager.current_screen.ids.img.source = self.download_image()

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()



MainApp().run()
