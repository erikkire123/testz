from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    uploaded_files = os.listdir('uploads')
    return render_template('HtmlFile.html', files=uploaded_files, os=os)

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = os.path.join('uploads', uploaded_file.filename)
        uploaded_file.save(file_path)
        return redirect(url_for('index'))
    return "No file selected."

if __name__ == '__main__':
    app.run(debug=True)
