from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        
        soma = int(num1) + int(num2)
        
        return render_template('index.html', resultado=soma)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)