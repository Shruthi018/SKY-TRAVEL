from flask import Flask, render_template, request,redirect,url_for,session
app = Flask(__name__)

import secrets
secret_key = secrets.token_hex(16)
print("Secret Key:", secret_key)
app.secret_key = secret_key

@app.route('/')
def index():   
    return render_template('bus.html')

@app.route('/bus', methods=['GET', 'POST'])
def bus():
    if request.method == 'POST':
        session['mode'] = 'bus'
        session['from'] = request.form['from']
        session['to'] = request.form['to']
        session['date'] = request.form['date']
        session['traveller'] = request.form['traveller']
        session['time'] = request.form['time']
        session['seat'] = request.form['seat']
        return redirect(url_for('detail'))
    return render_template('bus.html')

@app.route('/train', methods=['GET', 'POST'])
def train():
    if request.method == 'POST':
        session['mode'] = 'train'
        session['from'] = request.form['from']
        session['to'] = request.form['to']
        session['date'] = request.form['date']
        session['traveller'] = request.form['traveller']
        session['time'] = request.form['time']
        session['seat'] = request.form['seat']
        return redirect(url_for('detail'))
    return render_template('train.html')

@app.route('/plane', methods=['GET', 'POST'])
def plane():
    if request.method == 'POST':
        session['mode'] = 'plane'
        session['from'] = request.form['from']
        session['to'] = request.form['to']
        session['date'] = request.form['date']
        session['traveller'] = request.form['traveller']
        session['time'] = request.form['time']
        session['seat'] = request.form['seat']
        return redirect(url_for('detail'))
    return render_template('plane.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            session['logged_in'] = True
            return redirect(url_for('detail'))
        else:
            return render_template('login.html', error="Invalid username or password.")
    return render_template('login.html')

# Detail route with authentication
@app.route('/detail', methods=['GET', 'POST'])
def detail():
    if 'logged_in' in session and session['logged_in']:
        if request.method == 'POST':
            session['name'] = request.form['name']
            session['gen'] = request.form['gen']
            return redirect(url_for('ticket'))
        return render_template('details.html')
    else:
        return redirect(url_for('login'))
    
@app.route('/ticket')
def ticket():
    booking_data = {key: session[key] for key in session if key != 'name' and key != 'gen'}
    details_data = {'name': session.get('name'), 'gen': session.get('gen')}
    return render_template('ticket.html', booking_data=booking_data, details_data=details_data)

if __name__ == "__main__":
    app.run(debug=True)

