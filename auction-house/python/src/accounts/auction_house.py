import typing
from dataclasses import dataclass
from base64 import b64decode
from solana.publickey import PublicKey
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Commitment
import borsh_construct as borsh
from anchorpy.coder.accounts import ACCOUNT_DISCRIMINATOR_SIZE
from anchorpy.error import AccountInvalidDiscriminator
from anchorpy.utils.rpc import get_multiple_accounts
from anchorpy.borsh_extension import BorshPubkey
from ..program_id import PROGRAM_ID


class AuctionHouseJSON(typing.TypedDict):
    auction_house_fee_account: str
    auction_house_treasury: str
    treasury_withdrawal_destination: str
    fee_withdrawal_destination: str
    treasury_mint: str
    authority: str
    creator: str
    bump: int
    treasury_bump: int
    fee_payer_bump: int
    seller_fee_basis_points: int
    requires_sign_off: bool
    can_change_sale_price: bool


@dataclass
class AuctionHouse:
    discriminator: typing.ClassVar = b"(l\xd7k\xd5U\xf50"
    layout: typing.ClassVar = borsh.CStruct(
        "auction_house_fee_account" / BorshPubkey,
        "auction_house_treasury" / BorshPubkey,
        "treasury_withdrawal_destination" / BorshPubkey,
        "fee_withdrawal_destination" / BorshPubkey,
        "treasury_mint" / BorshPubkey,
        "authority" / BorshPubkey,
        "creator" / BorshPubkey,
        "bump" / borsh.U8,
        "treasury_bump" / borsh.U8,
        "fee_payer_bump" / borsh.U8,
        "seller_fee_basis_points" / borsh.U16,
        "requires_sign_off" / borsh.Bool,
        "can_change_sale_price" / borsh.Bool,
    )
    auction_house_fee_account: PublicKey
    auction_house_treasury: PublicKey
    treasury_withdrawal_destination: PublicKey
    fee_withdrawal_destination: PublicKey
    treasury_mint: PublicKey
    authority: PublicKey
    creator: PublicKey
    bump: int
    treasury_bump: int
    fee_payer_bump: int
    seller_fee_basis_points: int
    requires_sign_off: bool
    can_change_sale_price: bool

    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: PublicKey,
        commitment: typing.Optional[Commitment] = None,
    ) -> typing.Optional["AuctionHouse"]:
        resp = await conn.get_account_info(address, commitment=commitment)
        info = resp["result"]["value"]
        if info is None:
            return None
        if info["owner"] != str(PROGRAM_ID):
            raise ValueError("Account does not belong to this program")
        bytes_data = b64decode(info["data"][0])
        return cls.decode(bytes_data)

    @classmethod
    async def fetch_multiple(
        cls,
        conn: AsyncClient,
        addresses: list[PublicKey],
        commitment: typing.Optional[Commitment] = None,
    ) -> typing.List[typing.Optional["AuctionHouse"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["AuctionHouse"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != PROGRAM_ID:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "AuctionHouse":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = AuctionHouse.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(
            auction_house_fee_account=dec.auction_house_fee_account,
            auction_house_treasury=dec.auction_house_treasury,
            treasury_withdrawal_destination=dec.treasury_withdrawal_destination,
            fee_withdrawal_destination=dec.fee_withdrawal_destination,
            treasury_mint=dec.treasury_mint,
            authority=dec.authority,
            creator=dec.creator,
            bump=dec.bump,
            treasury_bump=dec.treasury_bump,
            fee_payer_bump=dec.fee_payer_bump,
            seller_fee_basis_points=dec.seller_fee_basis_points,
            requires_sign_off=dec.requires_sign_off,
            can_change_sale_price=dec.can_change_sale_price,
        )

    def to_json(self) -> AuctionHouseJSON:
        return {
            "auction_house_fee_account": str(self.auction_house_fee_account),
            "auction_house_treasury": str(self.auction_house_treasury),
            "treasury_withdrawal_destination": str(
                self.treasury_withdrawal_destination
            ),
            "fee_withdrawal_destination": str(self.fee_withdrawal_destination),
            "treasury_mint": str(self.treasury_mint),
            "authority": str(self.authority),
            "creator": str(self.creator),
            "bump": self.bump,
            "treasury_bump": self.treasury_bump,
            "fee_payer_bump": self.fee_payer_bump,
            "seller_fee_basis_points": self.seller_fee_basis_points,
            "requires_sign_off": self.requires_sign_off,
            "can_change_sale_price": self.can_change_sale_price,
        }

    @classmethod
    def from_json(cls, obj: AuctionHouseJSON) -> "AuctionHouse":
        return cls(
            auction_house_fee_account=PublicKey(obj["auction_house_fee_account"]),
            auction_house_treasury=PublicKey(obj["auction_house_treasury"]),
            treasury_withdrawal_destination=PublicKey(
                obj["treasury_withdrawal_destination"]
            ),
            fee_withdrawal_destination=PublicKey(obj["fee_withdrawal_destination"]),
            treasury_mint=PublicKey(obj["treasury_mint"]),
            authority=PublicKey(obj["authority"]),
            creator=PublicKey(obj["creator"]),
            bump=obj["bump"],
            treasury_bump=obj["treasury_bump"],
            fee_payer_bump=obj["fee_payer_bump"],
            seller_fee_basis_points=obj["seller_fee_basis_points"],
            requires_sign_off=obj["requires_sign_off"],
            can_change_sale_price=obj["can_change_sale_price"],
        )
