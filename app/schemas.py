from pydantic import BaseModel, EmailStr
from typing import Optional


class ReservationBase(BaseModel):
    number_of_people: int
    full_name: str
    email: EmailStr
    phone_number: str
    address: str
    payment_card_info: str
    stay_duration: int
    room_type: str
    paypal_email: Optional[EmailStr] = None
    paypal_password: Optional[str] = None  # Caution: Storing passwords in plain text is not secure


class ReservationCreate(ReservationBase):
    pass


class ReservationUpdate(ReservationBase):
    pass


class Reservation(ReservationBase):
    id: int

    class Config:
        from_attributes = True
