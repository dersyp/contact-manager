from typing import List

from sqlalchemy import desc

from models.contact import Contact


class ContactRepository:
    def __init__(self, session):
        self.session = session

    def add_contact(self, contact: Contact) -> Contact:
        self.session.add(contact)
        self.session.commit()
        return contact

    def get_contact(self, contact_id) -> Contact:
        return self.session.query(Contact).get(contact_id)

    def update_contact(self, contact_id, contact: Contact):
        current_contact = self.session.query(Contact).get(contact_id)
        current_contact.name = contact.name
        current_contact.surname = contact.surname
        current_contact.phone_number = contact.phone_number
        current_contact.mail = contact.mail
        current_contact.group_id = contact.group_id
        current_contact.address = contact.address
        current_contact.priority = contact.priority
        self.session.commit()
        return current_contact

    def increase_priority(self, contact_id):
        current_contact = self.session.query(Contact).get(contact_id)
        new_priority = current_contact.priority + (1 - current_contact.priority) * 0.05
        current_contact.priority = new_priority
        self.session.commit()
        return current_contact

    def delete_contact(self, contact_id):
        current_contact = self.get_contact(contact_id)
        self.session.delete(current_contact)
        self.session.commit()

    def list(self) -> List[Contact]:
        return self.session.query(Contact).order_by(desc(Contact.priority)).all()
