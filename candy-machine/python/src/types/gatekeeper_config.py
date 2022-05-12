from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
from solana.publickey import PublicKey
import borsh_construct as borsh
from anchorpy.borsh_extension import BorshPubkey


class GatekeeperConfigJSON(typing.TypedDict):
    gatekeeper_network: str
    expire_on_use: bool


@dataclass
class GatekeeperConfig:
    layout: typing.ClassVar = borsh.CStruct(
        "gatekeeper_network" / BorshPubkey, "expire_on_use" / borsh.Bool
    )
    gatekeeper_network: PublicKey
    expire_on_use: bool

    @classmethod
    def from_decoded(cls, obj: Container) -> "GatekeeperConfig":
        return cls(
            gatekeeper_network=obj.gatekeeper_network, expire_on_use=obj.expire_on_use
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "gatekeeper_network": self.gatekeeper_network,
            "expire_on_use": self.expire_on_use,
        }

    def to_json(self) -> GatekeeperConfigJSON:
        return {
            "gatekeeper_network": str(self.gatekeeper_network),
            "expire_on_use": self.expire_on_use,
        }

    @classmethod
    def from_json(cls, obj: GatekeeperConfigJSON) -> "GatekeeperConfig":
        return cls(
            gatekeeper_network=PublicKey(obj["gatekeeper_network"]),
            expire_on_use=obj["expire_on_use"],
        )
