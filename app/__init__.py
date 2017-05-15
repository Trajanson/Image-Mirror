from flask import Flask, render_template, request, make_response,\
                  redirect, url_for, flash, send_file
from StringIO import StringIO
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash_message = """
                There has been an error in your image submission. \
                Please try again.
            """
            flash(flash_message)
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('Please select an image to upload.')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            img = StringIO(file.read())
            return send_file(img, mimetype=file.mimetype)

    return redirect('/')

@app.errorhandler(404)
def page_not_found(event):
    flash('Sorry, that page does not exist. You have been redirected home.')
    return redirect('/', code=302)
