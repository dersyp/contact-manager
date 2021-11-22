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
