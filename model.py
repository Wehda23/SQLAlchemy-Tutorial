from typing import Optional, List
from sqlalchemy import ForeignKey, String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import uuid



# First step is to set up the database
Base = declarative_base()


class User(Base):
    
    # Name of the table
    __tablename__ = "user"

    # Unique Id for each user
    user_id : Column = Column(String, primary_key=True, default=str(uuid.uuid4()))

    # Name of the person giving it a limit of 30 characters
    name : Column  = Column(String(30))

    # Full name of the person
    fullname : Column[Optional[str]] = Column(String)

    # Address of the user


    # Here we can access the address of the user.
    address : List["Address"] = relationship( "Address" ,back_populates= 'user', cascade='all, delete-orphan')

    def __repr__(self):

        return f"{__class__.__name__}(id ={self.id!r}, name={self.name!r}, fullname = {self.fullname!r})"
    

class Address(Base):
    __tablename__  = "address"


    #  Id for each address.
    address_id : Column  = Column(Integer, primary_key = True, autoincrement = True)

    # Email address field as string.
    email_address : Column[str] = Column(String)

    # Create the column where as we store the primary key of user as foreign key in this table to establish connection One to Many between user and his addresses
    user_id : Column = Column(Integer, ForeignKey("user"))


    # Creating an attribute to call user for example address.user here we can access the user's attributes such as address.user.name..
    user : 'User' = relationship('User' ,back_populates = 'address')

    def __repr__(self):

        return f"{__class__.__name__}(id ={self.address_id!r}, email_address = {self.email_address!r})"
    
class Test(Base):
    __tablename__ = "test"

    test_id : Column  = Column(Integer, primary_key = True, autoincrement = True)



