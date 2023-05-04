from flask import Flask, render_template, request
import config as cf
from werkzeug.utils import secure_filename
import os
import requests

# Where you will save the images from form
LOCAL_FOLDER = 'C:\\Users\\losfr\\PycharmProjects\\Matriculas\\static\\cars'

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file2():
    return render_template('form.html')


@app.route('/process', methods=['GET', 'POST'])
def process():
    # Save img in /static/cars folder
    file = request.files['img']
    filename = secure_filename(file.filename)
    path = LOCAL_FOLDER
    file.save(os.path.join(path, filename))

    img = path + '\\' + filename
    request_url = cf.OPENALPR_CLOUD_API_URL + '&secret_key=' + cf.TOKEN
    # Files that contain the images to be analysed
    files = {'image': open(img, 'rb')}

    # OpenALPR request
    data = requests.post(request_url, files=files);

    # Analyse the obtained results
    plate, brand, model, color = cf.analyse_results(data.json())
    return render_template('car_data.html', img=filename, plate=plate, brand=brand, model=model, color=color)


if __name__ == '__main__':
    app.run(debug=True, port=8001)
