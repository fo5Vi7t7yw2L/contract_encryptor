import logging
from pathlib import Path
import tomllib
# from functools import partial
import pyodbc

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

logging.basicConfig(level=logging.DEBUG)

# QUERYSTRING = config[dbquery][string]
        
class ContractEncryptor(toga.App):
    def startup(self):

        self.config = self.load_config()
        self.db_connection = DB(self.config['database'])

        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            "Your name: ",
            style=Pack(padding=(0, 5))
        )

        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        querybutton = toga.Button(
            "query the DB",
            on_press=None,
            style=Pack(padding=5)
        )
        
        button_box = toga.Box(style=Pack(direction=ROW, padding=5))
        button_box.add(querybutton)
        main_box.add(name_box)
        main_box.add(button_box)


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


    def load_config(self):
        with open (fr"{self.paths.app}\resources\config.toml", mode="rb") as f:
            config = tomllib.load(f)
        return config


class DB():
    def __init__(self, config):
        self.connectionstring = f'DRIVER={config['driver']};DBQ={config['path']}'

        logging.info(f"trying to connect to Database: {self.connectionstring}")

        try:
            self.connection = pyodbc.connect(self.connectionstring)
            logging.info(f"Successfully connected to Database: {self.connectionstring}!")
        except Exception as e:
            logging.error(e)
            self.connection = None

    def query(self, strquery):
        pass

def main():
    return ContractEncryptor()



