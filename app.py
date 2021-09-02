from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template('index.html')

@app.route("/get", methods=['POST','GET'])
def getvalues():

    #importing values
    if request.method =='POST':
        exam= str(request.form['exam'])
        input_dob= str(request.form['input_dob'])
        # category= str(request.form['category'])
        gender= str(request.form['gender'])
        preference= str(request.form['preference'])


        def calc(table,dob):
            import db_conn
            results_list= db_conn.c.execute(f"""SELECT course from {table} WHERE starting_date <= '{dob}'
                                        and ending_date >= '{dob}'
                                    """)
            results_list= list(db_conn.c.fetchall())
            if table=="cse" and len(results_list) :
                results = ' '.join(str(v) for v in results_list)
                return render_template("index.html", results=f"Your available attempts for the exam is/are {results_list}\n\nAge Relaxation on upper age limit for category students and Ex-Servicemen:\n1. OBC= +3 years\n2. SC/ST= +5 years\n3. PWD= +10 years\n4. Ex-Servicemen with 5 years of service= +5 years")

            elif len(results_list):
                results = ' '.join(str(v) for v in results_list)
                return render_template("index.html", results=f"Your available attempts for the exam is/are {results_list}")

            else:
                ageover_error='Your entered age is out of attempts.'
                return render_template("index.html",ageover_error=ageover_error)
            


        if exam=="National Defence Academy" and gender=="Male":
            main_return= calc('nda',input_dob)
            return(main_return)

        elif exam=="Combined Defence Services Examination" and gender=="Male" and (preference=="IMA" or preference=="INA"):
            main_return= calc('cds_ima_ina',input_dob)
            return(main_return)

        elif exam=="Combined Defence Services Examination" and preference=="OTA":
            main_return= calc('cds_ota_men_women',input_dob)
            return(main_return)

        elif exam=="AFCAT" and preference=="AFA_flying":
            main_return= calc('afcat_fb',input_dob)
            return(main_return)

        elif exam=="AFCAT" and preference=="AFA_gd":
            main_return= calc('afcat_gd',input_dob)
            return(main_return)
        
        elif exam=="Combined Defence Services Examination" and gender=="Male" and preference=="AFA":
            main_return= calc('cds_afa',input_dob)
            return(main_return)

        elif exam=="Civil Services Examination":
            main_return= calc('cse',input_dob)
            return ((main_return))

        #ERRORS

        elif exam=="Combined Defence Services Examination" and gender=="Female" and (preference=="IMA" or preference=="INA" or preference=="AFA"):
            hello="Women are only eligibile to apply for OTA through CDS entry"
            return render_template('index.html',ageover_error=hello)

        else:
            hello="An Error has occured, try back again after some time"
            return render_template('index.html',ageover_error=hello)
            


if __name__=="__main__":
    app.run(debug=True)
