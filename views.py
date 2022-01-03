from app import app
from repository import ContactRepository, ContactGroupRepository, MaterialRepository
from models import session
from models.contact import Contact
from models.material import Material
from flask import request, redirect, render_template
import json

contact_repo = ContactRepository(session=session)
contact_group_repo = ContactGroupRepository(session=session)
material_repository = MaterialRepository(session=session)


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/home-employee', methods=['GET'])
def home_employee():
    contacts = contact_repo.list()
    contact_groups = contact_group_repo.list()
    return render_template('home-employee.html', contacts=contacts, contact_groups=contact_groups,
                           contacts_dump=json.dumps([contact.serialize for contact in contacts]))


@app.route('/home-material', methods=['GET'])
def home_material():
    materials = material_repository.list()
    return render_template('home-material.html', materials=materials,
                           materials_dump=json.dumps([material.serialize for material in materials]))


@app.route('/add', methods=['GET'])
def add():
    contact_groups = contact_group_repo.list()
    return render_template('add-employee.html', contact_groups=contact_groups)


@app.route('/add_material', methods=['GET'])
def add_material():
    return render_template('add-material.html')


@app.route('/add_material', methods=['POST'])
def handle_add_material():
    material_repository.add_material(Material(name=request.form["name"], description=request.form["description"],
                                              quantity=request.form["quantity"], priority=0.05))
    return redirect('/home-material')


@app.route('/add', methods=['POST'])
def handle_add():
    contact_repo.add_contact(Contact(name=request.form["name"], surname=request.form["surname"],
                                     mail=request.form["email"], phone_number=request.form["phone_number"],
                                     address=request.form["address"], group_id=request.form["group_id"],
                                     priority=0.05))
    return redirect('/home-employee')


@app.route('/employee/<contact_id>', methods=['GET'])
def employee(contact_id):
    # Increase priority
    contact_repo.increase_priority(contact_id)
    contact_info = contact_repo.get_contact(contact_id)
    contact_group = contact_group_repo.get_contact_group(contact_info.group_id)
    return render_template('employee.html', contact_group=contact_group, contact_info=contact_info)


@app.route('/material/<material_id>', methods=['GET'])
def material(material_id):
    # Increase priority
    # material_repository.increase_priority(material_id)
    material_info = contact_repo.get_contact(material_id)
    return render_template('material.html', material_info=material_info)


@app.route('/update_material/<material_id>', methods=['GET'])
def update_material(material_id):
    material_info = material_repository.get_material(material_id)
    return render_template('update-material.html', material_info=material_info)


@app.route('/update_material/<material_id>', methods=['POST'])
def handle_update_material(material_id):
    material_repository.update_material(material_id,
                                        Material(name=request.form["name"], description=request.form["description"],
                                                 quantity=request.form["quantity"], priority=request.form["priority"]))
    return redirect('/home-material')


@app.route('/delete_material/<material_id>', methods=['GET'])
def delete_material(material_id):
    material_repository.delete_material(material_id)
    return redirect('/home-material')


@app.route('/update/<contact_id>', methods=['GET'])
def update(contact_id):
    contact_groups = contact_group_repo.list()
    contact_info = contact_repo.get_contact(contact_id)
    return render_template('update-employee.html', contact_groups=contact_groups, contact_info=contact_info)


@app.route('/update/<contact_id>', methods=['POST'])
def handle_update(contact_id):
    contact_repo.update_contact(contact_id, Contact(name=request.form["name"], surname=request.form["surname"],
                                                    mail=request.form["email"],
                                                    phone_number=request.form["phone_number"],
                                                    address=request.form["address"], group_id=request.form["group_id"],
                                                    priority=request.form["priority"]))
    return redirect('/home-employee')


@app.route('/delete/<contact_id>', methods=['GET'])
def delete(contact_id):
    contact_repo.delete_contact(contact_id)
    return redirect('/home-employee')
