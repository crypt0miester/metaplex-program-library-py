from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
from solana.publickey import PublicKey
import borsh_construct as borsh
from anchorpy.borsh_extension import BorshPubkey


class ReservationJSON(typing.TypedDict):
    address: str
    spots_remaining: int
    total_spots: int


@dataclass
class Reservation:
    layout: typing.ClassVar = borsh.CStruct(
        "address" / BorshPubkey,
        "spots_remaining" / borsh.U64,
        "total_spots" / borsh.U64,
    )
    address: PublicKey
    spots_remaining: int
    total_spots: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "Reservation":
        return cls(
            address=obj.address,
            spots_remaining=obj.spots_remaining,
            total_spots=obj.total_spots,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "address": self.address,
            "spots_remaining": self.spots_remaining,
            "total_spots": self.total_spots,
        }

    def to_json(self) -> ReservationJSON:
        return {
            "address": str(self.address),
            "spots_remaining": self.spots_remaining,
            "total_spots": self.total_spots,
        }

    @classmethod
    def from_json(cls, obj: ReservationJSON) -> "Reservation":
        return cls(
            address=PublicKey(obj["address"]),
            spots_remaining=obj["spots_remaining"],
            total_spots=obj["total_spots"],
        )
