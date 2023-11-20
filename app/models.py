from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True, index=True)
    number_of_people = Column(Integer, nullable=True)
    full_name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    address = Column(String, nullable=True)
    payment_card_info = Column(String, nullable=True)
    stay_duration = Column(Integer, nullable=True)
    room_type = Column(String, nullable=True)
    paypal_email = Column(String, nullable=True)
    paypal_password = Column(String, nullable=True)
