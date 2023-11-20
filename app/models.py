from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True, index=True)
    number_of_people = Column(Integer)
    full_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    address = Column(String)
    payment_card_info = Column(String)
    stay_duration = Column(Integer)
    room_type = Column(String)
