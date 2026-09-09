from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class SimpleApp(App):
    def build(self):
        # Create main layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title Label
        self.label = Label(
            text="Hello, Kivy!",
            font_size='24sp'
        )

        # Counter variable
        self.count = 0

        # Action Button
        btn = Button(
            text="Click Me!",
            size_hint=(1, 0.3),
            background_color=(0.2, 0.6, 1, 1)
        )
        
        # Bind button press event
        btn.bind(on_press=self.on_button_click)

        # Add widgets to layout
        layout.add_widget(self.label)
        layout.add_widget(btn)

        return layout

    def on_button_click(self, instance):
        self.count += 1
        self.label.text = f"Button Clicked {self.count} times!"


if __name__ == '__main__':
    SimpleApp().run()
