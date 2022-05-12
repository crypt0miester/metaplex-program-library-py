from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class HiddenSettingsJSON(typing.TypedDict):
    name: str
    uri: str
    hash: list[int]


@dataclass
class HiddenSettings:
    layout: typing.ClassVar = borsh.CStruct(
        "name" / borsh.String, "uri" / borsh.String, "hash" / borsh.U8[32]
    )
    name: str
    uri: str
    hash: list[int]

    @classmethod
    def from_decoded(cls, obj: Container) -> "HiddenSettings":
        return cls(name=obj.name, uri=obj.uri, hash=obj.hash)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"name": self.name, "uri": self.uri, "hash": self.hash}

    def to_json(self) -> HiddenSettingsJSON:
        return {"name": self.name, "uri": self.uri, "hash": self.hash}

    @classmethod
    def from_json(cls, obj: HiddenSettingsJSON) -> "HiddenSettings":
        return cls(name=obj["name"], uri=obj["uri"], hash=obj["hash"])
