from typing import List
from models.group_priority import GroupPriority


class ContactGroupRepository:
    def __init__(self, session):
        self.session = session

    def add_contact_group(self, contact_group: GroupPriority) -> GroupPriority:
        existing_contact_group = self.session.query(GroupPriority).filter(GroupPriority.group_name == contact_group.group_name).all()
        if not existing_contact_group:
            self.session.add(contact_group)
            self.session.commit()
        return contact_group

    def get_contact_group(self, group_contact_id) -> GroupPriority:
        return self.session.query(GroupPriority).get(group_contact_id)

    def update_contact_group(self, contact_group: GroupPriority):
        current_contact_group = self.session.query(GroupPriority).get(contact_group.group_id)
        current_contact_group.priority = contact_group.group_priority
        self.session.commit()
        return contact_group

    def delete_contact_group(self, group_contact_id):
        current_contact_group = self.get_contact_group(group_contact_id)
        self.session.delete(current_contact_group)
        self.session.commit()

    def list(self) -> List[GroupPriority]:
        return self.session.query(GroupPriority).all()
