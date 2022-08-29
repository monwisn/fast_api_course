from pydantic import BaseModel, PositiveInt, constr


class Shipper(BaseModel):
    ShipperID: PositiveInt
    CompanyName: constr(max_length=40)
    Phone: constr(max_length=24)

    class Config:
        orm_mode = True


class Supplier(BaseModel):
    SupplierID: PositiveInt
    CompanyName: constr(max_length=40)

    class Config:
        orm_mode = True


class ExtendedSupplier(BaseModel):
    SupplierID: PositiveInt
    CompanyName: constr(max_length=40)
    ContactName: constr(max_length=30) = None
    ContactTitle: constr(max_length=30) = None
    Address: constr(max_length=60) = None
    City: constr(max_length=15) = None
    Region: constr(max_length=15) = None
    PostalCode: constr(max_length=10) = None
    Country: constr(max_length=15) = None
    Phone: constr(max_length=24) = None
    Fax: constr(max_length=24) = None
    HomePage: constr(max_length=300) = None

    class Config:
        orm_mode = True


class Category(BaseModel):
    CategoryID: PositiveInt
    CategoryName: constr(max_length=30) = None

    class Config:
        orm_mode = True


class SupplierProducts(BaseModel):
    ProductID: PositiveInt
    ProductName: constr(max_length=40)
    Category: Category
    Discontinued: bool = None

    class Config:
        orm_mode = True


class SupplierCreate(BaseModel):
    CompanyName: constr(max_length=40)
    ContactName: constr(max_length=30) = None
    ContactTitle: constr(max_length=30) = None
    Address: constr(max_length=60) = None
    City: constr(max_length=15) = None
    Region: constr(max_length=15) = None
    PostalCode: constr(max_length=10) = None
    Country: constr(max_length=15) = None
    Phone: constr(max_length=24) = None
    Fax: constr(max_length=24) = None
    HomePage: constr(max_length=300) = None

    class Config:
        orm_mode = True


class SupplierUpdate(BaseModel):
    CompanyName: constr(max_length=40) = None
    ContactName: constr(max_length=30) = None
    ContactTitle: constr(max_length=30) = None
    Address: constr(max_length=60) = None
    City: constr(max_length=15) = None
    Region: constr(max_length=15) = None
    PostalCode: constr(max_length=10) = None
    Country: constr(max_length=15) = None
    Phone: constr(max_length=24) = None
    Fax: constr(max_length=24) = None
    HomePage: constr(max_length=300) = None

    class Config:
        orm_mode = True
