from flask import  render_template
from pet import app
from lib.models import Pet, Owner

@app.route('/')
def index():
    pets = Pet.query.all()
    owners = Owner.query.all()

    return render_template('index.html', pets=pets, owners=owners)