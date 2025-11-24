from dataclasses import dataclass, fields


@dataclass
class Item:
    name: str
    link: str
    last_price: str
    price: str
    instalment_id: str

    @classmethod
    def labels(cls):
        return [f.name for f in fields(cls)]
