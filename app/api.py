from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from . import crud, models, schemas, database
import csv
import io

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


@router.patch("/reservations/{reservation_id}", response_model=schemas.Reservation)
def update_reservation_endpoint(reservation_id: int, reservation_update: schemas.ReservationUpdate,
                                db: Session = Depends(database.get_db)):
    updated_reservation = crud.update_reservation(db=db, reservation_id=reservation_id,
                                                  reservation_update=reservation_update)
    if updated_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return updated_reservation


@router.get("/reservations/export_csv/")
async def export_reservations_csv(db: Session = Depends(database.get_db)):
    reservations = crud.get_reservations(db)
    stream = io.StringIO()
    csv_writer = csv.writer(stream)

    # Write CSV Headers
    csv_writer.writerow(['id', 'number_of_people', 'full_name', 'email', 'phone_number', 'address', 'payment_card_info',
                         'stay_duration', 'room_type', 'paypal_email', 'paypal_password'])

    # Write reservation data
    for reservation in reservations:
        csv_writer.writerow([reservation.id, reservation.number_of_people, reservation.full_name, reservation.email,
                             reservation.phone_number, reservation.address, reservation.payment_card_info,
                             reservation.stay_duration, reservation.room_type, reservation.paypal_email,
                             reservation.paypal_password])

    response = Response(content=stream.getvalue(), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=export_reservations.csv"
    return response
