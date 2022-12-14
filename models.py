import re

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


class StoreItems(BaseModel):
    items: list[BaseModel] = []

    def from_product_list(self, product_list):
        """Fill store items from product list."""

        for product in product_list:
            LS = LegoSet(**product)
            s = re.search(r"(\d{4,6})", LS.title)
            LS.setNumber = s.group() if s else "unknown"
            self.items.append(LS)
