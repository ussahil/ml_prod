"""
This module defines the database models using SQLAlchemy

It includes model classes for different types of real estate spcefically rental apartments. This module uses SQLAlchemy ORM capabilities to map Python classes to Databases tables
"""

# we need to define the table schema as sql alchemy requires it (check this)

from sqlalchemy import REAL,INTEGER,VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped , mapped_column

from config.config import settings

class Base(DeclarativeBase):
  """ Base class for Alchemy model"""
  pass

class RentApartments(Base):
  """
  SQLAlchemy model class for rental apartments
  """
  
  __tablename__ =settings.rent_apart_table_name
  
  address:Mapped[str] = mapped_column(VARCHAR(),primary_key=True)
  # Primary key is done as SQLLite requires 1 primary at least
  area:Mapped[float] = mapped_column(REAL())
  constraction_year:Mapped[int] = mapped_column(INTEGER())
  rooms:Mapped[int] = mapped_column(INTEGER())
  bedrooms:Mapped[int] = mapped_column(INTEGER())
  bathrooms:Mapped[int] = mapped_column(INTEGER())
  balcony:Mapped[str]=mapped_column(VARCHAR())
  storage:Mapped[str]=mapped_column(VARCHAR())
  parking:Mapped[str]=mapped_column(VARCHAR())
  furnished:Mapped[str]=mapped_column(VARCHAR())
  garage:Mapped[str]=mapped_column(VARCHAR())
  garden:Mapped[str]=mapped_column(VARCHAR())
  energy:Mapped[str]=mapped_column(VARCHAR())
  facilities:Mapped[str]=mapped_column(VARCHAR())
  zip:Mapped[str]=mapped_column(VARCHAR())
  neighborhood:Mapped[str]=mapped_column(VARCHAR())
  rent:Mapped[int] = mapped_column(INTEGER())
  