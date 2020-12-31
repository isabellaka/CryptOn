# Copyright © 2021 Isabella Kainer

import string
import kivy
from kivy.config import Config
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.dropdown import DropDown
from kivy.lang import Builder
from kivy.core.window import Window
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import os
from os.path import expandvars

kivy.require("2.0.0")
Config.set("input", "mouse", "mouse, multitouch_on_demand") # ohne diese Zeile entsteht bei einem Rechtsklick ein roter Punkt auf den Bildschirm



class MyApp(App):
    def build(self):

        self.title = "CryptOn"
        self.icon = "schloss_blau.png"


        return sm



class CustomDropDown(DropDown):
    def __init__(self):

        pass



class Startpage(Screen):
    def __init__(self, **kwargs):
        super(Startpage, self).__init__()
        def makedropdown():
            self.add_widget(dropdown2)
        def makedropdown_3():
            self.add_widget(dropdown3)

        def uebersicht_menu(self, state):

            if state == "down":
                flayout.clear_widgets()

                logo_start = Builder.load_string("""Image:
                                                        source: "Startpage_hell.png"
                                                        size_hint_x: 1
                                                        size_hint_y: 0.9
                                                        pos_hint: {"top":0.9, "right":1}                                                        
                                                        """)


                flayout.add_widget(logo_start)


            else:
                pass



        def encrypt(filename, get_message):
            def build_finishpopup():
                Window.set_system_cursor("arrow")
                content = Builder.load_string("""Label:
                                                    text: "Verschlüsselung des Textes erfolgreich abgeschlossen."

                                                    font_name: "MPLUSRounded1c-Medium.ttf"
                                                    text_size: self.width, None
                                                    font_size: "18sp"
                                                    size_hint: 1, None
                                                    height: self.texture_size[1]
                                                    valign: "center"
                                                    pos_hint: {"top":0.9, "right":1}
                                                    """)
                ok_button = Builder.load_string("""Button:
                                                        background_normal: ""
                                                        background_color: 0, 0.4, 0.5, 1
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.size
                                                        font_size: "18sp"
                                                        halign: "center"
                                                        valign: "center"
                                                        size_hint: 0.3, 0.2
                                                        pos_hint: {"top":0.25, "right":0.9}
                                                        text: "OK"
                                                        """)
                widget_float = Builder.load_string("""FloatLayout:
                                                            size_hint: 1, 1
                                                            pos_hint: {"top":1, "right":1}
                                                            """)
                widget_float.add_widget(ok_button)
                widget_float.add_widget(content)

                popup_fertig = Builder.load_string("""Popup:
                                                            title: "Verschlüsselung abgeschlossen"
                                                            size_hint: 0.3, 0.4
                                                            pos_hint: {"middle":1, "center":1}
                                                            separator_color: 0, 0.4, 0.5, 1
                                                            title_size: "18sp"
                                                            title_font: "MPLUSRounded1c-Medium.ttf"
                                                            auto_dismiss: False
                                                            """)
                popup_fertig.content = widget_float
                ok_button.bind(on_press=lambda x: popup_fertig.dismiss())
                if feature == "dropdown2_1_menu":
                    dropdown2_1_menu()
                elif feature == "dropdown2_2_menu":
                    dropdown2_2_menu()
                popup_fertig.open()



            Window.set_system_cursor("wait")


            salt = get_random_bytes(16)
            key = PBKDF2(password, salt, 32, count=1000000, hmac_hash_module=SHA512)


            message = get_message.encode()  # .encode() --> convert string input to bytes

            cipher = AES.new(key, AES.MODE_EAX)
            ciphertext, mactag = cipher.encrypt_and_digest(message)

            if os.path.isdir("Verschlüsselte Dateien") == False:
                os.mkdir("Verschlüsselte Dateien")

            with open(f"{os.path.dirname(os.path.abspath(__file__))}\\Verschlüsselte Dateien\\{filename}.txt", "wb") as file:
                file.write(cipher.nonce)
                file.write(mactag)
                file.write(salt)
                file.write(ciphertext)
                file.close()

            build_finishpopup()


        def encrypt_prep(filename, get_message):
            global popup_alreadyexists
            if password != None:

                if filename != "":
                    if os.path.isfile(f"./{filename}.txt"):
                        popup_alreadyexists = Builder.load_string("""Popup:
                                                    title: "Datei mit diesem Namen existiert schon!"
                                                    size_hint: 0.3, 0.4
                                                    pos_hint: {"middle":1, "center":1}
                                                    separator_color: 0, 0.4, 0.5, 1
                                                    title_size: "18sp"
                                                    title_font: "MPLUSRounded1c-Medium.ttf"
                                                    auto_dismiss: False
                                                    """)
                        content = Builder.load_string("""Label:
                                                            text: "Möchten Sie die neue Datei umbenennen oder die schon bestehende Datei ersetzen?"
    
                                                            font_name: "MPLUSRounded1c-Medium.ttf"
                                                            text_size: self.width, None
                                                            font_size: "18sp"
                                                            size_hint: 1, None
                                                            height: self.texture_size[1]
                                                            valign: "center"
                                                            pos_hint: {"top":0.9, "right":1}
                                                            """)
                        umbenennen_button = Builder.load_string("""Button:
                                                                background_normal: ""
                                                                background_color: 0, 0.4, 0.5, 1
                                                                font_name: "MPLUSRounded1c-Medium.ttf"
                                                                text_size: self.size
                                                                font_size: "18sp"
                                                                halign: "center"
                                                                valign: "center"
                                                                size_hint: 0.3, 0.2
                                                                pos_hint: {"top":0.25, "right":0.45}
                                                                text: "Umbenennen"
                                                                """)
                        ersetzen_button = Builder.load_string("""Button:
                                                                        background_normal: ""
                                                                        background_color: 0, 0.4, 0.5, 1
                                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                                        text_size: self.size
                                                                        font_size: "18sp"
                                                                        halign: "center"
                                                                        valign: "center"
                                                                        size_hint: 0.3, 0.2
                                                                        pos_hint: {"top":0.25, "right":0.85}
                                                                        text: "Ersetzen"
                                                                        """)
                        widget_float = Builder.load_string("""FloatLayout:
                                                                    size_hint: 1, 1
                                                                    pos_hint: {"top":1, "right":1}
                                                                    """)


                        umbenennen_button.bind(on_press = lambda x: popup_alreadyexists.dismiss())
                        ersetzen_button.bind(on_press=lambda x: encrypt(filename, get_message))
                        ersetzen_button.bind(on_press = lambda x: popup_alreadyexists.dismiss())
                        widget_float.add_widget(umbenennen_button)
                        widget_float.add_widget(ersetzen_button)
                        widget_float.add_widget(content)
                        popup_alreadyexists.add_widget(widget_float)
                        popup_alreadyexists.open()
                    else:
                        encrypt(filename, get_message)
                else:
                    content = Builder.load_string("""Label:
                                                        text: "Erstellen Sie erst einen Dateinamen bevor Sie Ihren Text verschlüsseln!"

                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.width, None
                                                        font_size: "18sp"
                                                        size_hint: 1, None
                                                        height: self.texture_size[1]
                                                        valign: "center"
                                                        pos_hint: {"top":0.9, "right":1}
                                                        """)
                    ok_button = Builder.load_string("""Button:
                                                            background_normal: ""
                                                            background_color: 0, 0.4, 0.5, 1
                                                            font_name: "MPLUSRounded1c-Medium.ttf"
                                                            text_size: self.size
                                                            font_size: "18sp"
                                                            halign: "center"
                                                            valign: "center"
                                                            size_hint: 0.3, 0.2
                                                            pos_hint: {"top":0.25, "right":0.9}
                                                            text: "OK"
                                                            """)
                    widget_float = Builder.load_string("""FloatLayout:
                                                                size_hint: 1, 1
                                                                pos_hint: {"top":1, "right":1}
                                                                """)
                    widget_float.add_widget(ok_button)
                    widget_float.add_widget(content)

                    popup = Builder.load_string("""Popup:
                                                        title: "Keinen Dateinamen erstellt!"
                                                        size_hint: 0.3, 0.4
                                                        pos_hint: {"middle":1, "center":1}
                                                        separator_color: 0, 0.4, 0.5, 1
                                                        title_size: "18sp"
                                                        title_font: "MPLUSRounded1c-Medium.ttf"
                                                        auto_dismiss: False
                                                        """)
                    popup.content = widget_float
                    ok_button.bind(on_press=lambda x: popup.dismiss())

                    popup.open()
            else:
                content = Builder.load_string("""Label:
                                                    text: "Erstellen Sie erst ein Passwort bevor Sie ihren Text verschlüsseln!"

                                                    font_name: "MPLUSRounded1c-Medium.ttf"
                                                    text_size: self.width, None
                                                    font_size: "18sp"
                                                    size_hint: 1, None
                                                    height: self.texture_size[1]
                                                    valign: "center"
                                                    pos_hint: {"top":0.9, "right":1}
                                                    """)
                ok_button = Builder.load_string("""Button:
                                                        background_normal: ""
                                                        background_color: 0, 0.4, 0.5, 1
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.size
                                                        font_size: "18sp"
                                                        halign: "center"
                                                        valign: "center"
                                                        size_hint: 0.3, 0.2
                                                        pos_hint: {"top":0.25, "right":0.9}
                                                        text: "OK"
                                                        """)
                widget_float = Builder.load_string("""FloatLayout:
                                                            size_hint: 1, 1
                                                            pos_hint: {"top":1, "right":1}
                                                            """)
                widget_float.add_widget(ok_button)
                widget_float.add_widget(content)

                popup = Builder.load_string("""Popup:
                                                    title: "Kein Passwort erstellt!"
                                                    size_hint: 0.3, 0.4
                                                    pos_hint: {"middle":1, "center":1}
                                                    separator_color: 0, 0.4, 0.5, 1
                                                    title_size: "18sp"
                                                    title_font: "MPLUSRounded1c-Medium.ttf"
                                                    auto_dismiss: False
                                                    """) # auto_dismiss:False is necessary for Windows 10, not for Windows 7
                popup.content = widget_float
                ok_button.bind(on_press=lambda x: popup.dismiss())

                popup.open()

        def save_decrypted_text():
            def save():
                folder_selection = filechooser.selection
                name_of_file = save_name_input.text
                if name_of_file == "":
                    new_content = Builder.load_string("""Label:
                                                            text: 'Geben Sie einen Dateinamen in das entsprechende Feld ein.'

                                                            font_name: "MPLUSRounded1c-Medium.ttf"
                                                            text_size: self.width, None
                                                            font_size: "18sp"
                                                            size_hint: 1, None
                                                            height: self.texture_size[1]
                                                            valign: "center"
                                                            pos_hint: {"top":0.9, "right":1}
                                                            """)
                    ok_button = Builder.load_string("""Button:
                                                            background_normal: ""
                                                            background_color: 0, 0.4, 0.5, 1
                                                            font_name: "MPLUSRounded1c-Medium.ttf"
                                                            text_size: self.size
                                                            font_size: "18sp"
                                                            halign: "center"
                                                            valign: "center"
                                                            size_hint: 0.3, 0.2
                                                            pos_hint: {"top":0.25, "right":0.9}
                                                            text: "OK"
                                                            """)
                    new_widget_float = Builder.load_string("""FloatLayout:
                                                                    size_hint: 1, 1
                                                                    pos_hint: {"top":1, "right":1}
                                                                    """)
                    new_widget_float.add_widget(ok_button)
                    new_widget_float.add_widget(new_content)

                    popup = Builder.load_string("""Popup:
                                                        title: "Kein Dateiname!"
                                                        size_hint: 0.3, 0.4
                                                        pos_hint: {"middle":1, "center":1}
                                                        separator_color: 0, 0.4, 0.5, 1
                                                        title_size: "18sp"
                                                        title_font: "MPLUSRounded1c-Medium.ttf"
                                                        auto_dismiss: False
                                                        """)
                    popup.content = new_widget_float
                    ok_button.bind(on_press = lambda x: popup.dismiss())

                    popup.open()
                    return
                else:
                    pass
                try:
                    with open(f"{folder_selection[0]}\\{name_of_file}.txt", "w") as file: # Name des files wird an den selection path (der als string in einer list gespeichert ist) angehängt.
                        file.write(decoded_text)
                        file.close()
                    filechooser_popup.dismiss()
                except IndexError: # is needed because folder_selection doesn't work when no folder is selected
                    with open(f"{filechooser.rootpath}\\{name_of_file}.txt", "w") as file:
                        file.write(decoded_text)
                        file.close()
                    filechooser_popup.dismiss()
            def open_filechooser():
                laufwerk_popup.dismiss()
                if laufwerk_input.text not in drives:
                    new_content = Builder.load_string("""Label:
                                                        text: 'Beispiel für einen gültigen Laufwerknamen: C:'

                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.width, None
                                                        font_size: "18sp"
                                                        size_hint: 1, None
                                                        height: self.texture_size[1]
                                                        valign: "center"
                                                        pos_hint: {"top":0.9, "right":1}
                                                        """)
                    ok_button = Builder.load_string("""Button:
                                                            background_normal: ""
                                                            background_color: 0, 0.4, 0.5, 1
                                                            font_name: "MPLUSRounded1c-Medium.ttf"
                                                            text_size: self.size
                                                            font_size: "18sp"
                                                            halign: "center"
                                                            valign: "center"
                                                            size_hint: 0.3, 0.2
                                                            pos_hint: {"top":0.25, "right":0.9}
                                                            text: "OK"
                                                            """)
                    new_widget_float = Builder.load_string("""FloatLayout:
                                                                    size_hint: 1, 1
                                                                    pos_hint: {"top":1, "right":1}
                                                                    """)
                    new_widget_float.add_widget(ok_button)
                    new_widget_float.add_widget(new_content)

                    popup = Builder.load_string("""Popup:
                                                        title: "Eingabe nicht gültig!"
                                                        size_hint: 0.3, 0.4
                                                        pos_hint: {"middle":1, "center":1}
                                                        separator_color: 0, 0.4, 0.5, 1
                                                        title_size: "18sp"
                                                        title_font: "MPLUSRounded1c-Medium.ttf"
                                                        auto_dismiss: False
                                                        """)
                    popup.content = new_widget_float
                    ok_button.bind(on_press = lambda x: popup.dismiss())

                    popup.open()
                else:
                    filechooser.rootpath = expandvars(laufwerk_input.text + "\\") # das "\\" ist wichtig, damit bei externen Laufwerken (wie z.B. USB-Sticks) alle Ordner gefunden werden.
                    filechooser_popup.open()
            filechooser_popup = Builder.load_string("""Popup:
                                                            title: "Wählen sie einen Ordner und einen Dateinamen."
                                                            
                                                            separator_color: 0, 0.4, 0.5, 1
                                                            title_size: "18sp"
                                                            title_font: "MPLUSRounded1c-Medium.ttf"
                                                            auto_dismiss: False
                                                            """)
            filechooser_flayout = Builder.load_string("""FloatLayout:
                                                            size_hint: 1, 1
                                                            pos_hint: {"top":1, "right":1}
                                                            """)

            filechooser = Builder.load_string("""FileChooserIconView:
                                                        size_hint: 1, 0.8
                                                        pos_hint: {"top": 1, "right": 1}
                                                        dirselect: True
                                                        """)
            filechooser.filters = "?." # versteckt alle files, damit nur mehr folders zur Auswahl stehen (da files immer einen Punkt im Namen haben, der vor der Fileendung steht, folders haben sowas nicht)

            drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)] # lists all drives that exist on the device
            print(drives)


            save_name_label = Builder.load_string("""Label:
                                                        text: "Dateiname:"
    
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.width, None
                                                        font_size: "18sp"
                                                        size_hint: 0.1, 0.1
                                                        height: self.texture_size[1]
                                                        valign: "center"
                                                        halign: "right"
                                                        pos_hint: {"top":0.15, "right":0.525}
                                                        """)
            save_name_input = Builder.load_string("""TextInput:
                                                            size_hint: 0.2, 0.05
                                                            pos_hint: {"top":0.125, "right":0.73}
                                                            padding: [3, (self.height-self.line_height)/2]
                                                            font_name: "MPLUSRounded1c-Medium.ttf"
                                                            font_size: "18sp"
                                                            multiline: False
                                                            """) # padding lässt einen den Text im textinput auch in der Mitte positionieren.

            save_name_input.hint_text = "file_decrypted"

            savetext_button = Builder.load_string("""Button:
                                                        background_normal: ""
                                                        background_color: 0, 0.4, 0.5, 1
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.size
                                                        font_size: "18sp"
                                                        halign: "center"
                                                        valign: "center"
                                                        size_hint: 0.1, 0.1
                                                        pos_hint: {"top":0.15, "right":0.85}
                                                        text: "Speichern"
                                                        """)
            abbrechen_button = Builder.load_string("""Button:
                                                        background_normal: ""
                                                        background_color: 0, 0.4, 0.5, 1
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.size
                                                        font_size: "18sp"
                                                        halign: "center"
                                                        valign: "center"
                                                        size_hint: 0.1, 0.1
                                                        pos_hint: {"top":0.15, "right":0.97}
                                                        text: "Abbrechen"
                                                        """)
            content = Builder.load_string("""Label:
                                                  text: "Wählen Sie ein Laufwerk aus, auf dem Sie speichern möchten."

                                                  font_name: "MPLUSRounded1c-Medium.ttf"
                                                  text_size: self.width, None
                                                  font_size: "18sp"
                                                  size_hint: 1, None
                                                  height: self.texture_size[1]
                                                  valign: "center"
                                                  pos_hint: {"top":0.9, "right":1}
                                                  """)
            fertig_button = Builder.load_string("""Button:
                                                      background_normal: ""
                                                      background_color: 0, 0.4, 0.5, 1
                                                      font_name: "MPLUSRounded1c-Medium.ttf"
                                                      text_size: self.size
                                                      font_size: "18sp"
                                                      halign: "center"
                                                      valign: "center"
                                                      size_hint: 0.3, 0.2
                                                      pos_hint: {"top":0.25, "right":0.9}
                                                      text: "Fertig"
                                                      """)
            widget_float = Builder.load_string("""FloatLayout:
                                                      size_hint: 1, 1
                                                      pos_hint: {"top":1, "right":1}
                                                      """)
            laufwerk_input =  Builder.load_string("""TextInput:
                                                        size_hint: 0.5, 0.15
                                                        pos_hint: {"top":0.225, "right":0.55}
                                                        padding: [3, (self.height-self.line_height)/2]
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        font_size: "18sp"
                                                        multiline: False
                                                        """)
            laufwerk_input.hint_text = str(drives)
            fertig_button.bind(on_press = lambda x: open_filechooser())
            widget_float.add_widget(fertig_button)
            widget_float.add_widget(content)
            widget_float.add_widget(laufwerk_input)

            laufwerk_popup = Builder.load_string("""Popup:
                                              title: "Laufwerk auswählen"
                                              size_hint: 0.3, 0.4
                                              pos_hint: {"middle":1, "center":1}
                                              separator_color: 0, 0.4, 0.5, 1
                                              title_size: "18sp"
                                              title_font: "MPLUSRounded1c-Medium.ttf"
                                              auto_dismiss: False
                                              """)
            laufwerk_popup.content = widget_float
            laufwerk_popup.open()
            abbrechen_button.bind(on_press = lambda x: filechooser_popup.dismiss())
            savetext_button.bind(on_press = lambda x: save())
            filechooser_flayout.add_widget(filechooser)
            filechooser_flayout.add_widget(save_name_label)
            filechooser_flayout.add_widget(save_name_input)
            filechooser_flayout.add_widget(savetext_button)
            filechooser_flayout.add_widget(abbrechen_button)
            filechooser_popup.content = filechooser_flayout


        def after_decrypting():
            global decoded_text
            decoded_text = plaintext.decode()  # .decode() --> convert bytes to string
            text_input.text = decoded_text
            Window.set_system_cursor("arrow")
            flayout.remove_widget(decrypt_button)
            savetext_button = Builder.load_string("""Button:
                                                        background_normal: ""
                                                        background_color: 0, 0.4, 0.5, 1
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.size
                                                        font_size: "18sp"
                                                        halign: "center"
                                                        valign: "center"
                                                        size_hint: 0.3, 0.075
                                                        pos_hint: {"top":0.75, "right":0.35}
                                                        text: "Entschlüsselten Text speichern"
                                                        """)
            passwort_input.is_focusable = False
            passwort_input.foreground_color = (0.6, 0.6, 0.6, 1)
            dateiname_input.is_focusable = False
            dateiname_input.foreground_color = (0.6, 0.6, 0.6, 1)
            savetext_button.bind(on_press = lambda x: save_decrypted_text())
            flayout.add_widget(savetext_button)



        def decrypt():
            global plaintext, decrypt_filename
            Window.set_system_cursor("wait")
            if feature == "dropdown3_1_menu":
                decrypt_password = passwort_input.text
                decrypt_filename = dateiname_input.text
                try:
                    with open(f"Verschlüsselte Dateien\\{decrypt_filename}.txt", "rb") as file:
                        nonce = file.read(16)
                        mactag = file.read(16)
                        salt = file.read(16)
                        key = PBKDF2(decrypt_password, salt, 32, count = 1000000, hmac_hash_module = SHA512)
                        ciphertext = file.read()
                        file.close()
                    cipher = AES.new(key, AES.MODE_EAX, nonce = nonce)

                except FileNotFoundError:
                    Window.set_system_cursor("arrow")
                    content = Builder.load_string("""Label:
                                                        text: 'Die gewünschte Datei existiert nicht! Kontrollieren Sie den Dateinamen.'

                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.width, None
                                                        font_size: "18sp"
                                                        size_hint: 1, None
                                                        height: self.texture_size[1]
                                                        valign: "center"
                                                        pos_hint: {"top":0.9, "right":1}
                                                        """)
                    ok_button = Builder.load_string("""Button:
                                                        background_normal: ""
                                                        background_color: 0, 0.4, 0.5, 1
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.size
                                                        font_size: "18sp"
                                                        halign: "center"
                                                        valign: "center"
                                                        size_hint: 0.3, 0.2
                                                        pos_hint: {"top":0.25, "right":0.9}
                                                        text: "OK"
                                                        """)
                    widget_float = Builder.load_string("""FloatLayout:
                                                            size_hint: 1, 1
                                                            pos_hint: {"top":1, "right":1}
                                                            """)
                    widget_float.add_widget(ok_button)
                    widget_float.add_widget(content)

                    popup_exception = Builder.load_string("""Popup:
                                                                title: "Datei nicht gefunden"
                                                                size_hint: 0.3, 0.4
                                                                pos_hint: {"middle":1, "center":1}
                                                                separator_color: 0, 0.4, 0.5, 1
                                                                title_size: "18sp"
                                                                title_font: "MPLUSRounded1c-Medium.ttf"
                                                                auto_dismiss: False
                                                                """)

                    popup_exception.content = widget_float
                    ok_button.bind(on_press = lambda x: popup_exception.dismiss())
                    popup_exception.open()
                    return
            else:
                decrypt_password = passwort_input.text
                decrypt_filename = filename2.decode()
                with open(filename2, "rb") as file:
                    nonce = file.read(16)
                    mactag = file.read(16)
                    salt = file.read(16)
                    key = PBKDF2(decrypt_password, salt, 32, count = 1000000, hmac_hash_module = SHA512)
                    ciphertext = file.read()
                    file.close()
                cipher = AES.new(key, AES.MODE_EAX, nonce = nonce)
            try:
                plaintext = cipher.decrypt_and_verify(ciphertext, mactag)
                after_decrypting()
            except ValueError:
                Window.set_system_cursor("arrow")
                content = Builder.load_string("""Label:
                                                    text: 'Das Passwort ist falsch oder die Datei wurde manipuliert! Geben Sie das Passwort erneut ein oder informieren Sie sich unter "Hilfe" über Manipulation von Dateien.'

                                                    font_name: "MPLUSRounded1c-Medium.ttf"
                                                    text_size: self.width, None
                                                    font_size: "18sp"
                                                    size_hint: 1, None
                                                    height: self.texture_size[1]
                                                    valign: "center"
                                                    pos_hint: {"top":0.9, "right":1}
                                                    """)
                ok_button = Builder.load_string("""Button:
                                                        background_normal: ""
                                                        background_color: 0, 0.4, 0.5, 1
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.size
                                                        font_size: "18sp"
                                                        halign: "center"
                                                        valign: "center"
                                                        size_hint: 0.3, 0.2
                                                        pos_hint: {"top":0.25, "right":0.9}
                                                        text: "OK"
                                                        """)
                widget_float = Builder.load_string("""FloatLayout:
                                                            size_hint: 1, 1
                                                            pos_hint: {"top":1, "right":1}
                                                            """)
                widget_float.add_widget(ok_button)
                widget_float.add_widget(content)

                popup_exception = Builder.load_string("""Popup:
                                                            title: "Fehler aufgetreten"
                                                            size_hint: 0.3, 0.4
                                                            pos_hint: {"middle":1, "center":1}
                                                            separator_color: 0, 0.4, 0.5, 1
                                                            title_size: "18sp"
                                                            title_font: "MPLUSRounded1c-Medium.ttf"
                                                            auto_dismiss: False
                                                            """)
                popup_exception.content = widget_float
                ok_button.bind(on_press = lambda x: popup_exception.dismiss())
                popup_exception.open()


        def create_password(passwort_input, passwort_bestaetigung_input, passwort_canvas, save_button):
            global password, check_image
            if passwort_input.text == "":
                content = Builder.load_string("""Label:
                                                        text: 'Erstellen Sie erst ein Passwort und klicken Sie dann auf "Fertig"!'
    
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.width, None
                                                        font_size: "18sp"
                                                        size_hint: 1, None
                                                        height: self.texture_size[1]
                                                        valign: "center"
                                                        pos_hint: {"top":0.9, "right":1}
                                                        """)
                ok_button = Builder.load_string("""Button:
                                                        background_normal: ""
                                                        background_color: 0, 0.4, 0.5, 1
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.size
                                                        font_size: "18sp"
                                                        halign: "center"
                                                        valign: "center"
                                                        size_hint: 0.3, 0.2
                                                        pos_hint: {"top":0.25, "right":0.9}
                                                        text: "OK"
                                                        """)
                widget_float = Builder.load_string("""FloatLayout:
                                                            size_hint: 1, 1
                                                            pos_hint: {"top":1, "right":1}
                                                            """)
                widget_float.add_widget(ok_button)
                widget_float.add_widget(content)

                popup = Builder.load_string("""Popup:
                                                    title: "Kein Passwort erstellt!"
                                                    size_hint: 0.3, 0.4
                                                    pos_hint: {"middle":1, "center":1}
                                                    separator_color: 0, 0.4, 0.5, 1
                                                    title_size: "18sp"
                                                    title_font: "MPLUSRounded1c-Medium.ttf"
                                                    auto_dismiss: False
                                                    """)
                popup.content = widget_float
                ok_button.bind(on_press=lambda x: popup.dismiss())

                popup.open()
            elif passwort_input.text != passwort_bestaetigung_input.text:
                content = Builder.load_string("""Label:
                                                    text: "Passwort und Passwort-Bestätigung stimmen nicht überein. Geben Sie Ihr Passwort erneut ein!"
                                                   
                                                    font_name: "MPLUSRounded1c-Medium.ttf"
                                                    text_size: self.width, None
                                                    font_size: "18sp"
                                                    size_hint: 1, None
                                                    height: self.texture_size[1]
                                                    valign: "center"
                                                    pos_hint: {"top":0.9, "right":1}
                                                    """)
                ok_button = Builder.load_string("""Button:
                                                        background_normal: ""
                                                        background_color: 0, 0.4, 0.5, 1
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.size
                                                        font_size: "18sp"
                                                        halign: "center"
                                                        valign: "center"
                                                        size_hint: 0.3, 0.2
                                                        pos_hint: {"top":0.25, "right":0.9}
                                                        text: "OK"
                                                        """)
                widget_float = Builder.load_string("""FloatLayout:
                                                    size_hint: 1, 1
                                                    pos_hint: {"top":1, "right":1}
                                                    """)
                widget_float.add_widget(ok_button)
                widget_float.add_widget(content)

                popup = Builder.load_string("""Popup:
                                                    title: "Keine Übereinstimmung!"
                                                    size_hint: 0.3, 0.4
                                                    pos_hint: {"middle":1, "center":1}
                                                    separator_color: 0, 0.4, 0.5, 1
                                                    title_size: "18sp"
                                                    title_font: "MPLUSRounded1c-Medium.ttf"
                                                    auto_dismiss: False
                                                    """)
                popup.content = widget_float
                ok_button.bind(on_press = lambda x: popup.dismiss())

                popup.open()
            else:
                passwort_canvas.remove_widget(save_button)
                check_image = Builder.load_string("""Image:
                                                        source: "check4.png"
                                                        size_hint_x: 0.15
                                                        size_hint_y: 0.15
                                                        pos_hint: {"top":0.25, "right":0.9}
                                                        """)
                passwort_canvas.add_widget(check_image)
                password = passwort_input.text

        def auge_change():
            if auge.source == "auge_zu.png":
                auge.source = "auge_offen.png"
                passwort_input.password = False
                if feature == "dropdown3_1_menu" or feature == "dropdown3_2_menu":
                    pass
                else:
                    passwort_bestaetigung_input.password = False
            else:
                auge.source = "auge_zu.png"
                passwort_input.password = True
                if feature == "dropdown3_1_menu" or feature == "dropdown3_2_menu":
                    pass
                else:
                    passwort_bestaetigung_input.password = True


        def dropdown2_1_menu():
            global passwort_canvas, password, file_name_input, feature, encrypt_button, text_input, auge, passwort_input, passwort_bestaetigung_input
            password = None
            feature = "dropdown2_1_menu"
            flayout.clear_widgets()
            self.remove_widget(dropdown2)
            text_input = Builder.load_string("""TextInput:
                                                    hint_text: "Geben Sie hier einen Text ein, den Sie verschlüsseln wollen."
                                                    size_hint: 0.5, 0.5
                                                    pos_hint: {"top":0.65, "right":0.9}
                                                    font_name: "MPLUSRounded1c-Medium.ttf"
                                                    font_size: "18sp"
                                                    """)
            encrypt_button = Builder.load_string(("""Button:
                                                        background_normal: ""
                                                        background_color: 0, 0.4, 0.5, 1
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.size
                                                        font_size: "18sp"
                                                        halign: "center"
                                                        valign: "center"
                                                        size_hint: 0.3, 0.075
                                                        pos_hint: {"top":0.75, "right":0.9}
                                                        text: "Text verschlüsseln und speichern"
                                                        """))
            encrypt_button_img1 = Builder.load_string("""Image:
                                                            source: "key.png"
                                                            size_hint: 0.035, 0.07
                                                            pos_hint: {"top":0.745, "right":0.64}
                                                            """)
            encrypt_button_img2 = Builder.load_string("""Image:
                                                            source: "diskette.png"
                                                            size_hint: 0.04, 0.07
                                                            pos_hint: {"top":0.745, "right":0.899}
                                                            """)
            file_name_input = Builder.load_string("""TextInput:
                                                        hint_text: "filename"
                                                        size_hint: 0.9, 0.4
                                                        pos_hint: {"top":0.5, "right":0.95}
                                                        padding: [3, (self.height-self.line_height)/2]
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        font_size: "18sp"
                                                        multiline: False
                                                        """)
            file_name_input_label = Builder.load_string("""Label:
                                                                background_normal: ""
                                                                background_color: 0, 0.4, 0.5, 1
                                                                font_name: "MPLUSRounded1c-Medium.ttf"
                                                                text_size: self.size
                                                                font_size: "18sp"
                                                                halign: "center"
                                                                valign: "center"
                                                                size_hint: 1, 0.3
                                                                pos_hint: {"top":0.9, "right":1}
                                                                text: "Dateinamen festlegen:"
                                                                """)
            passwort_canvas = Builder.load_file("passwort_canvas.kv")
            filename_canvas = Builder.load_file("filename_canvas.kv")
            flayout.add_widget(filename_canvas)
            flayout.add_widget(passwort_canvas)

            passwort_label = Builder.load_string("""Label:
                                                        background_normal: ""
                                                        background_color: 0, 0.4, 0.5, 1
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.size
                                                        font_size: "18sp"
                                                        halign: "center"
                                                        valign: "center"
                                                        size_hint: 1, 0.2
                                                        pos_hint: {"top":0.95, "right":1}
                                                        text: "Passwort festlegen:"
                                                        """)
            passwort_input = Builder.load_string("""TextInput:
                                                        hint_text: "abcd1234"
                                                        size_hint: 0.75, 0.1
                                                        pos_hint: {"top":0.75, "right":0.8}
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        padding: [3, (self.height-self.line_height)/2]
                                                        font_size: "18sp"
                                                        password: True
                                                        multiline: False
                                                        """)

            passwort_bestaetigung_label = Builder.load_string("""Label:
                                                                    background_normal: ""
                                                                    background_color: 0, 0.4, 0.5, 1
                                                                    font_name: "MPLUSRounded1c-Medium.ttf"
                                                                    text_size: self.size
                                                                    font_size: "18sp"
                                                                    halign: "center"
                                                                    valign: "center"
                                                                    size_hint: 1, 0.2
                                                                    pos_hint: {"top":0.6, "right":1}
                                                                    text: "Passwort bestätigen:"
                                                                    """)
            passwort_bestaetigung_input = Builder.load_string("""TextInput:
                                                                    hint_text: "abcd1234"
                                                                    padding: [3, (self.height-self.line_height)/2]
                                                                    size_hint: 0.75, 0.1
                                                                    pos_hint: {"top":0.4, "right":0.8}
                                                                    font_name: "MPLUSRounded1c-Medium.ttf"
                                                                    font_size: "18sp"
                                                                    password: True
                                                                    multiline: False
                                                                    """)

            save_button = Builder.load_string("""Button:
                                                    background_normal: ""
                                                    background_color: 1, 1, 1, 1
                                                    color: 0, 0, 0, 1
                                                    font_name: "MPLUSRounded1c-Medium.ttf"
                                                    text_size: self.size
                                                    font_size: "18sp"
                                                    halign: "center"
                                                    valign: "center"
                                                    size_hint: 0.35, 0.1
                                                    pos_hint: {"top":0.2, "right":0.9}
                                                    text: "Fertig"
                                                    """)
            auge_btn = Builder.load_string("""Button:
                                                background_normal: ""
                                                background_color: 0, 0.4, 0.5, 1
                                                size_hint: 0.15, 0.1
                                                pos_hint: {"top":0.75, "right":0.97}                                                        
                                                """)
            auge = Builder.load_string("""Image:
                                            source: "auge_zu.png"
                                            size_hint: 0.15, 0.1
                                            pos_hint: {"top":0.75, "right":0.97}
                                            """)


            flayout.add_widget(text_input)
            flayout.add_widget(encrypt_button)
            flayout.add_widget(encrypt_button_img1)
            flayout.add_widget(encrypt_button_img2)
            filename_canvas.add_widget(file_name_input)
            filename_canvas.add_widget(file_name_input_label)
            passwort_canvas.add_widget(passwort_label)
            passwort_canvas.add_widget(passwort_input)
            passwort_canvas.add_widget(passwort_bestaetigung_input)
            passwort_canvas.add_widget(passwort_bestaetigung_label)
            passwort_canvas.add_widget(save_button)
            passwort_canvas.add_widget(auge_btn)
            passwort_canvas.add_widget(auge)
            def encrypt_prep_prep():

                encrypt_prep(file_name_input.text, text_input.text)

            encrypt_button.bind(on_press = lambda x: encrypt_prep_prep())
            save_button.bind(on_press = lambda x: create_password(passwort_input, passwort_bestaetigung_input,
                                                                  passwort_canvas, save_button))
            auge_btn.bind(on_press = lambda x: auge_change())


        def dropdown2_2_menu():
            global feature

            def handledrops(self, filename):
                if drop_rect.collide_point(*Window.mouse_pos): # if a file is dropped in the widget
                    if filename[-3:].decode() == "txt":
                        drop_rect.clear_widgets()
                        doc_img = Builder.load_string("""Image:
                                                            source: "document.png"
                                                            size_hint: 0.5, 0.5
                                                            pos_hint: {"top":0.75, "right":0.4}
                                                            """)
                        drop_rect.add_widget(doc_img)
                        doc_label = Builder.load_string("""Label:
                                                                background_normal: ""
                                                                background_color: 1, 1, 1, 1
                                                                color: 0, 0, 0, 1
                                                                font_name: "MPLUSRounded1c-Medium.ttf"
                                                                text_size: self.size
                                                                font_size: "18sp"
                                                                halign: "center"
                                                                valign: "center"
                                                                size_hint: 0.5, 0.2
                                                                pos_hint: {"top":0.6, "right":0.75}
                                                                """)
                        doc_label.text = filename.decode()
                        drop_rect.add_widget(doc_label)



                        with open(filename, "r", encoding="utf-8") as f:
                            get_message = f.read()
                        encrypt_button.bind(on_press = lambda x: encrypt_prep(file_name_input.text, get_message))




                    else:
                        content = Builder.load_string("""Label:
                                                              text: "Die Textdatei muss die Dateiendung .txt besitzen!"
    
                                                              font_name: "MPLUSRounded1c-Medium.ttf"
                                                              text_size: self.width, None
                                                              font_size: "18sp"
                                                              size_hint: 1, None
                                                              height: self.texture_size[1]
                                                              valign: "center"
                                                              pos_hint: {"top":0.9, "right":1}
                                                              """)
                        ok_button = Builder.load_string("""Button:
                                                              background_normal: ""
                                                              background_color: 0, 0.4, 0.5, 1
                                                              font_name: "MPLUSRounded1c-Medium.ttf"
                                                              text_size: self.size
                                                              font_size: "18sp"
                                                              halign: "center"
                                                              valign: "center"
                                                              size_hint: 0.3, 0.2
                                                              pos_hint: {"top":0.25, "right":0.9}
                                                              text: "OK"
                                                              """)
                        widget_float = Builder.load_string("""FloatLayout:
                                                                  size_hint: 1, 1
                                                                  pos_hint: {"top":1, "right":1}
                                                                  """)
                        widget_float.add_widget(ok_button)
                        widget_float.add_widget(content)

                        popup = Builder.load_string("""Popup:
                                                          title: "Falsches Dateiformat!"
                                                          size_hint: 0.3, 0.4
                                                          pos_hint: {"middle":1, "center":1}
                                                          separator_color: 0, 0.4, 0.5, 1
                                                          title_size: "18sp"
                                                          title_font: "MPLUSRounded1c-Medium.ttf"
                                                          auto_dismiss: False
                                                          """)
                        popup.content = widget_float
                        ok_button.bind(on_press=lambda x: popup.dismiss())

                        popup.open()

            flayout.clear_widgets()
            self.remove_widget(dropdown2)
            dropdown2_1_menu()
            Clock.schedule_once(lambda x: flayout.remove_widget(text_input))
            feature = "dropdown2_2_menu"
            drop_rect = Builder.load_file("drop_rect_canvas.kv")
            flayout.add_widget(drop_rect)


            Window.bind(on_dropfile=handledrops)
            drop_label = Builder.load_string("""Label:
                                                    background_normal: ""
                                                    background_color: 1, 1, 1, 1
                                                    color: 0, 0, 0, 1
                                                    font_name: "MPLUSRounded1c-Medium.ttf"
                                                    text_size: self.size
                                                    font_size: "18sp"
                                                    halign: "center"
                                                    valign: "center"
                                                    size_hint: 1, 0.2
                                                    pos_hint: {"top":0.95, "right":1}
                                                    text: "Ziehen Sie eine Textdatei, die Sie verschlüsseln möchten, in dieses Feld!"
                                                    """)
            drop_img = Builder.load_string("""Image:
                                                    source: "drop.png"
                                                    size_hint: 0.45, 0.7
                                                    pos_hint: {"top":0.75, "right":0.725}
                                                    """)
            drop_rect.add_widget(drop_label)
            drop_rect.add_widget(drop_img)


        def dropdown3_1_menu():
            global auge,  passwort_input, feature, text_input, decrypt_password, decrypt_filename, dateiname_input, decrypt_button, password_label_canvas
            flayout.clear_widgets()
            self.remove_widget(dropdown3)
            feature = "dropdown3_1_menu"
            text_input = Builder.load_string("""TextInput:
                                                    hint_text: 'Geben Sie das richtige Passwort und den Dateinamen ein und klicken sie auf "entschlüsseln", damit hier Ihr entschlüsselter Text erscheint.'
                                                    size_hint: 0.5, 0.8
                                                    pos_hint: {"top":0.85, "right":0.9}
                                                    font_name: "MPLUSRounded1c-Medium.ttf"
                                                    font_size: "18sp"
                                                    is_focusable: False
                                                    """) # is_focusable verhindert, dass das Text Input Widget fokussiert.

            flayout.add_widget(text_input)

            password_label_canvas = Builder.load_file("password_filename_canvas.kv")
            flayout.add_widget(password_label_canvas)

            passwort_label = Builder.load_string("""Label:
                                                        background_normal: ""
                                                        background_color: 0, 0.4, 0.5, 1
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.size
                                                        font_size: "18sp"
                                                        halign: "center"
                                                        valign: "center"
                                                        size_hint: 1, 0.2
                                                        pos_hint: {"top":0.95, "right":1}
                                                        text: "Passwort:"
                                                        """)
            passwort_input = Builder.load_string("""TextInput:
                                                        hint_text: "abcd1234"
                                                        size_hint: 0.75, 0.1
                                                        pos_hint: {"top":0.75, "right":0.8}
                                                        padding: [3, (self.height-self.line_height)/2]
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        font_size: "18sp"
                                                        password: True
                                                        multiline: False
                                                        """)

            dateiname_label = Builder.load_string("""Label:
                                                        background_normal: ""
                                                        background_color: 0, 0.4, 0.5, 1
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        padding: [3, (self.height-self.line_height)/2]
                                                        text_size: self.size
                                                        font_size: "18sp"
                                                        halign: "center"
                                                        valign: "center"
                                                        size_hint: 1, 0.2
                                                        pos_hint: {"top":0.6, "right":1}
                                                        text: "Dateiname:"
                                                        """)
            dateiname_input = Builder.load_string("""TextInput:
                                                        hint_text: "filename"
                                                        size_hint: 0.75, 0.1
                                                        pos_hint: {"top":0.4, "right":0.8}
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        padding: [3, (self.height-self.line_height)/2]
                                                        font_size: "18sp"
                                                        multiline: False
                                                        """)

            auge_btn = Builder.load_string("""Button:
                                                    background_normal: ""
                                                    background_color: 0, 0.4, 0.5, 1
                                                    size_hint: 0.15, 0.1
                                                    pos_hint: {"top":0.75, "right":0.97}                                                        
                                                    """)
            auge = Builder.load_string("""Image:
                                                source: "auge_zu.png"
                                                size_hint: 0.15, 0.1
                                                pos_hint: {"top":0.75, "right":0.97}
                                                """)

            decrypt_button = Builder.load_string(("""Button:
                                                        background_normal: ""
                                                        background_color: 0, 0.4, 0.5, 1
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.size
                                                        font_size: "18sp"
                                                        halign: "center"
                                                        valign: "center"
                                                        size_hint: 0.3, 0.075
                                                        pos_hint: {"top":0.75, "right":0.35}
                                                        text: "Datei entschlüsseln"
                                                        """))
            flayout.add_widget(decrypt_button)
            password_label_canvas.add_widget(passwort_label)
            password_label_canvas.add_widget(passwort_input)
            password_label_canvas.add_widget(dateiname_label)
            password_label_canvas.add_widget(dateiname_input)
            password_label_canvas.add_widget(auge_btn)
            password_label_canvas.add_widget(auge)
            auge_btn.bind(on_press = lambda x: auge_change())



            decrypt_button.bind(on_press = lambda x: decrypt())

        def dropdown3_2_menu():
            global feature, auge, passwort_input

            def handledrops(self, filename):
                global filename2
                filename2 = filename
                if drop_rect.collide_point(*Window.mouse_pos):  # if a file is dropped in the widget
                    if filename[-3:].decode() == "txt":
                        drop_rect.clear_widgets()
                        doc_img = Builder.load_string("""Image:
                                                            source: "document.png"
                                                            size_hint: 0.5, 0.5
                                                            pos_hint: {"top":0.75, "right":0.45}
                                                            """)
                        drop_rect.add_widget(doc_img)
                        doc_label = Builder.load_string("""Label:
                                                                background_normal: ""
                                                                background_color: 1, 1, 1, 1
                                                                color: 0, 0, 0, 1
                                                                font_name: "MPLUSRounded1c-Medium.ttf"
                                                                text_size: self.size
                                                                font_size: "18sp"
                                                                halign: "center"
                                                                valign: "center"
                                                                size_hint: 0.5, 0.2
                                                                pos_hint: {"top":0.6, "right":0.9}
                                                                """)
                        doc_label.text = filename.decode()
                        drop_rect.add_widget(doc_label)


                    else:
                        content = Builder.load_string("""Label:
                                                              text: "Die Textdatei muss die Dateiendung .txt besitzen!"

                                                              font_name: "MPLUSRounded1c-Medium.ttf"
                                                              text_size: self.width, None
                                                              font_size: "18sp"
                                                              size_hint: 1, None
                                                              height: self.texture_size[1]
                                                              valign: "center"
                                                              pos_hint: {"top":0.9, "right":1}
                                                              """)
                        ok_button = Builder.load_string("""Button:
                                                              background_normal: ""
                                                              background_color: 0, 0.4, 0.5, 1
                                                              font_name: "MPLUSRounded1c-Medium.ttf"
                                                              text_size: self.size
                                                              font_size: "18sp"
                                                              halign: "center"
                                                              valign: "center"
                                                              size_hint: 0.3, 0.2
                                                              pos_hint: {"top":0.25, "right":0.9}
                                                              text: "OK"
                                                              """)
                        widget_float = Builder.load_string("""FloatLayout:
                                                                  size_hint: 1, 1
                                                                  pos_hint: {"top":1, "right":1}
                                                                  """)
                        widget_float.add_widget(ok_button)
                        widget_float.add_widget(content)

                        popup = Builder.load_string("""Popup:
                                                          title: "Falsches Dateiformat!"
                                                          size_hint: 0.3, 0.4
                                                          pos_hint: {"middle":1, "center":1}
                                                          separator_color: 0, 0.4, 0.5, 1
                                                          title_size: "18sp"
                                                          title_font: "MPLUSRounded1c-Medium.ttf"
                                                          auto_dismiss: False
                                                          """)
                        popup.content = widget_float
                        ok_button.bind(on_press = lambda x: popup.dismiss())

                        popup.open()

            flayout.clear_widgets()
            self.remove_widget(dropdown3)
            dropdown3_1_menu()
            feature = "dropdown3_2_menu"
            flayout.remove_widget(password_label_canvas)
            drop_rect = Builder.load_file("drop_rect_canvas2.kv")
            flayout.add_widget(drop_rect)

            Window.bind(on_dropfile = handledrops)
            drop_label = Builder.load_string("""Label:
                                                    background_normal: ""
                                                    background_color: 1, 1, 1, 1
                                                    color: 0, 0, 0, 1
                                                    font_name: "MPLUSRounded1c-Medium.ttf"
                                                    text_size: self.size
                                                    font_size: "18sp"
                                                    halign: "center"
                                                    valign: "center"
                                                    size_hint: 1, 0.2
                                                    pos_hint: {"top":0.95, "right":1}
                                                    text: "Ziehen Sie eine Textdatei, die Sie verschlüsseln möchten, in dieses Feld!"
                                                    """)
            drop_img = Builder.load_string("""Image:
                                                    source: "drop.png"
                                                    size_hint: 0.45, 0.7
                                                    pos_hint: {"top":0.75, "right":0.725}
                                                    """)
            drop_rect.add_widget(drop_label)
            drop_rect.add_widget(drop_img)
            drag_drop_password_canvas = Builder.load_file("drag_drop_pw_canvas.kv")
            flayout.add_widget(drag_drop_password_canvas)
            passwort_label = Builder.load_string("""Label:
                                                        background_normal: ""
                                                        background_color: 0, 0.4, 0.5, 1
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        text_size: self.size
                                                        font_size: "18sp"
                                                        halign: "center"
                                                        valign: "center"
                                                        size_hint: 0.3, 0.7
                                                        pos_hint: {"top":0.85, "right":0.3}
                                                        text: "Passwort:"
                                                        """)
            passwort_input = Builder.load_string("""TextInput:
                                                        hint_text: "abcd1234"
                                                        size_hint: 0.5, 0.7
                                                        pos_hint: {"top":0.85, "right":0.8}
                                                        font_name: "MPLUSRounded1c-Medium.ttf"
                                                        padding: [3, (self.height-self.line_height)/2]
                                                        font_size: "18sp"
                                                        password: True
                                                        multiline: False
                                                        """)
            drag_drop_password_canvas.add_widget(passwort_input)
            drag_drop_password_canvas.add_widget(passwort_label)

            auge_btn = Builder.load_string("""Button:
                                                background_normal: ""
                                                background_color: 0, 0.4, 0.5, 1
                                                size_hint: 0.15, 1
                                                pos_hint: {"top":1, "right":0.975}                                                        
                                                """)
            auge = Builder.load_string("""Image:
                                                source: "auge_zu.png"
                                                size_hint: 0.15, 1
                                                pos_hint: {"top":1, "right":0.975}
                                                """)
            drag_drop_password_canvas.add_widget(auge_btn)
            drag_drop_password_canvas.add_widget(auge)

            auge_btn.bind(on_press = lambda x: auge_change())



        def dropdown3_3_menu():
            flayout.clear_widgets()
            self.remove_widget(dropdown3)

        def projekt_menu():
            flayout.clear_widgets()
            logo_projekt = Builder.load_string("""Image:
                                                    source: "logo_original.png"
                                                    size_hint_x: 0.5
                                                    size_hint_y: 0.3
                                                    pos_hint: {"top":0.85, "right":0.75}                                                        
                                                    """)
            text_label = Builder.load_string("""Label:
                                                    background_normal: ""
                                                    background_color: 0, 0.4, 0.5, 1
                                                    font_name: "MPLUSRounded1c-Medium.ttf"
                                                    color: 0, 0.4, 0.5, 1
                                                    text_size: self.size
                                                    font_size: "18sp"
                                                    halign: "center"
                                                    valign: "center"
                                                    size_hint_x: 0.9
                                                    pos_hint: {"top":0.8, "right":0.95}
                                                    """)


            with open("projekt_text.txt", encoding = "utf-8") as pfile:
                text_label.text = pfile.read()
                pfile.close()

            flayout.add_widget(logo_projekt)
            flayout.add_widget(text_label)

        def hilfe_menu():
            flayout.clear_widgets()
            logo_projekt = Builder.load_string("""Image:
                                                    source: "logo_original.png"
                                                    size_hint_x: 0.5
                                                    size_hint_y: 0.3
                                                    pos_hint: {"top":0.85, "right":0.75}                                                        
                                                    """)
            text_label = Builder.load_string("""Label:
                                                    background_normal: ""
                                                    background_color: 0, 0.4, 0.5, 1
                                                    font_name: "MPLUSRounded1c-Medium.ttf"
                                                    color: 0, 0.4, 0.5, 1
                                                    text_size: self.size
                                                    font_size: "18sp"
                                                    halign: "center"
                                                    valign: "center"
                                                    size_hint_x: 0.9
                                                    pos_hint: {"top":0.8, "right":0.95}
                                                    """)

            with open("hilfe_text.txt", encoding = "utf-8") as hfile:
                text_label.text = hfile.read()
                hfile.close()

            flayout.add_widget(logo_projekt)
            flayout.add_widget(text_label)

        auswahl_gridLayout = Builder.load_string("""GridLayout:
                                                        cols: 5
                                                        rows: 1
                                                        size_hint: 1, 0.1
                                                        pos_hint: {"top":1, "right":1}
                                                        spacing: 2""")
        uebersicht_tbutton = Builder.load_string("""ToggleButton:
                                                        background_normal: ""
                                                        background_color: 0, 0.4, 0.5, 1
                                                        font_name: "MPLUSRounded1c-Bold.ttf"
                                                        text_size: self.size
                                                        font_size: "18sp"
                                                        halign: "center"
                                                        valign: "center"
                                                        group: "panel"
                                                        text: "Home"
                                                        state: "normal"
                                                        allow_no_selection: False
                                                        """)
        verschluesseln_tbutton = Builder.load_string("""ToggleButton:
                                                            background_normal: ""
                                                            background_color: 0, 0.4, 0.5, 1
                                                            font_name: "MPLUSRounded1c-Bold.ttf"
                                                            text_size: self.size
                                                            font_size: "18sp"
                                                            halign: "center"
                                                            valign: "center"                                                        
                                                            group: "panel"
                                                            text: "Verschlüsseln"
                                                            state: "normal"
                                                            allow_no_selection: False
                                                            """)
        entschluesseln_tbutton = Builder.load_string("""ToggleButton:
                                                            background_normal: ""
                                                            background_color: 0, 0.4, 0.5, 1
                                                            font_name: "MPLUSRounded1c-Bold.ttf"
                                                            text_size: self.size
                                                            font_size: "18sp"
                                                            halign: "center"
                                                            valign: "center"                                                        
                                                            group: "panel"
                                                            text: "Entschlüsseln"
                                                            state: "normal"
                                                            allow_no_selection: False
                                                            """)
        projekt_tbutton = Builder.load_string("""ToggleButton:
                                                    background_normal: ""
                                                    background_color: 0, 0.4, 0.5, 1
                                                    font_name: "MPLUSRounded1c-Bold.ttf"
                                                    text_size: self.size
                                                    font_size: "18sp"
                                                    halign: "center"
                                                    valign: "center"                                                        
                                                    group: "panel"
                                                    text: "Über das Projekt"
                                                    state: "normal"
                                                    allow_no_selection: False
                                                    """)
        hilfe_tbutton = Builder.load_string("""ToggleButton:
                                                    background_normal: ""
                                                    background_color: 0, 0.4, 0.5, 1
                                                    font_name: "MPLUSRounded1c-Bold.ttf"
                                                    text_size: self.size
                                                    font_size: "18sp"
                                                    halign: "center"
                                                    valign: "center"                                                        
                                                    group: "panel"
                                                    text: "Hilfe"
                                                    state: "normal"
                                                    allow_no_selection: False
                                                    """)
        dropdown2 = Builder.load_string("""DropDown:
                                                size_hint_x: 0.2
                                                size_hint_y: None
                                                height: 132
                                                pos_hint: {"top":0.9, "right":0.4}
                                                """)
        dropdown2_1 = Builder.load_string("""Button:
                                                text: "Neuer Text"
                                                size_hint_y: None
                                                font_name: "MPLUSRounded1c-Regular.ttf"
                                                text_size: self.size
                                                font_size: "18sp"
                                                halign: "center"
                                                valign: "center"
                                                height: "44sp"
                                                """)
        dropdown2_2 = Builder.load_string("""Button:
                                                text: "Drag and Drop"
                                                size_hint_y: None
                                                font_name: "MPLUSRounded1c-Regular.ttf"
                                                text_size: self.size
                                                font_size: "18sp"
                                                halign: "center"
                                                valign: "center"
                                                height: "44sp"
                                                """)

        dropdown2.add_widget(dropdown2_1)
        dropdown2.add_widget(dropdown2_2)


        dropdown3 = Builder.load_string("""DropDown:
                                                size_hint_x: 0.2
                                                size_hint_y: None
                                                height: 132
                                                pos_hint: {"top":0.9, "right":0.6}
                                                """)
        dropdown3_1 = Builder.load_string("""Button:
                                                text: "Dateiname"
                                                size_hint_y: None
                                                font_name: "MPLUSRounded1c-Regular.ttf"
                                                text_size: self.size
                                                font_size: "18sp"
                                                halign: "center"
                                                valign: "center"
                                                height: "44sp"
                                                """)
        dropdown3_2 = Builder.load_string("""Button:
                                                text: "Drag and Drop"
                                                size_hint_y: None
                                                font_name: "MPLUSRounded1c-Regular.ttf"
                                                text_size: self.size
                                                font_size: "18sp"
                                                halign: "center"
                                                valign: "center"
                                                height: "44sp"
                                                """)

        dropdown3.add_widget(dropdown3_1)
        dropdown3.add_widget(dropdown3_2)

        flayout = Builder.load_string("""FloatLayout:
                                                size_hint: 1, 1
                                                pos_hint: {"top":1, "right":1}
                                                """)


        self.add_widget(auswahl_gridLayout)
        self.add_widget(flayout)

        auswahl_gridLayout.add_widget(uebersicht_tbutton)
        auswahl_gridLayout.add_widget(verschluesseln_tbutton)
        auswahl_gridLayout.add_widget(entschluesseln_tbutton)
        auswahl_gridLayout.add_widget(projekt_tbutton)
        auswahl_gridLayout.add_widget(hilfe_tbutton)

        verschluesseln_tbutton.bind(on_release = lambda x: makedropdown())
        entschluesseln_tbutton.bind(on_release = lambda x: makedropdown_3())
        uebersicht_tbutton.bind(state = uebersicht_menu)
        uebersicht_tbutton.state = "down"
        projekt_tbutton.bind(on_release = lambda x: projekt_menu())
        hilfe_tbutton.bind(on_release = lambda x: hilfe_menu())
        dropdown2_1.bind(on_press = lambda x: dropdown2_1_menu())
        dropdown2_2.bind(on_press = lambda x: dropdown2_2_menu())
        dropdown3_1.bind(on_press = lambda x: dropdown3_1_menu())
        dropdown3_2.bind(on_press = lambda x: dropdown3_2_menu())


    pass





with open("canvas.kv", encoding="utf-8") as file:
    Builder.load_file("canvas.kv")
sm = ScreenManager()
startpage = Startpage()
sm.add_widget(startpage)
Window.maximize()


if __name__ == "__main__":
    MyApp().run()