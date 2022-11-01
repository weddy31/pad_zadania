import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
kivy.require('2.1.0')


class MainWidget(Widget):
    angle = NumericProperty(0)
    increment = NumericProperty(1)

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.angle = 1

    def rotate(self, angle):
        angle_2 = (self.angle + angle) % 360
        if angle_2 >= 0:
            self.angle = angle_2
        else:
            360 - angle_2
        self.output_label.text = f"Kąt: {self.angle}"


class MainApp(App):
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    MainApp().run()
