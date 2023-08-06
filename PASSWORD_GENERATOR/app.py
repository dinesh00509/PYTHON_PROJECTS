from flask import Flask, render_template,request
import random
import string


app = Flask(__name__,template_folder='templates')


def generate_password(length=10,uppercase=True, lowercase=True, digits=True, special_char=True):
    characters =''
    if uppercase:
        characters =characters+string.ascii_uppercase
    if lowercase:
        characters=characters+string.ascii_lowercase
    if digits:
        characters = characters+string.digits
    if special_char :
        characters = characters +string.punctuation
    if not characters :
        return "please select atleast single character to generate the password"
    
    
   
    password = ''.join(random.choice(characters) for i in range(length))
    return password




@app.route('/')
def index():
    return render_template('index.html')




    
@app.route('/generate', methods=['POST'])
def generate():
    if request.method =='POST':
    
        length = int(request.form.get('length', 10))
        uppercase = request.form.get(('uppercase')) == 'on'
        lowercase = request.form.get(('lowercase')) == 'on'
        digits= request.form.get(('digits')) == 'on'
        special_char = request.form.get(('special_char')) == 'on'
        password = generate_password(length,uppercase,lowercase,digits,special_char)
        return render_template('pass.html', password=password)
    else :
        return render_template('index.html')
    





    
    

if __name__ == "__main__":
    
    app.run(debug=True)
    
   
       
    
    

        
    
    

    