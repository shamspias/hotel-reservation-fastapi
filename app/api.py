from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

router = APIRouter()


@router.post('/reservations/', response_model=schemas.Reservation)
def create_reservation(reservation: schemas.ReservationCreate, db: Session = Depends(database.get_db)):
    return crud.create_reservation(db=db, reservation=reservation)


@router.get('/reservations/', response_model=list[schemas.Reservation])
def read_reservations(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    reservations = crud.get_reservations(db, skip=skip, limit=limit)
    return reservations


@router.get('/reservations/{reservation_id}', response_model=schemas.Reservation)
def read_reservation(reservation_id: int, db: Session = Depends(database.get_db)):
    db_reservation = crud.get_reservation(db, reservation_id=reservation_id)
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return db_reservation
