from typing import List

from sqlalchemy import desc

from models.material import Material


class MaterialRepository:
    def __init__(self, session):
        self.session = session

    def add_material(self, material: Material) -> Material:
        self.session.add(material)
        self.session.commit()
        return material

    def get_material(self, material_id) -> Material:
        return self.session.query(Material).get(material_id)

    def update_material(self, contact_id, material: Material):
        current_material = self.session.query(Material).get(contact_id)
        current_material.name = material.name
        current_material.description = material.description
        current_material.quantity = material.quantity
        current_material.priority = material.priority
        self.session.commit()
        return current_material

    def delete_material(self, material_id):
        current_material = self.get_material(material_id)
        self.session.delete(current_material)
        self.session.commit()

    def list(self) -> List[Material]:
        return self.session.query(Material).order_by(desc(Material.priority)).all()
