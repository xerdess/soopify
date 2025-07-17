from flask import Flask,redirect,render_template,request

app= Flask(__name__)

@app.route('/', methods=['GET','POST'])
def fun():
    if request.method == 'POST':
        link = request.form.get('link')
        return redirect(link)
    return render_template('fun.html')

if __name__=='__main__':
    app.run(debug=True)