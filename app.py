from flask import Flask,render_template,request
import requests,json

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('index.html')

@app.route("/response", methods=['POST','GET'])
def getvalues():

    #importing values
    if request.method =='POST':
        exam= str(request.form['exam'])
        input_dob= str(request.form['input_dob'])
        gender= str(request.form['gender'])
        preference= str(request.form['preference'])
    
        response = requests.get(f'https://api.upsceligibility.live/play?exam={exam}&gender={gender}&pref={preference}&dob={input_dob}')
        data= response.json()['Calculated attempts']

        return render_template('index.html',results=data)


if __name__=="__main__":
    app.run(port=8080)
