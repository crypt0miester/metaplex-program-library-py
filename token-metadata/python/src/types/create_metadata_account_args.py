from __future__ import annotations
from . import (
    data,
)
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class CreateMetadataAccountArgsJSON(typing.TypedDict):
    data: data.DataJSON
    is_mut: bool


@dataclass
class CreateMetadataAccountArgs:
    layout: typing.ClassVar = borsh.CStruct(
        "data" / data.Data.layout, "is_mut" / borsh.Bool
    )
    data: data.Data
    is_mut: bool

    @classmethod
    def from_decoded(cls, obj: Container) -> "CreateMetadataAccountArgs":
        return cls(data=data.Data.from_decoded(obj.data), is_mut=obj.is_mut)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"data": self.data.to_encodable(), "is_mut": self.is_mut}

    def to_json(self) -> CreateMetadataAccountArgsJSON:
        return {"data": self.data.to_json(), "is_mut": self.is_mut}

    @classmethod
    def from_json(
        cls, obj: CreateMetadataAccountArgsJSON
    ) -> "CreateMetadataAccountArgs":
        return cls(data=data.Data.from_json(obj["data"]), is_mut=obj["is_mut"])
