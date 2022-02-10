import kivy
kivy.require('1.0.8')
 
from kivy.app import App
from kivy.uix.button import Label
 
class myexample(App):
 
    def build(self):
        return Label(text="hi")
 
myexample = myexample()
 
myexample.run()