from __future__ import annotations
import typing
from dataclasses import dataclass
from anchorpy.borsh_extension import EnumForCodegen
import borsh_construct as borsh


class DateJSON(typing.TypedDict):
    kind: typing.Literal["Date"]


class AmountJSON(typing.TypedDict):
    kind: typing.Literal["Amount"]


@dataclass
class Date:
    discriminator: typing.ClassVar = 0
    kind: typing.ClassVar = "Date"

    @classmethod
    def to_json(cls) -> DateJSON:
        return DateJSON(
            kind="Date",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "Date": {},
        }


@dataclass
class Amount:
    discriminator: typing.ClassVar = 1
    kind: typing.ClassVar = "Amount"

    @classmethod
    def to_json(cls) -> AmountJSON:
        return AmountJSON(
            kind="Amount",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "Amount": {},
        }


EndSettingTypeKind = typing.Union[Date, Amount]
EndSettingTypeJSON = typing.Union[DateJSON, AmountJSON]


def from_decoded(obj: dict) -> EndSettingTypeKind:
    if not isinstance(obj, dict):
        raise ValueError("Invalid enum object")
    if "Date" in obj:
        return Date()
    if "Amount" in obj:
        return Amount()
    raise ValueError("Invalid enum object")


def from_json(obj: EndSettingTypeJSON) -> EndSettingTypeKind:
    if obj["kind"] == "Date":
        return Date()
    if obj["kind"] == "Amount":
        return Amount()
    kind = obj["kind"]
    raise ValueError(f"Unrecognized enum kind: {kind}")


layout = EnumForCodegen("Date" / borsh.CStruct(), "Amount" / borsh.CStruct())
