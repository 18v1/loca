import telebot
from flask import Flask, request, send_from_directory, render_template_string, redirect, url_for
import threading
import socket
import os
import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

app = Flask(__name__)

FILE_DIRECTORY = '/sdcard/locaAdmin/fileloca'

# @lni34
def init_db():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'locaLCE?_$77loca')")
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return "Hello, this is a test server running on port 5001!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        c.execute(query)
        result = c.fetchone()
        conn.close()
        
        if result:
            return redirect(url_for('list_files'))
        else:
            return "Invalid username or password! Please try again.", 403
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Login</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #121212;
                    color: white;
                    font-family: Arial, sans-serif;
                    margin: 0;
                }
                .login-container {
                    background-color: #1e1e1e;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
                    text-align: center;
                }
                input[type="text"], input[type="password"] {
                    width: 100%;
                    padding: 10px;
                    margin: 10px 0;
                    border: 1px solid #333;
                    border-radius: 5px;
                    background-color: #333;
                    color: white;
                }
                input[type="submit"] {
                    width: 100%;
                    padding: 10px;
                    margin: 10px 0;
                    border: none;
                    border-radius: 5px;
                    background-color: #6200ea;
                    color: white;
                    font-size: 16px;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #3700b3;
                }
            </style>
        </head>
        <body>
            <div class="login-container">
                <h2>Login</h2>
                <form method="post">
                    <input type="text" name="username" placeholder="Username" required><br>
                    <input type="password" name="password" placeholder="Password" required><br>
                    <input type="submit" value="Login">
                </form>
            </div>
        </body>
        </html>
    '''

@app.route('/files', methods=['GET', 'POST'])
def list_files():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username != 'admin' or password!='locaLCE?_$77loca':
            return "Invalid username or password! Please try again.", 403
    else:
        return '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Files</title>
                <style>
                    body {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        background-color: #121212;
                        color: white;
                        font-family: Arial, sans-serif;
                        margin: 0;
                    }
                    .login-container {
                        background-color: #1e1e1e;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
                        text-align: center;
                    }
                    input[type="text"], input[type="password"] {
                        width: 100%;
                        padding: 10px;
                        margin: 10px 0;
                        border: 1px solid #333;
                        border-radius: 5px;
                        background-color: #333;
                        color: white;
                    }
                    input[type="submit"] {
                        width: 100%;
                        padding: 10px;
                        margin: 10px 0;
                        border: none;
                        border-radius: 5px;
                        background-color: #6200ea;
                        color: white;
                        font-size: 16px;
                        cursor: pointer.
                    }
                    input[type="submit"]:hover {
                        background-color: #3700b3;
                    }
                </style>
            </head>
            <body>
                <div class="login-container">
                    <h2>Files</h2>
                    <form method="post">
                        <input type="text" name="username" placeholder="Username" required><br>
                        <input type="password" name="password" placeholder="Password" required><br>
                        <input type="submit" value="Login">
                    </form>
                </div>
            </body>
            </html>
        '''
    
    files = os.listdir(FILE_DIRECTORY)
    file_links = []
    for file in files:
        if file == 'locaadmin':
            file_links.append(f'<a href="{url_for("protected_file", filename=file)}">locaadmin</a>')
        else:
            file_links.append(f'<a href="{url_for("download_file", filename=file)}">{file}</a>')
    return render_template_string('<br>'.join(file_links))

@app.route('/files/<filename>', methods=['GET', 'POST'])
def download_file(filename):
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username != 'admin' or password != 'locaLCE?_$77loca':
            return "Invalid username or password! Please try again.", 403
    else:
        return '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Download File</title>
                <style>
                    body {
                        display: flex;
                        justify-content: center.
                        align-items: center.
                        height: 100vh.
                        background-color: #121212.
                        color: white.
                        font-family: Arial, sans-serif.
                        margin: 0.
                    }
                    .login-container {
                        background-color: #1e1e1e.
                        padding: 20px.
                        border-radius: 10px.
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.5).
                        text-align: center.
                    }
                    input[type="text"], input[type="password"] {
                        width: 100%.
                        padding: 10px.
                        margin: 10px 0.
                        border: 1px solid #333.
                        border-radius: 5px.
                        background-color: #333.
                        color: white.
                    }
                    input[type="submit"] {
                        width: 100%.
                        padding: 10px.
                        margin: 10px 0.
                        border: none.
                        border-radius: 5px.
                        background-color: #6200ea.
                        color: white.
                        font-size: 16px.
                        cursor: pointer.
                    }
                    input[type="submit"]:hover {
                        background-color: #3700b3.
                    }
                </style>
            </head>
            <div class="login-container">
                    <h2>Download File</h2>
                    <form method="post">
                        <input type="text" name="username" placeholder="Username" required><br>
                        <input type="password" name="password" placeholder="Password" required><br>
                        <input type="submit" value="Login">
                    </form>
                </div>
            </body>
            </html>
        '''
    
    return send_from_directory(FILE_DIRECTORY, filename)

@app.route('/protected/locaadmin')
def protected_file():
    return '''
    <html>
    <body>
        <h2>Sorry, this file is protected and cannot be downloaded.</h2>
    </body>
    </html>
    '''

# إعداد Kivy للواجهة
class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.token_label = Label(text="Enter Telegram Bot Token:")
        self.token_input = TextInput(multiline=False)
        self.add_widget(self.token_label)
        self.add_widget(self.token_input)

        self.save_token_button = Button(text="Save Token", on_press=self.save_token)
        self.add_widget(self.save_token_button)

        self.start_server_button = Button(text="Start Server", on_press=self.start_server)
        self.add_widget(self.start_server_button)

        self.console_output = Label(text="Output will be shown here", size_hint_y=None, height=200)
        self.add_widget(self.console_output)

    def save_token(self, instance):
        token = self.token_input.text
        with open("token.txt", "w") as token_file:
            token_file.write(token)
        popup = Popup(title='Token Saved',
                      content=Label(text='The token has been saved successfully.'),
                      size_hint=(0.6, 0.4))
        popup.open()

    def start_server(self, instance):
        token = None
        try:
            with open("token.txt", "r") as token_file:
                token = token_file.read()
        except FileNotFoundError:
            popup = Popup(title='Token Not Found',
                          content=Label(text='Please save the token before starting the server.'),
                          size_hint=(0.6, 0.4))
            popup.open()
            return

        def run_flask():
            bot = telebot.TeleBot(token)
            ip_address = socket.gethostbyname(socket.gethostname())
            message = f"Server is running at http://{ip_address}:5001/files"
            bot.send_message(chat_id='7259803875', text=message)
            self.console_output.text += f"\n{message}"
            app.run(host='0.0.0.0', port=5001, threaded=True)

        threading.Thread(target=run_flask).start()
        popup = Popup(title='Server Started',
                      content=Label(text='The server has started successfully.'),
                      size_hint=(0.6, 0.4))
        popup.open()

class MainApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    MainApp().run()
