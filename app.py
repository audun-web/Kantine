from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/meny')
def meny():
    menu_data = [
        {
            "day": "Mandag",
            "image": "img/kremet-pasta.webp",
            "alt_text": "Kremet pasta med kylling",
            "description": "Kremet pasta med kylling og soltørkede tomater.",
            "price": "45,-"
        },
        {
            "day": "Tirsdag",
            "image": "img/pannestekt-laks.webp",
            "alt_text": "Pannestekt laks",
            "description": "Pannestekt laks servert med ovnsbakte rotgrønnsaker.",
            "price": "50,-"
        },
        {
            "day": "Onsdag",
            "image": "img/lasagne.jpg",
            "alt_text": "Hjemmelaget lasagne",
            "description": "Hjemmelaget lasagne med frisk salat og hvitløksbrød.",
            "price": "45,-"
        },
        {
            "day": "Torsdag",
            "image": "img/burger.jpeg",
            "alt_text": "Saftig burger",
            "description": "Burger-torsdag! Saftig burger med cheddar og bacon.",
            "price": "48,-"
        },
        {
            "day": "Fredag",
            "image": "img/taco.webp",
            "alt_text": "Taco-buffet",
            "description": "Taco-fredag! Buffet med alt du kan ønske deg av tilbehør.",
            "price": "49,-"
        }
    ]
    return render_template('meny.html', menu_items=menu_data)

@app.route('/varer')
def varer():
    return render_template('varer.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

if __name__ == '__main__':
    app.run(debug=True)