from sqlalchemy.orm import Session
from . import models, schemas


def get_reservation(db: Session, reservation_id: int):
    return db.query(models.Reservation).filter(models.Reservation.id == reservation_id).first()


def get_reservations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Reservation).offset(skip).limit(limit).all()


def create_reservation(db: Session, reservation: schemas.ReservationCreate):
    db_reservation = models.Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation


def update_reservation(db: Session, reservation_id: int, reservation_update: schemas.ReservationUpdate):
    db_reservation = db.query(models.Reservation).filter(models.Reservation.id == reservation_id).first()
    if db_reservation is None:
        return None
    for var, value in vars(reservation_update).items():
        setattr(db_reservation, var, value) if value else None
    db.commit()
    db.refresh(db_reservation)
    return db_reservation
