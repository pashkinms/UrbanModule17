from app.backend import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__= 'categories'
    __table_args__ = {'extended_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    products = relationship('Product', back_populates='category')

from sqlalchemy.schema import CreateTable
print(CreateTable(Category.__table__))