from flask import Flask, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
CSRFProtect(app)
app.config["UPLOAD_FOLDER"] = "UPLOADS"
app.config['SECRET_KEY'] = 'secret_key'
app.config['WTF_CSRF_ENABLED'] = True


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'dem', 'flt', 'tif', 'txt', 'csv', 'asc', 'grd', 'hgt', 'nc', 'png'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=['POST'])
def upload():
    file = request.files["file"]
    if file.filename == "":
        return jsonify({'message': 'upload failed'})
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': 'upload was successful'})
    else:
        print('no')
        return jsonify({'message': 'upload failed'})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
