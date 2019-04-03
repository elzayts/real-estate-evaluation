from flask import Flask, render_template, request, redirect, url_for
app=Flask(__name__)

filt = {}

@app.route("/main", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        filt['street'] = request.form['street']
        filt['room'] = request.form['rooms']
        # filt[distr]=request.form['district']
        # filt[t_area] = request.form['total_area']
        # filt[l_area] = request.form['living_area']
        # filt[residence]= request.form['residence_type']
        return redirect(url_for('show'))
    else:
      return render_template("index1.html")


@app.route("/info", methods=['GET'])
def show():
    return render_template("info.html")



