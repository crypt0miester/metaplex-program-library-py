from __future__ import annotations
from . import (
    end_setting_type,
)
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class EndSettingsJSON(typing.TypedDict):
    end_setting_type: end_setting_type.EndSettingTypeJSON
    number: int


@dataclass
class EndSettings:
    layout: typing.ClassVar = borsh.CStruct(
        "end_setting_type" / end_setting_type.layout, "number" / borsh.U64
    )
    end_setting_type: end_setting_type.EndSettingTypeKind
    number: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "EndSettings":
        return cls(
            end_setting_type=end_setting_type.from_decoded(obj.end_setting_type),
            number=obj.number,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "end_setting_type": self.end_setting_type.to_encodable(),
            "number": self.number,
        }

    def to_json(self) -> EndSettingsJSON:
        return {
            "end_setting_type": self.end_setting_type.to_json(),
            "number": self.number,
        }

    @classmethod
    def from_json(cls, obj: EndSettingsJSON) -> "EndSettings":
        return cls(
            end_setting_type=end_setting_type.from_json(obj["end_setting_type"]),
            number=obj["number"],
        )
