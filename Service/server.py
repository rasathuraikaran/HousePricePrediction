from flask import Flask ,request ,jsonify
import utill
app=Flask(__name__)


@app.route('/hello')
def hello():
    return "Hiii"


@app.route('/get_location_names')
def get_location_name():
    response = jsonify({
        'locations': utill.get_location_name()

    })
    #response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft =float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': utill.get_estimated_price(location,total_sqft,bath,bhk)

    })
    return response

if __name__ =="__main__":
    print("starting a python seerver for preditio")
    print(utill.get_location_name())
    app.run()
