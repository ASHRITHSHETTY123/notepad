from flask import Flask, render_template, request, redirect
from git import Repo
import os

import glob




app = Flask(__name__)
repo = Repo(r"C:\Users\ASHRITH SHETTY\Desktop\MYNOTEPAD")

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/save', methods=['POST'])
def save():
    # note = request.form['note']
    # repo.git.add('.')
    # repo.index.commit(note)
    # new_file = repo.working_tree_dir + '/' + request.form['filename'] + '.txt'
    # with open(new_file, 'w') as f:
    #     f.write(note)
    # return redirect('/')
    note = request.form['note']
    filename = request.form['filename'] + '.txt'
    path = os.path.join(repo.working_tree_dir, filename)
    with open(path, 'w') as f:
        f.write(note)
    repo.index.add([path])
    repo.index.commit(request.form['note'])
    origin = repo.remote(name='origin')
    origin.push(refspec='{}:{}'.format('master','master'), set_upstream=True)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
