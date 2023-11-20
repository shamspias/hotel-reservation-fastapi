from pydantic import BaseModel


class ReservationBase(BaseModel):
    number_of_people: int
    full_name: str
    email: str
    phone_number: str
    address: str
    payment_card_info: str
    stay_duration: int
    room_type: str


class ReservationCreate(ReservationBase):
    pass


class Reservation(ReservationBase):
    id: int

    class Config:
        from_attributes = True
