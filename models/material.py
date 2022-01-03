from sqlalchemy import Column, Integer, String, Float, ForeignKey
from models import Base


class Material(Base):
    __tablename__ = "material"
    material_id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    description = Column(String)
    priority = Column(Float)

    def __init__(self, name, quantity, priority, description):
        self.name = name
        self.quantity = quantity
        self.description = description
        self.priority = priority

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'material_id': self.material_id,
            'name': self.name,
            'quantity': self.quantity,
            'description': self.description,
            'priority': self.priority
        }
