from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class MintPrintingTokensViaTokenArgsJSON(typing.TypedDict):
    supply: int


@dataclass
class MintPrintingTokensViaTokenArgs:
    layout: typing.ClassVar = borsh.CStruct("supply" / borsh.U64)
    supply: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "MintPrintingTokensViaTokenArgs":
        return cls(supply=obj.supply)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"supply": self.supply}

    def to_json(self) -> MintPrintingTokensViaTokenArgsJSON:
        return {"supply": self.supply}

    @classmethod
    def from_json(
        cls, obj: MintPrintingTokensViaTokenArgsJSON
    ) -> "MintPrintingTokensViaTokenArgs":
        return cls(supply=obj["supply"])
