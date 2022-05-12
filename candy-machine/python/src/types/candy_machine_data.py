from __future__ import annotations
from . import (
    whitelist_mint_settings,
    gatekeeper_config,
    end_settings,
    hidden_settings,
    creator,
)
import typing
from dataclasses import dataclass
from construct import Container, Construct
import borsh_construct as borsh


class CandyMachineDataJSON(typing.TypedDict):
    uuid: str
    price: int
    symbol: str
    seller_fee_basis_points: int
    max_supply: int
    is_mutable: bool
    retain_authority: bool
    go_live_date: typing.Optional[int]
    end_settings: typing.Optional[end_settings.EndSettingsJSON]
    creators: list[creator.CreatorJSON]
    hidden_settings: typing.Optional[hidden_settings.HiddenSettingsJSON]
    whitelist_mint_settings: typing.Optional[
        whitelist_mint_settings.WhitelistMintSettingsJSON
    ]
    items_available: int
    gatekeeper: typing.Optional[gatekeeper_config.GatekeeperConfigJSON]


@dataclass
class CandyMachineData:
    layout: typing.ClassVar = borsh.CStruct(
        "uuid" / borsh.String,
        "price" / borsh.U64,
        "symbol" / borsh.String,
        "seller_fee_basis_points" / borsh.U16,
        "max_supply" / borsh.U64,
        "is_mutable" / borsh.Bool,
        "retain_authority" / borsh.Bool,
        "go_live_date" / borsh.Option(borsh.I64),
        "end_settings" / borsh.Option(end_settings.EndSettings.layout),
        "creators" / borsh.Vec(typing.cast(Construct, creator.Creator.layout)),
        "hidden_settings" / borsh.Option(hidden_settings.HiddenSettings.layout),
        "whitelist_mint_settings"
        / borsh.Option(whitelist_mint_settings.WhitelistMintSettings.layout),
        "items_available" / borsh.U64,
        "gatekeeper" / borsh.Option(gatekeeper_config.GatekeeperConfig.layout),
    )
    uuid: str
    price: int
    symbol: str
    seller_fee_basis_points: int
    max_supply: int
    is_mutable: bool
    retain_authority: bool
    go_live_date: typing.Optional[int]
    end_settings: typing.Optional[end_settings.EndSettings]
    creators: list[creator.Creator]
    hidden_settings: typing.Optional[hidden_settings.HiddenSettings]
    whitelist_mint_settings: typing.Optional[
        whitelist_mint_settings.WhitelistMintSettings
    ]
    items_available: int
    gatekeeper: typing.Optional[gatekeeper_config.GatekeeperConfig]

    @classmethod
    def from_decoded(cls, obj: Container) -> "CandyMachineData":
        return cls(
            uuid=obj.uuid,
            price=obj.price,
            symbol=obj.symbol,
            seller_fee_basis_points=obj.seller_fee_basis_points,
            max_supply=obj.max_supply,
            is_mutable=obj.is_mutable,
            retain_authority=obj.retain_authority,
            go_live_date=obj.go_live_date,
            end_settings=(
                None
                if obj.end_settings is None
                else end_settings.EndSettings.from_decoded(obj.end_settings)
            ),
            creators=list(
                map(lambda item: creator.Creator.from_decoded(item), obj.creators)
            ),
            hidden_settings=(
                None
                if obj.hidden_settings is None
                else hidden_settings.HiddenSettings.from_decoded(obj.hidden_settings)
            ),
            whitelist_mint_settings=(
                None
                if obj.whitelist_mint_settings is None
                else whitelist_mint_settings.WhitelistMintSettings.from_decoded(
                    obj.whitelist_mint_settings
                )
            ),
            items_available=obj.items_available,
            gatekeeper=(
                None
                if obj.gatekeeper is None
                else gatekeeper_config.GatekeeperConfig.from_decoded(obj.gatekeeper)
            ),
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "uuid": self.uuid,
            "price": self.price,
            "symbol": self.symbol,
            "seller_fee_basis_points": self.seller_fee_basis_points,
            "max_supply": self.max_supply,
            "is_mutable": self.is_mutable,
            "retain_authority": self.retain_authority,
            "go_live_date": self.go_live_date,
            "end_settings": (
                None if self.end_settings is None else self.end_settings.to_encodable()
            ),
            "creators": list(map(lambda item: item.to_encodable(), self.creators)),
            "hidden_settings": (
                None
                if self.hidden_settings is None
                else self.hidden_settings.to_encodable()
            ),
            "whitelist_mint_settings": (
                None
                if self.whitelist_mint_settings is None
                else self.whitelist_mint_settings.to_encodable()
            ),
            "items_available": self.items_available,
            "gatekeeper": (
                None if self.gatekeeper is None else self.gatekeeper.to_encodable()
            ),
        }

    def to_json(self) -> CandyMachineDataJSON:
        return {
            "uuid": self.uuid,
            "price": self.price,
            "symbol": self.symbol,
            "seller_fee_basis_points": self.seller_fee_basis_points,
            "max_supply": self.max_supply,
            "is_mutable": self.is_mutable,
            "retain_authority": self.retain_authority,
            "go_live_date": self.go_live_date,
            "end_settings": (
                None if self.end_settings is None else self.end_settings.to_json()
            ),
            "creators": list(map(lambda item: item.to_json(), self.creators)),
            "hidden_settings": (
                None if self.hidden_settings is None else self.hidden_settings.to_json()
            ),
            "whitelist_mint_settings": (
                None
                if self.whitelist_mint_settings is None
                else self.whitelist_mint_settings.to_json()
            ),
            "items_available": self.items_available,
            "gatekeeper": (
                None if self.gatekeeper is None else self.gatekeeper.to_json()
            ),
        }

    @classmethod
    def from_json(cls, obj: CandyMachineDataJSON) -> "CandyMachineData":
        return cls(
            uuid=obj["uuid"],
            price=obj["price"],
            symbol=obj["symbol"],
            seller_fee_basis_points=obj["seller_fee_basis_points"],
            max_supply=obj["max_supply"],
            is_mutable=obj["is_mutable"],
            retain_authority=obj["retain_authority"],
            go_live_date=obj["go_live_date"],
            end_settings=(
                None
                if obj["end_settings"] is None
                else end_settings.EndSettings.from_json(obj["end_settings"])
            ),
            creators=list(
                map(lambda item: creator.Creator.from_json(item), obj["creators"])
            ),
            hidden_settings=(
                None
                if obj["hidden_settings"] is None
                else hidden_settings.HiddenSettings.from_json(obj["hidden_settings"])
            ),
            whitelist_mint_settings=(
                None
                if obj["whitelist_mint_settings"] is None
                else whitelist_mint_settings.WhitelistMintSettings.from_json(
                    obj["whitelist_mint_settings"]
                )
            ),
            items_available=obj["items_available"],
            gatekeeper=(
                None
                if obj["gatekeeper"] is None
                else gatekeeper_config.GatekeeperConfig.from_json(obj["gatekeeper"])
            ),
        )
