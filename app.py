from flask import Flask,render_template,request
app = Flask(__name__)
import sqlite3


@app.route("/")
def website_eligibility():
    return render_template('index.html')

    
#form submission route
@app.route("/w4", methods=['POST','GET'])
def send():

    if request.method =='POST':
        exam= str(request.form['exam'])
        input_dob= str(request.form['input_dob'])
        category= str(request.form['category'])
        gender= str(request.form['gender'])
        preference= str(request.form['preference'])

        #ONLY FOR NATIONAL DEFENCE ACADEMY

        if exam=="National Defence Academy" and gender=="Male":
            import db_conn
            conn = sqlite3.connect('your.db', check_same_thread=False)
            results_nda_list= db_conn.c.execute(f"""SELECT course from nda WHERE starting_date <= '{input_dob}'
                                        and ending_date >= '{input_dob}'
                                    """)
            results_nda_list= list(db_conn.c.fetchall())
            results_nda = ' '.join(str(v) for v in results_nda_list)
            results_nda0= results_nda_list[0]
            results_nda1= results_nda_list[1]
            return render_template("index.html", results_nda=results_nda, results_nda0=results_nda0, results_nda1=results_nda1)

            
        elif exam=="National Defence Academy" and (gender=="Female" or gender=="Others"):
            nda_error='Women and ternanry genders are presently not accepted in the National Defence Academy'
            return render_template("index.html", nda_error=nda_error)


            #FOR CDS IMA AND INA


        elif exam=="Combined Defence Services Examination" and gender=="Male" and (preference=="IMA" or preference=="INA"):
            import db_conn
            conn = sqlite3.connect('your.db', check_same_thread=False)
            results_cds_list=db_conn.c.execute(f"""SELECT course from cds_ima_ina WHERE starting_date <= '{input_dob}'
                                        and ending_date >= '{input_dob}'
                                    """)
            results_cds_list= list(db_conn.c.fetchall())
            results_cds_ima= ' '.join(str(v) for v in results_cds_list)
            results_cds_ima04= results_cds_list[0]
            results_cds_ima04= ' '.join(str(v) for v in results_cds_ima04)
            
            return render_template("index.html", results_cds_ima=results_cds_ima, results_cds_ima04=results_cds_ima04)

            #for cds and afa

        elif exam=="Combined Defence Services Examination" and gender=="Male" and preference=="AFA":
            import db_conn
            conn = sqlite3.connect('your.db', check_same_thread=False)
            results_cds_afa_list=db_conn.c.execute(f"""SELECT course from cds_afa WHERE starting_date <= '{input_dob}'
                                        and ending_date >= '{input_dob}'
                                    """)
            results_cds_afa_list= list(db_conn.c.fetchall())
            results_cds_afa= ' '.join(str(v) for v in results_cds_afa_list)
            results_cds_afa04= results_cds_afa_list[0:5]
            results_cds_afa04= ' '.join(str(v) for v in results_cds_afa04)
            return render_template("index.html", results_cds_afa=results_cds_afa, results_cds_afa04=results_cds_afa04)
        
            #for cds and ota (ssc)

        elif exam=="Combined Defence Services Examination" and preference=="OTA":
            import db_conn
            conn = sqlite3.connect('your.db', check_same_thread=False)
            results_cds_ota_list=db_conn.c.execute(f"""SELECT course from cds_ota_men_women WHERE starting_date <= '{input_dob}'
                                        and ending_date >= '{input_dob}'
                                    """)
            results_cds_ota_list= list(db_conn.c.fetchall())
            results_cds_ota= ' '.join(str(v) for v in results_cds_ota_list)
            results_cds_ota04= results_cds_ota_list[0:5]
            results_cds_ota04= ' '.join(str(v) for v in results_cds_ota04)
            return render_template("index.html", results_cds_ota=results_cds_ota, results_cds_ota04=results_cds_ota04)
                          

if __name__=="__main__":
    app.run(debug=True)






 