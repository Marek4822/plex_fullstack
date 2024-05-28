from flask import Flask, render_template, url_for, request, redirect, flash
from cred import flask_secret_key
from update import *
from view import *


app = Flask(__name__)
app.secret_key = flask_secret_key


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/update", methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        playlist_id = request.form['playlist_id']
        dir_name = request.form['dir_name']

        if playlist_id and dir_name:
            update_app(playlist_id, dir_name)
            flash('Playlist updated!', 'success')
        else:
            print('none')
            flash('Error', 'error')

    return render_template('update.html')

@app.route("/view", methods=['GET', 'POST'])
def view():
    select_list, count_dir = view_dir()

    if request.method == 'POST':

        view_option = request.form['option']

        if view_option == 'folders':
            dir_list, count_dir = view_dir()
            return render_template('view.html',select_list=select_list, dir_list=dir_list, count_dir=count_dir)    
        
        if view_option == 'files':
            playlist = request.form['playlist']
            print(playlist)
            file_list, count_file = view_file_list(playlist)
            return render_template('view.html',select_list=select_list, file_list=file_list, count_file=count_file)
        else:
            print('o_0')

    return render_template('view.html', select_list=select_list)    


if __name__ == "__main__":
    app.run(debug=True, port=2137)