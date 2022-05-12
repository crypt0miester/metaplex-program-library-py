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


class PurchaseReceiptJSON(typing.TypedDict):
    bookkeeper: str
    buyer: str
    seller: str
    auction_house: str
    metadata: str
    token_size: int
    price: int
    bump: int
    created_at: int


@dataclass
class PurchaseReceipt:
    discriminator: typing.ClassVar = b"O\x7f\xde\x89\x9a\x83\x96\x86"
    layout: typing.ClassVar = borsh.CStruct(
        "bookkeeper" / BorshPubkey,
        "buyer" / BorshPubkey,
        "seller" / BorshPubkey,
        "auction_house" / BorshPubkey,
        "metadata" / BorshPubkey,
        "token_size" / borsh.U64,
        "price" / borsh.U64,
        "bump" / borsh.U8,
        "created_at" / borsh.I64,
    )
    bookkeeper: PublicKey
    buyer: PublicKey
    seller: PublicKey
    auction_house: PublicKey
    metadata: PublicKey
    token_size: int
    price: int
    bump: int
    created_at: int

    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: PublicKey,
        commitment: typing.Optional[Commitment] = None,
    ) -> typing.Optional["PurchaseReceipt"]:
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
    ) -> typing.List[typing.Optional["PurchaseReceipt"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["PurchaseReceipt"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != PROGRAM_ID:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "PurchaseReceipt":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = PurchaseReceipt.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(
            bookkeeper=dec.bookkeeper,
            buyer=dec.buyer,
            seller=dec.seller,
            auction_house=dec.auction_house,
            metadata=dec.metadata,
            token_size=dec.token_size,
            price=dec.price,
            bump=dec.bump,
            created_at=dec.created_at,
        )

    def to_json(self) -> PurchaseReceiptJSON:
        return {
            "bookkeeper": str(self.bookkeeper),
            "buyer": str(self.buyer),
            "seller": str(self.seller),
            "auction_house": str(self.auction_house),
            "metadata": str(self.metadata),
            "token_size": self.token_size,
            "price": self.price,
            "bump": self.bump,
            "created_at": self.created_at,
        }

    @classmethod
    def from_json(cls, obj: PurchaseReceiptJSON) -> "PurchaseReceipt":
        return cls(
            bookkeeper=PublicKey(obj["bookkeeper"]),
            buyer=PublicKey(obj["buyer"]),
            seller=PublicKey(obj["seller"]),
            auction_house=PublicKey(obj["auction_house"]),
            metadata=PublicKey(obj["metadata"]),
            token_size=obj["token_size"],
            price=obj["price"],
            bump=obj["bump"],
            created_at=obj["created_at"],
        )
