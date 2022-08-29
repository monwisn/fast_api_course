from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from pydantic import PositiveInt
from sqlalchemy.orm import Session

from . import crud, schemas
from .database import get_db

router = APIRouter()


@router.get("/shippers/{shipper_id}", response_model=schemas.Shipper)
async def get_shipper(shipper_id: PositiveInt, db: Session = Depends(get_db)):
    db_shipper = crud.get_shipper(db, shipper_id)
    if db_shipper is None:
        raise HTTPException(status_code=404, detail="Shipper not found")
    return db_shipper


@router.get("/shippers", response_model=List[schemas.Shipper])
async def get_shippers(db: Session = Depends(get_db)):
    return crud.get_shippers(db)


# task 5.1

@router.get('/suppliers', response_model=List[schemas.Supplier], status_code=200)
def get_supplier(db: Session = Depends(get_db)):
    return crud.get_suppliers(db)


@router.get('/suppliers/{supplier_id}', response_model=schemas.ExtendedSupplier, status_code=200)
def get_supplier(supplier_id: PositiveInt, db: Session = Depends(get_db)):
    db_supplier = crud.get_suppier(db, supplier_id)

    if db_supplier is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
        # raise HTTPException(status_code=404, detail='Supplier not found')

    return db_supplier


# task 5.2

@router.get("/suppliers/{supplier_id}/products", response_model=List[schemas.SupplierProducts], status_code=200)
def get_supplier_products(supplier_id: PositiveInt, db: Session = Depends(get_db)):
    if crud.get_supplier(db, supplier_id) is None:
        # raise HTTPException(status_code=404, detail="Supplier not found")
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    db_supplier_products = crud.get_supplier_products(db, supplier_id)

    for item in db_supplier_products:
        db_category = crud.get_category(db, item.CategoryID)
        schemas.Category(CategoryID=db_category.CategoryID, CategoryName=db_category.CategoryName)
        item.Category = schemas.Category(CategoryID=db_category.CategoryID, CategoryName=db_category.CategoryName)

        return db_supplier_products


# task 5.3

@router.post('/suppliers')
def create_supplier(supplier: schemas.SupplierCreate, db: Session = Depends(get_db), response: Response = Response):
    if supplier.CompanyName is not None or supplier.CompanyName != "":
        response.status_code = status.HTTP_201_CREATED

    return crud.create_supplier(db, supplier)


# task 5.4

@router.put('/suppliers/{supplier_id}', status_code=200)
def update_supplier(supplier_id: PositiveInt, supplier: schemas.SupplierUpdate, db: Session = Depends(get_db)):
    if crud.get_supplier(db, supplier_id) is None:
        # raise HTTPException(status_code=404, detail="Supplier not found")
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    return crud.update_supplier(db, supplier_id, supplier)


# task 5.5

@router.delete('/suppliers/{supplier_id}')
def delete_supplier(supplier_id: PositiveInt, db: Session = Depends(get_db)):
    if crud.get_supplier(db, supplier_id) is None:
        # raise HTTPException(status_code=404, detail='Supplier not found')
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    crud.delete_supplier(db, supplier_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
