from flask import render_template, Blueprint, request, flash
import random

views = Blueprint('views', __name__)

def password_generator(nr_letters, nr_symbols, nr_numbers):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []
    for letter in range(0,nr_letters):
        password.append(random.choice(letters))
    for symbol in range(0,nr_symbols):
        password.append(random.choice(symbols))
    for number in range(0,nr_numbers):
        password.append(random.choice(numbers))
    # print(password)
    random.shuffle(password)
    shuffled_password = ""
    for x in password:
        shuffled_password += x
    # print(shuffled_password)
    return shuffled_password


@views.route('/')
def index():
    return render_template('index.html')

@views.route('/process', methods=['POST'])
def process():
    letters = request.form.get('nr_letters')
    numbers = request.form.get('nr_numbers')
    symbols = request.form.get('nr_symbols')
    # print(letters, numbers, symbols)

    if letters:
        letters = int(letters)
    if numbers:
        numbers = int(numbers)
    if symbols:
        symbols = int(symbols)

    if letters or numbers or symbols:
        generated_password = password_generator(letters or 0, numbers or 0, symbols or 0)
        return render_template('result.html', password = generated_password)
    else:
        flash("You didn't input anything")
        return render_template('index.html')

    

    
