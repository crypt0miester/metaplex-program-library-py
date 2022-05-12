from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
from solana.publickey import PublicKey
import borsh_construct as borsh
from anchorpy.borsh_extension import BorshPubkey


class CreatorJSON(typing.TypedDict):
    address: str
    verified: bool
    share: int


@dataclass
class Creator:
    layout: typing.ClassVar = borsh.CStruct(
        "address" / BorshPubkey, "verified" / borsh.Bool, "share" / borsh.U8
    )
    address: PublicKey
    verified: bool
    share: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "Creator":
        return cls(address=obj.address, verified=obj.verified, share=obj.share)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"address": self.address, "verified": self.verified, "share": self.share}

    def to_json(self) -> CreatorJSON:
        return {
            "address": str(self.address),
            "verified": self.verified,
            "share": self.share,
        }

    @classmethod
    def from_json(cls, obj: CreatorJSON) -> "Creator":
        return cls(
            address=PublicKey(obj["address"]),
            verified=obj["verified"],
            share=obj["share"],
        )
