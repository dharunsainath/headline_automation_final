from flask import Flask,render_template,request

import main2

app=Flask(__name__)




@app.route("/")
def index():


    return render_template("index.html")




@app.route("/form" , methods=["POST"])
def form():
    name= request.form.get("enter_name")
    email=request.form.get("email_input")
    a = main2.extract_news()
    main2.email_send(email,a)
    name_form=name
    email_id = email

    return render_template("thanks.html",name=name,email=email)



if __name__=="__main__":
    app.run()
