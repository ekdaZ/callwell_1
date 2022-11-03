from crypt import methods
from distutils.dep_util import newer
from telnetlib import DO
from flask import Flask, render_template, request, send_from_directory
import os
from flask_bootstrap import Bootstrap
from main import traverse

 

app = Flask(__name__,template_folder='template')

#secret key

app.secret_key = 'Hello world'

Bootstrap(app)

#getcwd is locate current location

BASIC_PATH = os.getcwd()

#path where the files are stored

UPLOAD_PATH = os.path.join(BASIC_PATH, 'upload/')

DOWNLOAD_PATH = os.path.join(BASIC_PATH, 'modified_files/')


@app.route('/', methods=['POST', 'GET'])
def network():
    if request.method == 'POST':
        print("LINK CHECK")
        uploaded_xlsx = request.files['file']
        file_name = uploaded_xlsx.filename
        save_path = os.path.join(UPLOAD_PATH, file_name)
        uploaded_xlsx.save(save_path)
        new = file_name.split('.')
        del new[-1]
        new = ''.join(new)
        traverse(new)
        os.remove(UPLOAD_PATH + new + '.csv')
        return render_template('bounce.html',new = new)
        
    else:
        return render_template('template1.html')



@app.route('/download/<variable>/', methods=['POST', 'GET'])
def downloading(variable):
    return send_from_directory(DOWNLOAD_PATH, 'improved_' + variable + '.csv'), os.remove(DOWNLOAD_PATH + 'improved_' + variable + '.csv')
    # os.remove(DOWNLOAD_PATH + 'improved_' + variable + '.csv')
    # return render_template('template1.html')


if __name__ == '__main__':
    app.run(debug=True)