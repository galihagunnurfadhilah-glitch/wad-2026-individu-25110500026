from pydantic import BaseModel, Field
from typing import Literal


class MenuCreate(BaseModel):
    sku: str = Field(pattern=r"^KOPI-\d{3}$")
    nama: str
    harga: float = Field(gt=0)
    kategori: Literal["kopi", "non-kopi", "makanan"]


class MenuOut(BaseModel):
    id: int
    sku: str
    nama: str
    harga: float
    kategori: Literal["kopi", "non-kopi", "makanan"]