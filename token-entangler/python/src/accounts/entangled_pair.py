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


class EntangledPairJSON(typing.TypedDict):
    treasury_mint: str
    mint_a: str
    mint_b: str
    token_a_escrow: str
    token_b_escrow: str
    authority: str
    bump: int
    token_a_escrow_bump: int
    token_b_escrow_bump: int
    price: int
    paid: bool
    pays_every_time: bool


@dataclass
class EntangledPair:
    discriminator: typing.ClassVar = b"\x85v\x14\xd2\x016\xact"
    layout: typing.ClassVar = borsh.CStruct(
        "treasury_mint" / BorshPubkey,
        "mint_a" / BorshPubkey,
        "mint_b" / BorshPubkey,
        "token_a_escrow" / BorshPubkey,
        "token_b_escrow" / BorshPubkey,
        "authority" / BorshPubkey,
        "bump" / borsh.U8,
        "token_a_escrow_bump" / borsh.U8,
        "token_b_escrow_bump" / borsh.U8,
        "price" / borsh.U64,
        "paid" / borsh.Bool,
        "pays_every_time" / borsh.Bool,
    )
    treasury_mint: PublicKey
    mint_a: PublicKey
    mint_b: PublicKey
    token_a_escrow: PublicKey
    token_b_escrow: PublicKey
    authority: PublicKey
    bump: int
    token_a_escrow_bump: int
    token_b_escrow_bump: int
    price: int
    paid: bool
    pays_every_time: bool

    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: PublicKey,
        commitment: typing.Optional[Commitment] = None,
    ) -> typing.Optional["EntangledPair"]:
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
    ) -> typing.List[typing.Optional["EntangledPair"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["EntangledPair"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != PROGRAM_ID:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "EntangledPair":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = EntangledPair.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(
            treasury_mint=dec.treasury_mint,
            mint_a=dec.mint_a,
            mint_b=dec.mint_b,
            token_a_escrow=dec.token_a_escrow,
            token_b_escrow=dec.token_b_escrow,
            authority=dec.authority,
            bump=dec.bump,
            token_a_escrow_bump=dec.token_a_escrow_bump,
            token_b_escrow_bump=dec.token_b_escrow_bump,
            price=dec.price,
            paid=dec.paid,
            pays_every_time=dec.pays_every_time,
        )

    def to_json(self) -> EntangledPairJSON:
        return {
            "treasury_mint": str(self.treasury_mint),
            "mint_a": str(self.mint_a),
            "mint_b": str(self.mint_b),
            "token_a_escrow": str(self.token_a_escrow),
            "token_b_escrow": str(self.token_b_escrow),
            "authority": str(self.authority),
            "bump": self.bump,
            "token_a_escrow_bump": self.token_a_escrow_bump,
            "token_b_escrow_bump": self.token_b_escrow_bump,
            "price": self.price,
            "paid": self.paid,
            "pays_every_time": self.pays_every_time,
        }

    @classmethod
    def from_json(cls, obj: EntangledPairJSON) -> "EntangledPair":
        return cls(
            treasury_mint=PublicKey(obj["treasury_mint"]),
            mint_a=PublicKey(obj["mint_a"]),
            mint_b=PublicKey(obj["mint_b"]),
            token_a_escrow=PublicKey(obj["token_a_escrow"]),
            token_b_escrow=PublicKey(obj["token_b_escrow"]),
            authority=PublicKey(obj["authority"]),
            bump=obj["bump"],
            token_a_escrow_bump=obj["token_a_escrow_bump"],
            token_b_escrow_bump=obj["token_b_escrow_bump"],
            price=obj["price"],
            paid=obj["paid"],
            pays_every_time=obj["pays_every_time"],
        )
