from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class ConfigLineJSON(typing.TypedDict):
    name: str
    uri: str


@dataclass
class ConfigLine:
    layout: typing.ClassVar = borsh.CStruct("name" / borsh.String, "uri" / borsh.String)
    name: str
    uri: str

    @classmethod
    def from_decoded(cls, obj: Container) -> "ConfigLine":
        return cls(name=obj.name, uri=obj.uri)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"name": self.name, "uri": self.uri}

    def to_json(self) -> ConfigLineJSON:
        return {"name": self.name, "uri": self.uri}

    @classmethod
    def from_json(cls, obj: ConfigLineJSON) -> "ConfigLine":
        return cls(name=obj["name"], uri=obj["uri"])
