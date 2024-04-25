"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class LBs():
    

class ProgrammzurVerschlüsselungvonVerträgenvonLehrbeauftragten(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            "Your name: ",
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            "Say Hello!",
            on_press=self.say_hello,
            style=Pack(padding=5)
        )
        button2 = toga.Button(
            "Georg",
            on_press=self.say_georg,
            style=Pack(padding=5)
        )

        button_box = toga.Box(style=Pack(direction=ROW, padding=5))
        button_box.add(button)
        button_box.add(button2)
        main_box.add(name_box)
        main_box.add(button_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        self.main_window.info_dialog(
            f"Hello, {self.name_input.value}",
            "Hi there!"
        )
    
    def say_georg(self, widget):
        self.main_window.info_dialog(
            f"Georg",
            "Hallo, mein Name ist Georg und meine Festplatte ist voll."
        )


def main():
    return ProgrammzurVerschlüsselungvonVerträgenvonLehrbeauftragten()

