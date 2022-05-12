from __future__ import annotations
from . import (
    data,
)
import typing
from dataclasses import dataclass
from construct import Container
from solana.publickey import PublicKey
import borsh_construct as borsh
from anchorpy.borsh_extension import BorshPubkey


class UpdateMetadataAccountArgsJSON(typing.TypedDict):
    data: typing.Optional[data.DataJSON]
    update_authority: typing.Optional[str]
    primary_sale_happened: typing.Optional[bool]


@dataclass
class UpdateMetadataAccountArgs:
    layout: typing.ClassVar = borsh.CStruct(
        "data" / borsh.Option(data.Data.layout),
        "update_authority" / borsh.Option(BorshPubkey),
        "primary_sale_happened" / borsh.Option(borsh.Bool),
    )
    data: typing.Optional[data.Data]
    update_authority: typing.Optional[PublicKey]
    primary_sale_happened: typing.Optional[bool]

    @classmethod
    def from_decoded(cls, obj: Container) -> "UpdateMetadataAccountArgs":
        return cls(
            data=(None if obj.data is None else data.Data.from_decoded(obj.data)),
            update_authority=obj.update_authority,
            primary_sale_happened=obj.primary_sale_happened,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "data": (None if self.data is None else self.data.to_encodable()),
            "update_authority": self.update_authority,
            "primary_sale_happened": self.primary_sale_happened,
        }

    def to_json(self) -> UpdateMetadataAccountArgsJSON:
        return {
            "data": (None if self.data is None else self.data.to_json()),
            "update_authority": (
                None if self.update_authority is None else str(self.update_authority)
            ),
            "primary_sale_happened": self.primary_sale_happened,
        }

    @classmethod
    def from_json(
        cls, obj: UpdateMetadataAccountArgsJSON
    ) -> "UpdateMetadataAccountArgs":
        return cls(
            data=(None if obj["data"] is None else data.Data.from_json(obj["data"])),
            update_authority=(
                None
                if obj["update_authority"] is None
                else PublicKey(obj["update_authority"])
            ),
            primary_sale_happened=obj["primary_sale_happened"],
        )
