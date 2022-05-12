from __future__ import annotations
from . import (
    data_v2,
)
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class CreateMetadataAccountArgsV2JSON(typing.TypedDict):
    data: data_v2.DataV2JSON
    is_mut: bool


@dataclass
class CreateMetadataAccountArgsV2:
    layout: typing.ClassVar = borsh.CStruct(
        "data" / data_v2.DataV2.layout, "is_mut" / borsh.Bool
    )
    data: data_v2.DataV2
    is_mut: bool

    @classmethod
    def from_decoded(cls, obj: Container) -> "CreateMetadataAccountArgsV2":
        return cls(data=data_v2.DataV2.from_decoded(obj.data), is_mut=obj.is_mut)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"data": self.data.to_encodable(), "is_mut": self.is_mut}

    def to_json(self) -> CreateMetadataAccountArgsV2JSON:
        return {"data": self.data.to_json(), "is_mut": self.is_mut}

    @classmethod
    def from_json(
        cls, obj: CreateMetadataAccountArgsV2JSON
    ) -> "CreateMetadataAccountArgsV2":
        return cls(data=data_v2.DataV2.from_json(obj["data"]), is_mut=obj["is_mut"])
