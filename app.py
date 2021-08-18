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
        # category= str(request.form['category'])
        gender= str(request.form['gender'])
        preference= str(request.form['preference'])

        #ONLY FOR NATIONAL DEFENCE ACADEMY

        if exam=="National Defence Academy" and gender=="Male":
            import db_conn
            conn = sqlite3.connect('dates.db', check_same_thread=False)
            results_nda_list= db_conn.c.execute(f"""SELECT course from nda WHERE starting_date <= '{input_dob}'
                                        and ending_date >= '{input_dob}'
                                    """)
            results_nda_list= list(db_conn.c.fetchall())
            if len(results_nda_list):
                results_nda = ' '.join(str(v) for v in results_nda_list)
                # results_nda0= results_nda_list[0:2]
                return render_template("index.html", results_nda=results_nda)
            else:
                ageover_error='Your entered age is out of attempts.'
                return render_template("index.html",ageover_error=ageover_error)


            
        elif exam=="National Defence Academy" and (gender=="Female" or gender=="Others"):
            nda_error='Women and ternanry genders are presently not accepted in the National Defence Academy'
            return render_template("index.html", nda_error=nda_error)


            #FOR CDS IMA AND INA


        elif exam=="Combined Defence Services Examination" and gender=="Male" and (preference=="IMA" or preference=="INA"):
            import db_conn
            conn = sqlite3.connect('dates.db', check_same_thread=False)
            results_cds_list=db_conn.c.execute(f"""SELECT course from cds_ima_ina WHERE starting_date <= '{input_dob}'
                                        and ending_date >= '{input_dob}'
                                    """)
            results_cds_list= list(db_conn.c.fetchall())
            if len(results_cds_list):
                results_cds_ima= ' '.join(str(v) for v in results_cds_list)
                # results_cds_ima04= results_cds_list[0:5]
                # results_cds_ima04= ' '.join(str(v) for v in results_cds_ima04)
                return render_template("index.html", results_cds_ima=results_cds_ima)
            else:
                ageover_error='Your entered age is out of attempts.'
                return render_template("index.html",ageover_error=ageover_error)
        
        elif exam=="Combined Defence Services Examination" and (gender=="Female" or gender=="Others") and (preference=="IMA" or preference=="INA" or preference=="AFA"):
            cds_women_error="Women are only eligible to apply for OTA through CDS entry."
            return render_template("index.html", cds_women_error=cds_women_error)


            #for cds and afa

        elif exam=="Combined Defence Services Examination" and gender=="Male" and preference=="AFA":
            import db_conn
            conn = sqlite3.connect('dates.db', check_same_thread=False)
            results_cds_afa_list=db_conn.c.execute(f"""SELECT course from cds_afa WHERE starting_date <= '{input_dob}'
                                        and ending_date >= '{input_dob}'
                                    """)
            results_cds_afa_list= list(db_conn.c.fetchall())
            if len(results_cds_afa_list):
                results_cds_afa= ' '.join(str(v) for v in results_cds_afa_list)
                # results_cds_afa04= results_cds_afa_list[0:5]
                # results_cds_afa04= ' '.join(str(v) for v in results_cds_afa04)
                return render_template("index.html", results_cds_afa=results_cds_afa)
            
            else:
                ageover_error='Your entered age is out of attempts.'
                return render_template("index.html",ageover_error=ageover_error)


            #for cds and ota (ssc)

        elif exam=="Combined Defence Services Examination" and preference=="OTA":
            import db_conn
            conn = sqlite3.connect('dates.db', check_same_thread=False)
            results_cds_ota_list=db_conn.c.execute(f"""SELECT course from cds_ota_men_women WHERE starting_date <= '{input_dob}'
                                        and ending_date >= '{input_dob}'
                                    """)
            results_cds_ota_list= list(db_conn.c.fetchall())
            if len(results_cds_ota_list):
                results_cds_ota= ' '.join(str(v) for v in results_cds_ota_list)
                # results_cds_ota04= results_cds_ota_list[0:5]
                # results_cds_ota04= ' '.join(str(v) for v in results_cds_ota04)
                return render_template("index.html", results_cds_ota=results_cds_ota)
            
            else:
                ageover_error='Your entered age is out of attempts.'
                return render_template("index.html",ageover_error=ageover_error)
        
        elif exam=="Combined Defence Services Examination" and gender=="Others" and preference=="OTA":
            cds_others_error="Ternanry genders are not eligible to apply for OTA through CDS entry."
            return render_template("index.html", cds_others_error=cds_others_error)
        
          #for afcat fb
        
        elif exam=="AFCAT" and preference=="AFA_flying":
            import db_conn
            conn = sqlite3.connect('dates.db', check_same_thread=False)
            results_afcat_fb_list=db_conn.c.execute(f"""SELECT course from afcat_fb WHERE starting_date <= '{input_dob}'
                                        and ending_date >= '{input_dob}'
                                    """)
            results_afcat_fb_list= list(db_conn.c.fetchall())
            if len(results_afcat_fb_list):
                results_afcat_fb= ' '.join(str(v) for v in results_afcat_fb_list)
                # results_afcat_fb04= results_afcat_fb_list[0:5]
                # results_afcat_fb04= ' '.join(str(v) for v in results_afcat_fb04)
                return render_template("index.html", results_afcat_fb=results_afcat_fb)
            
            else:
                ageover_error='Your entered age is out of attempts.'
                return render_template("index.html",ageover_error=ageover_error)

            #for afcat gd
        
        elif exam=="AFCAT" and preference=="AFA_gd":
            import db_conn
            conn = sqlite3.connect('dates.db', check_same_thread=False)
            results_afcat_fb_list=db_conn.c.execute(f"""SELECT course from afcat_gd WHERE starting_date <= '{input_dob}'
                                        and ending_date >= '{input_dob}'
                                    """)
            results_afcat_gd_list= list(db_conn.c.fetchall())
            if len(results_afcat_gd_list):
                results_afcat_gd= ' '.join(str(v) for v in results_afcat_gd_list)
                # results_afcat_gd04= results_afcat_gd_list[0:5]
                # results_afcat_gd04= ' '.join(str(v) for v in results_afcat_gd04)
                return render_template("index.html", results_afcat_gd=results_afcat_gd)
            
            else:
                ageover_error='Your entered age is out of attempts.'
                return render_template("index.html",ageover_error=ageover_error)


           # for CSE 
        
        elif exam=="Civil Services Examination":
            import db_conn
            conn = sqlite3.connect('dates.db', check_same_thread=False)
            results_afcat_fb_list=db_conn.c.execute(f"""SELECT course from cse WHERE starting_date <= '{input_dob}'
                                        and ending_date >= '{input_dob}'
                                    """)
            results_cse_list= list(db_conn.c.fetchall())
            if len(results_cse_list):
                results_cse= ' '.join(str(v) for v in results_cse_list)
                # results_afcat_gd04= results_afcat_gd_list[0:5]
                # results_afcat_gd04= ' '.join(str(v) for v in results_afcat_gd04)
                return render_template("index.html", results_cse=results_cse)        

            else:
                ageover_error='Your entered age is out of attempts.'
                return render_template("index.html",ageover_error=ageover_error)

        else:
            return render_template("index.html")


@app.route("/sendmail2442")
def website_sendmail():
    return render_template('sendmail.html')


@app.route("/sendmailadded", methods=['POST','GET'])
def getmail():

    if request.method =='POST':
        exam= str(request.form['exam2442'])
        input_mail= str(request.form['email2442'])
        if exam=="National Defence Academy":
            import emaildb
            sqlite3.connect('emails.db', check_same_thread=False)
            ess=emaildb.c.execute(f"INSERT INTO email_list VALUES ('NDA', '{input_mail}')")
            emaildb.conn.commit()
            return render_template("sendmail.html")
        if exam=="Combined Defence Services Examination":
            import emaildb
            sqlite3.connect('emails.db', check_same_thread=False)
            ess=emaildb.c.execute(f"INSERT INTO email_list VALUES ('CDS', '{input_mail}')")
            emaildb.conn.commit()
            return render_template("sendmail.html")
        if exam=="AFCAT":
            import emaildb
            sqlite3.connect('emails.db', check_same_thread=False)
            ess=emaildb.c.execute(f"INSERT INTO email_list VALUES ('AFCAT', '{input_mail}')")
            emaildb.conn.commit()
            return render_template("sendmail.html")
        else:
            return render_template("sendmail.html")            

if __name__=="__main__":
    app.run(debug=True)
