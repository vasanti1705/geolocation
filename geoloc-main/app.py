from flask import *
import requests
import os

app = Flask(__name__)

# print(os.getenv(''))
api_key = os.environ.get('API_KEY')

api_endpoint = "https://api.ipgeolocation.io/ipgeo"

@app.route('/')
def get_geolocation():
    params = {
        'apiKey': api_key,
        'ip': ''    # IP can be left blank to get our current IP
    }
    ip = request.args.get('ip')
    if ip:
        params['ip']=ip

    response = requests.get(api_endpoint, params=params)
    
    if response.status_code == 200:
        data = response.json()
        # print(data)
        return render_template('home.html',data=data)
    else:
        return(response.json())
        # return render_template('error.html', error_code=response.status_code, error_message='IP does not exist.')

@app.route('/input')
def input_ip():
    return render_template('input.html')

@app.route('/', methods=['POST'])
def index():
    ip = request.form.get('ip')
    return redirect(url_for('get_geolocation', ip=ip))

app.run(debug=True)
