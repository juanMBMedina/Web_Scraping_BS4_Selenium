import re
from dataclasses import dataclass, field, fields
from logger import logger
from extract.utils import NONE_TEXT, short_uuid


@dataclass
class Instalment:
    _id: str = field(default_factory=short_uuid, init=False, repr=False)
    number: str
    amount: str
    interest_rate: str

    _pattern = re.compile(r"^(\d+).+?(\$[\d\.]+).+?(\d+[.,]?\d*)%.+$", re.IGNORECASE)

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value):
        raise AttributeError("The ID Instalment does not support modification.")

    @staticmethod
    def from_text(text: str) -> "Instalment":

        if text == NONE_TEXT:
            logger.warning(
                "The value for instalment is 0. Returning default Instalment."
            )
            return Instalment(number="0", amount="0", interest_rate="0")

        match = Instalment._pattern.search(text.strip())
        if not match:
            logger.error(f"Invalid instalment text: {text}")
            raise ValueError(f"Invalid text: {text}")

        number = int(match.group(1))
        amount = match.group(2)
        interest_rate = match.group(3)

        return Instalment(number=number, amount=amount, interest_rate=interest_rate)

    @classmethod
    def labels(cls):
        return [f.name for f in fields(cls)]
