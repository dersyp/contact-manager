from app import app
from repository import ContactRepository, ContactGroupRepository
from models import session
from models.contact import Contact
from flask import request, redirect, render_template, url_for

contact_repo = ContactRepository(session=session)
contact_group_repo = ContactGroupRepository(session=session)


@app.route('/', methods=['GET'])
def index():
    contacts = contact_repo.list()
    contact_groups = contact_group_repo.list()
    return render_template('home.html', contacts=contacts, contact_groups=contact_groups)


@app.route('/add', methods=['GET'])
def add():
    contact_groups = contact_group_repo.list()
    return render_template('add-contact.html', contact_groups=contact_groups)


@app.route('/add', methods=['POST'])
def addingContact():
    print("POST add")
    print(request.form["name"])
    contact_repo.add_contact(Contact(name=request.form["name"], surname=request.form["name"],
                                     mail=request.form["email"], phone_number=request.form["phone_number"],
                                     address=request.form["address"], group_id=request.form["group_id"],
                                     priority=0.05))
    return redirect('/')


@app.route('/change', methods=['GET'])
def change():
    return 'Change contact'
