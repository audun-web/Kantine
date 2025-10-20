from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Organiserer menydata som en dictionary for enklere oppslag
menu_data = {
    "mandag": {
        "day": "Mandag",
        "image": "img/kremet-pasta.webp",
        "alt_text": "Kremet pasta med kylling",
        "description": "Kremet pasta med kylling og soltørkede tomater.",
        "price": "45,-",
        "allergens": "Inneholder: Pasta, Protein"
    },
    "tirsdag": {
        "day": "Tirsdag",
        "image": "img/pannestekt-laks.webp",
        "alt_text": "Pannestekt laks",
        "description": "Pannestekt laks servert med ovnsbakte rotgrønnsaker.",
        "price": "50,-",
        "allergens": "Inneholder: Fisk."
    },
    "onsdag": {
        "day": "Onsdag",
        "image": "img/lasagne.jpg",
        "alt_text": "Hjemmelaget lasagne",
        "description": "Hjemmelaget lasagne med frisk salat og hvitløksbrød.",
        "price": "45,-",
        "allergens": "Inneholder: Gluten, melk."
    },
    "torsdag": {
        "day": "Torsdag",
        "image": "img/burger.jpeg",
        "alt_text": "Saftig burger",
        "description": "Burger-torsdag! Saftig burger med cheddar og bacon.",
        "price": "48,-",
        "allergens": "Inneholder: Gluten, melk, sesamfrø."
    },
    "fredag": {
        "day": "Fredag",
        "image": "img/taco.webp",
        "alt_text": "Taco-buffet",
        "description": "Taco-fredag! Buffet med alt du kan ønske deg av tilbehør.",
        "price": "49,-",
        "allergens": "Inneholder: Melk. Glutenfrie lefser tilgjengelig."
    }
}

@app.route('/meny')
def meny():
    # Sender alle verdiene fra dictionaryen til malen
    return render_template('meny.html', menu_items=menu_data.values())

@app.route('/varer')
def varer():
    return render_template('varer.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

@app.route('/meny/<string:day>')
def menu_day_detail(day):
    # Finner den spesifikke retten basert på dagen i URL-en
    item = menu_data.get(day.lower())
    if not item:
        abort(404) # Viser en "Not Found"-side hvis dagen ikke finnes
    return render_template('day_detail.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)