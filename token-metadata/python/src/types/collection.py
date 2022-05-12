from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
from solana.publickey import PublicKey
import borsh_construct as borsh
from anchorpy.borsh_extension import BorshPubkey


class CollectionJSON(typing.TypedDict):
    verified: bool
    key: str


@dataclass
class Collection:
    layout: typing.ClassVar = borsh.CStruct(
        "verified" / borsh.Bool, "key" / BorshPubkey
    )
    verified: bool
    key: PublicKey

    @classmethod
    def from_decoded(cls, obj: Container) -> "Collection":
        return cls(verified=obj.verified, key=obj.key)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"verified": self.verified, "key": self.key}

    def to_json(self) -> CollectionJSON:
        return {"verified": self.verified, "key": str(self.key)}

    @classmethod
    def from_json(cls, obj: CollectionJSON) -> "Collection":
        return cls(verified=obj["verified"], key=PublicKey(obj["key"]))
