from sqlalchemy import Column, Integer, String, Float, ForeignKey
from models import Base


class GroupPriority(Base):
    __tablename__ = "contact_group"
    group_id = Column(Integer, primary_key=True)
    group_name = Column(String)
    group_priority = Column(Float)

    def __init__(self, group_name, group_priority):
        self.group_priority = group_priority
        self.group_name = group_name
