from flask import Flask, url_for, render_template, request, session, redirect

SECRET_KEY = '5d8d4c03-ce93-43bc-8a0c-cf23ff4f5593'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return 'About'

@app.route('/users/<username>')
def welcome_user(username):
    return 'Welcome {}'.format(username)

@app.route('/with_int/<int:number>')
def show_number(number):
    return 'We\'re counting from number {}'.format(number)

@app.route('/build_url_sample')
def build_url_sample():
    return url_for('about')

@app.route('/get_http_method_sample', methods=['GET'])
def get_http_method_sample():
    return 'GET'

@app.route('/post_http_method_sample', methods=['POST'])
def post_http_method_sample():
    return 'POST'

@app.route('/view_product', methods=['GET'])
def view_product():
    return render_template('products/view_products.html', product_name='Glossy lipstick', brand='Color pop')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        if 'username' in session:
            return redirect(url_for('home'))

        return render_template('login/login.html')

    username = request.form['username']
    password = request.form['password']

    # Login code here..
    login_successful = True
    if login_successful:
        session['username'] = username
        return redirect(url_for('home'))

    return redirect(url_for('forbidden'))

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/trigger_error_401/')
def trigger_error_401():
    abort(401)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error/404.html'), 404

if __name__ == '__main__':
    app.secret_key = SECRET_KEY
    app.run(debug=True)
