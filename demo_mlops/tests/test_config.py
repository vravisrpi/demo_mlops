from attr.setters import NO_OP
import pytest


class NotInRange(Exception):
    def __init__(self, messeage="Entered Values are not in Range"):
        self.messeage = messeage
        super().__init__(self.messeage)

# def test_any():
#     a = 2,
#     b = 2,
#     assert a==b


def test_any():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10, 20):
            raise NotInRange
