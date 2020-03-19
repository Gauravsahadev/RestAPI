from app import app

from flask import Flask, jsonify,send_file,request, redirect
import os
import sys
import subprocess
import urllib.request
import re
from werkzeug.utils import secure_filename

@app.route("/")
def index():
    return "API Running!"

UPLOAD_FOLDER = 'app/data/'
app.secret_key = '/\x8c\x9a\xadT\xdf\x1b\xf0\r\x87\xa9\x1aV\xd5\x04\xbc\x0c\xff|\x15\x0edmd'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'docx','doc'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_to(folder, source, timeout=None):
    args = [libreoffice_exec(), '--headless', '--convert-to', 'pdf', '--outdir', folder, source]

    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    filename = re.search('-> (.*?) using filter', process.stdout.decode())

    if filename is None:
        raise LibreOfficeError(process.stdout.decode())
    else:
        return filename.group(1)


def libreoffice_exec():
    # TODO: Provide support for more platforms
    if sys.platform == 'darwin':
        return '/Applications/LibreOffice.app/Contents/MacOS/soffice'
    return 'libreoffice'


class LibreOfficeError(Exception):
    def __init__(self, output):
        self.output = output

@app.route("/docx2pdf",methods=['POST'])
def docx2pdf():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		file=str(UPLOAD_FOLDER+filename)
		if os.path.isfile(file)==False:
			return jsonify({'message' : 'File not found in data/'})
		convert_to(UPLOAD_FOLDER, file)
		file_pdf='data/'+str(filename.split('.')[0])+'.pdf'
		return send_file(file_pdf, as_attachment=True,mimetype = "application/pdf",attachment_filename='download.pdf')
	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf, doc,docx'})
		resp.status_code = 400
		return resp