from __future__ import annotations
from . import (
    whitelist_mint_mode,
)
import typing
from dataclasses import dataclass
from construct import Container
from solana.publickey import PublicKey
import borsh_construct as borsh
from anchorpy.borsh_extension import BorshPubkey


class WhitelistMintSettingsJSON(typing.TypedDict):
    mode: whitelist_mint_mode.WhitelistMintModeJSON
    mint: str
    presale: bool
    discount_price: typing.Optional[int]


@dataclass
class WhitelistMintSettings:
    layout: typing.ClassVar = borsh.CStruct(
        "mode" / whitelist_mint_mode.layout,
        "mint" / BorshPubkey,
        "presale" / borsh.Bool,
        "discount_price" / borsh.Option(borsh.U64),
    )
    mode: whitelist_mint_mode.WhitelistMintModeKind
    mint: PublicKey
    presale: bool
    discount_price: typing.Optional[int]

    @classmethod
    def from_decoded(cls, obj: Container) -> "WhitelistMintSettings":
        return cls(
            mode=whitelist_mint_mode.from_decoded(obj.mode),
            mint=obj.mint,
            presale=obj.presale,
            discount_price=obj.discount_price,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "mode": self.mode.to_encodable(),
            "mint": self.mint,
            "presale": self.presale,
            "discount_price": self.discount_price,
        }

    def to_json(self) -> WhitelistMintSettingsJSON:
        return {
            "mode": self.mode.to_json(),
            "mint": str(self.mint),
            "presale": self.presale,
            "discount_price": self.discount_price,
        }

    @classmethod
    def from_json(cls, obj: WhitelistMintSettingsJSON) -> "WhitelistMintSettings":
        return cls(
            mode=whitelist_mint_mode.from_json(obj["mode"]),
            mint=PublicKey(obj["mint"]),
            presale=obj["presale"],
            discount_price=obj["discount_price"],
        )
