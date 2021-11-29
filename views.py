from app import app
from repository import ContactRepository, ContactGroupRepository
from models import session
from models.contact import Contact
from flask import request, redirect, render_template, url_for, flash
import json

contact_repo = ContactRepository(session=session)
contact_group_repo = ContactGroupRepository(session=session)


@app.route('/', methods=['GET'])
def index():
    contacts = contact_repo.list()
    contact_groups = contact_group_repo.list()
    return render_template('home.html', contacts=contacts, contact_groups=contact_groups, contacts_dump=json.dumps([contact.serialize for contact in contacts]))


@app.route('/add', methods=['GET'])
def add():
    contact_groups = contact_group_repo.list()
    return render_template('add-contact.html', contact_groups=contact_groups)


@app.route('/add', methods=['POST'])
def handle_add():
    contact_repo.add_contact(Contact(name=request.form["name"], surname=request.form["surname"],
                                     mail=request.form["email"], phone_number=request.form["phone_number"],
                                     address=request.form["address"], group_id=request.form["group_id"],
                                     priority=0.05))
    return redirect('/')


@app.route('/contact/<contact_id>', methods=['GET'])
def contact(contact_id):
    # Increase priority
    contact_repo.increase_priority(contact_id)
    contact_info = contact_repo.get_contact(contact_id)
    contact_group = contact_group_repo.get_contact_group(contact_info.group_id)
    return render_template('contact.html', contact_group=contact_group, contact_info=contact_info)


@app.route('/update/<contact_id>', methods=['GET'])
def update(contact_id):
    contact_groups = contact_group_repo.list()
    contact_info = contact_repo.get_contact(contact_id)
    return render_template('update-contact.html', contact_groups=contact_groups, contact_info=contact_info)


@app.route('/update/<contact_id>', methods=['POST'])
def handle_update(contact_id):
    contact_repo.update_contact(contact_id, Contact(name=request.form["name"], surname=request.form["name"],
                                                    mail=request.form["email"], phone_number=request.form["phone_number"],
                                                    address=request.form["address"], group_id=request.form["group_id"]))
    return redirect('/')


@app.route('/delete/<contact_id>', methods=['GET'])
def delete(contact_id):
    contact_repo.delete_contact(contact_id)
    return redirect('/')
