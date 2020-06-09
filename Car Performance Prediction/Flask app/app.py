from flask import Flask,render_template,request,url_for
app=Flask(__name__)
import pickle
model=pickle.load(open("mileage.pkl","rb"))
@app.route('/')
def helloworld():
    return render_template("index.html")

@app.route('/login',methods=["POST","GET"])
def admin():
    if request.method=="POST":
        if(request.form == None):
            return render_template('form.html')
        p=request.form["cylinders"]
        q=request.form["displacement"]
        r=request.form["horsepower"]
        s=request.form["weight"]
        t=request.form["acceleration"]
        u=request.form["modelyear"]
        v=request.form["origin"]
        try:
            w=[[int(p),int(q),int(r),int(s),float(t),int(u),int(v)]]
    
            y=model.predict((w))
            return render_template("form.html",y="The predicted mileage would be:" +str(y[0][0]))
        except:
            return render_template("form.html",error="Please enter numeric value")
    else:
        return render_template('form.html')
@app.route('/user')
def user():
    return "hi user"
if __name__=='__main__':
    app.run(debug=True)
    


