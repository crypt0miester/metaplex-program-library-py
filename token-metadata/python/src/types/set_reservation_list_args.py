from __future__ import annotations
from . import (
    reservation,
)
import typing
from dataclasses import dataclass
from construct import Container, Construct
import borsh_construct as borsh


class SetReservationListArgsJSON(typing.TypedDict):
    reservations: list[reservation.ReservationJSON]
    total_reservation_spots: typing.Optional[int]
    offset: int
    total_spot_offset: int


@dataclass
class SetReservationListArgs:
    layout: typing.ClassVar = borsh.CStruct(
        "reservations"
        / borsh.Vec(typing.cast(Construct, reservation.Reservation.layout)),
        "total_reservation_spots" / borsh.Option(borsh.U64),
        "offset" / borsh.U64,
        "total_spot_offset" / borsh.U64,
    )
    reservations: list[reservation.Reservation]
    total_reservation_spots: typing.Optional[int]
    offset: int
    total_spot_offset: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "SetReservationListArgs":
        return cls(
            reservations=list(
                map(
                    lambda item: reservation.Reservation.from_decoded(item),
                    obj.reservations,
                )
            ),
            total_reservation_spots=obj.total_reservation_spots,
            offset=obj.offset,
            total_spot_offset=obj.total_spot_offset,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "reservations": list(
                map(lambda item: item.to_encodable(), self.reservations)
            ),
            "total_reservation_spots": self.total_reservation_spots,
            "offset": self.offset,
            "total_spot_offset": self.total_spot_offset,
        }

    def to_json(self) -> SetReservationListArgsJSON:
        return {
            "reservations": list(map(lambda item: item.to_json(), self.reservations)),
            "total_reservation_spots": self.total_reservation_spots,
            "offset": self.offset,
            "total_spot_offset": self.total_spot_offset,
        }

    @classmethod
    def from_json(cls, obj: SetReservationListArgsJSON) -> "SetReservationListArgs":
        return cls(
            reservations=list(
                map(
                    lambda item: reservation.Reservation.from_json(item),
                    obj["reservations"],
                )
            ),
            total_reservation_spots=obj["total_reservation_spots"],
            offset=obj["offset"],
            total_spot_offset=obj["total_spot_offset"],
        )
