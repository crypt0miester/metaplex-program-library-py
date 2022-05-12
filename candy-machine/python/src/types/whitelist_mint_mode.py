from __future__ import annotations
import typing
from dataclasses import dataclass
from anchorpy.borsh_extension import EnumForCodegen
import borsh_construct as borsh


class BurnEveryTimeJSON(typing.TypedDict):
    kind: typing.Literal["BurnEveryTime"]


class NeverBurnJSON(typing.TypedDict):
    kind: typing.Literal["NeverBurn"]


@dataclass
class BurnEveryTime:
    discriminator: typing.ClassVar = 0
    kind: typing.ClassVar = "BurnEveryTime"

    @classmethod
    def to_json(cls) -> BurnEveryTimeJSON:
        return BurnEveryTimeJSON(
            kind="BurnEveryTime",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "BurnEveryTime": {},
        }


@dataclass
class NeverBurn:
    discriminator: typing.ClassVar = 1
    kind: typing.ClassVar = "NeverBurn"

    @classmethod
    def to_json(cls) -> NeverBurnJSON:
        return NeverBurnJSON(
            kind="NeverBurn",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "NeverBurn": {},
        }


WhitelistMintModeKind = typing.Union[BurnEveryTime, NeverBurn]
WhitelistMintModeJSON = typing.Union[BurnEveryTimeJSON, NeverBurnJSON]


def from_decoded(obj: dict) -> WhitelistMintModeKind:
    if not isinstance(obj, dict):
        raise ValueError("Invalid enum object")
    if "BurnEveryTime" in obj:
        return BurnEveryTime()
    if "NeverBurn" in obj:
        return NeverBurn()
    raise ValueError("Invalid enum object")


def from_json(obj: WhitelistMintModeJSON) -> WhitelistMintModeKind:
    if obj["kind"] == "BurnEveryTime":
        return BurnEveryTime()
    if obj["kind"] == "NeverBurn":
        return NeverBurn()
    kind = obj["kind"]
    raise ValueError(f"Unrecognized enum kind: {kind}")


layout = EnumForCodegen(
    "BurnEveryTime" / borsh.CStruct(), "NeverBurn" / borsh.CStruct()
)
