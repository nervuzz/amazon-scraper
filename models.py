from pydantic import BaseModel


class Price(BaseModel):
    displayString: str
    fraction: int
    symbol: str
    whole: int


class PriceInfo(BaseModel):
    priceToPay: Price


class LegoSet(BaseModel):
    asin: str
    detailPageLink: str
    imgURL: str
    priceInfo: PriceInfo
    title: str
    setNumber: str = None
