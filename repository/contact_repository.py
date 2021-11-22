from typing import List
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

    def update_contact(self, contact: Contact):
        current_contact = self.session.query(Contact).get(contact.contact_id)
        current_contact.name = current_contact.name
        current_contact.surname = current_contact.surname
        self.session.commit()
        return contact

    def delete_contact(self, contact_id):
        current_contact = self.get_contact(contact_id)
        self.session.delete(current_contact)
        self.session.commit()

    def list(self) -> List[Contact]:
        return self.session.query(Contact).all()
