from flask import Flask, render_template, request
from waitress import serve
from calc import Convert

converter = Convert()

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Home page.
    '''
    return render_template('./index.html')


@app.route('/upload', methods=['POST'])
def upload():
    '''
    Upload page where the result of the calculation gets loaded
    '''
    if request.method != "POST":
        return render_template('./upload.html', error='Please upload a file.')
    
    form_data = request.form

    result = converter.convert_bill_share(int(form_data["total"]),int(form_data["share"]), int(form_data["bank"]))
    return render_template('./upload.html', result = result)


if __name__ == '__main__':
    print('Server running at http://localhost:8080')
    serve(app, host='0.0.0.0', port=8080)