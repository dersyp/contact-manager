from sqlalchemy import Column, Integer, String, Float, ForeignKey
from models import Base


class Contact(Base):
    __tablename__ = "contact"
    contact_id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    mail = Column(String)
    phone_number = Column(String)
    group_id = Column(Integer, ForeignKey("contact_group.group_id"))
    address = Column(String)
    priority = Column(Float)

    def __init__(self, name, surname, mail, phone_number, group_id, address, priority):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.phone_number = phone_number
        self.group_id = group_id
        self.address = address
        self.priority = priority

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'contact_id': self.contact_id,
            'name': self.name,
            'surname': self.surname,
            'mail': self.mail,
            'phone_number': self.phone_number,
            'group_id': self.group_id,
            'address': self.address,
            'priority': self.priority
        }