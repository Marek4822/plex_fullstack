from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
from cred import flask_secret_key
from update_old import *
from refresh_plex import *
from view import *
from update_checker import *
from update import *


app = Flask(__name__)
app.secret_key = flask_secret_key


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.is_json:
        data = request.get_json()
        action = data.get('action')

        if action == 'refresh':
            flash('PLEX refreshed!', 'success')
            refresh()
            return jsonify({'status': 'success', 'message': 'PLEX refreshed!'}) 
        else:
            flash('Error', 'error')
            return jsonify({'status': 'failure', 'message': 'Invalid action'}), 400
        
    return render_template('index.html')
       

@app.route("/update_old", methods=['GET', 'POST'])
def update_old():
    if request.method == 'POST':
        playlist_id = request.form['playlist_id']
        dir_name = request.form['dir_name']

        if playlist_id and dir_name:
            update_app_old(playlist_id, dir_name)
            flash('Playlist updated!', 'success')
            return jsonify({'status': 'success', 'message': 'PLEX updated!'})
        else:
            print('none')
            flash('Error', 'error')
            return jsonify({'status': 'failure', 'message': 'Invalid action'}), 400


    return render_template('update_old.html')

@app.route("/update", methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        playlist_link = request.form['playlist_link']

        if playlist_link:
            if checker(playlist_link):
                update_app(playlist_link)
                flash('Playlist updated!', 'success')
                print(playlist_link)
            else:
                flash('Invalid link!', 'error')

        else:
            flash('Error: input is empty', 'error')

    return render_template('update.html')

@app.route("/view", methods=['GET', 'POST'])
def view():
    dir_list, count_dir = view_dir()
    print(dir_list)
    if request.method == 'POST':
        playlist = request.form['playlist']


        if playlist:
            file_list, count_file = view_file_list(playlist)
            flash('Playlist selected!', 'success')
            return render_template('view.html', select_list=dir_list, file_list=file_list, count_dir=count_dir, count_file=count_file)
        else:
            flash('Please select playlist!', 'error')


    return render_template('view.html', select_list=dir_list, count_dir=count_dir)    


if __name__ == "__main__":
    app.run(host='192.168.1.19', debug=True, port=2137)

