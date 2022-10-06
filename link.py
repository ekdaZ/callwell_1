from crypt import methods
from flask import Flask, render_template, request
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



@app.route('/', methods=['POST', 'GET'])
def network():
    if request.method == 'POST':
        uploaded_xlsx = request.files['file']
        file_name = uploaded_xlsx.filename
        save_path = os.path.join(UPLOAD_PATH, file_name)
        uploaded_xlsx.save(save_path)
        print(file_name, "Uploaded Successfully")
        traverse(file_name)
    else:
        return render_template('template1.html')

        

if __name__ == '__main__':
    app.run(debug=True)