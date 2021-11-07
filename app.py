from flask import Flask,render_template,request
import requests

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
        print(exam,input_dob,gender,preference)
    
        response = requests.get(f'https://upscapi.pythonanywhere.com/play?exam={exam}&gender={gender}&pref={preference}&dob={input_dob}')
        response1= response.json()
        response2= dict(response1)
        response2=list(response2.values())[0]
        return render_template('index.html',results=response2)


if __name__=="__main__":
    app.run(port=8080)
