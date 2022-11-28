from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String
class Person(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    birth = Column(Integer, nullable=False)
    def __repr__(self):
        return self.full_name
