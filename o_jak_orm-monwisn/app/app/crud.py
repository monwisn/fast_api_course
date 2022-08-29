from sqlalchemy.orm import Session

from . import models, schemas


def get_shippers(db: Session):
    return db.query(models.Shipper).all()


def get_shipper(db: Session, shipper_id: int):
    return (
        db.query(models.Shipper).filter(models.Shipper.ShipperID == shipper_id).first()
    )


# task 5.1

def get_suppliers(db: Session):
    return db.query(models.Supplier).order_by(models.Supplier.SupplierID).all()
    # return db.query(models.Supplier).order_by(models.Supplier.SupplierID.asc()).all()


def get_supplier(db: Session, supplier_id: int):
    return (
        db.query(models.Supplier).filter(models.Supplier.SupplierID == supplier_id).first()
    )


# task 5.2

def get_supplier_products(db: Session, supplier_id: int):
    return db.query(models.Product).filter(models.Product.SupplierID == supplier_id).order_by(
        models.Product.ProductID.desc()).all()


def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.CategoryID == category_id).first()


# task 5.3

def get_last_supplier_id(db: Session):
    return db.query(models.Supplier.SupplierID).order_by(models.Supplier.SupplierID.desc()).first()[0]


def create_supplier(db: Session, supplier: schemas.SupplierCreate):
    new_id = get_last_supplier_id(db) + 1
    # print(new_id)

    db_supplier = models.Supplier(SupplierID=new_id,
                                  CompanyName=supplier.CompanyName,
                                  ContactName=supplier.ContactName,
                                  ContactTitle=supplier.ContactTitle,
                                  Address=supplier.Address,
                                  City=supplier.City,
                                  Region=supplier.Region,
                                  PostalCode=supplier.PostalCode,
                                  Country=supplier.Country,
                                  Phone=supplier.Phone,
                                  Fax=supplier.Fax)

    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier


# task 5.4

def update_supplier(db: Session, supplier_id: int, supplier: schemas.SupplierCreate):
    db_supplier = db.query(models.Supplier).filter(models.Supplier.SupplierID == supplier_id).first()

    for item in supplier:
        if item[1] is not None:
            if item[0] == 'CompanyName':
                db_supplier.CompanyName = item[1]
            if item[0] == 'ContactName':
                db_supplier.ContactName = item[1]
            if item[0] == 'ContactTitle':
                db_supplier.ContactTitle = item[1]
            if item[0] == 'Address':
                db_supplier.Address = item[1]
            if item[0] == 'City':
                db_supplier.City = item[1]
            if item[0] == 'Region':
                db_supplier.Region = item[1]
            if item[0] == 'PostalCode':
                db_supplier.PostalCode = item[1]
            if item[0] == 'Country':
                db_supplier.Country = item[1]
            if item[0] == 'Phone':
                db_supplier.Phone = item[1]
            if item[0] == 'Fax':
                db_supplier.Fax = item[1]
    db.commit()
    db.refresh(db_supplier)
    return db_supplier


# task 5.5

def delete_supplier(db: Session, supplier_id: int):
    db_supplier = db.query(models.Supplier).filter(models.Supplier.SupplierID == supplier_id).first()
    db.delete(db_supplier)
    db.commit()

    return db_supplier
