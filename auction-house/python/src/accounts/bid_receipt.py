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


class BidReceiptJSON(typing.TypedDict):
    trade_state: str
    bookkeeper: str
    auction_house: str
    buyer: str
    metadata: str
    token_account: typing.Optional[str]
    purchase_receipt: typing.Optional[str]
    price: int
    token_size: int
    bump: int
    trade_state_bump: int
    created_at: int
    canceled_at: typing.Optional[int]


@dataclass
class BidReceipt:
    discriminator: typing.ClassVar = b"\xba\x96\x8d\x87;z'c"
    layout: typing.ClassVar = borsh.CStruct(
        "trade_state" / BorshPubkey,
        "bookkeeper" / BorshPubkey,
        "auction_house" / BorshPubkey,
        "buyer" / BorshPubkey,
        "metadata" / BorshPubkey,
        "token_account" / borsh.Option(BorshPubkey),
        "purchase_receipt" / borsh.Option(BorshPubkey),
        "price" / borsh.U64,
        "token_size" / borsh.U64,
        "bump" / borsh.U8,
        "trade_state_bump" / borsh.U8,
        "created_at" / borsh.I64,
        "canceled_at" / borsh.Option(borsh.I64),
    )
    trade_state: PublicKey
    bookkeeper: PublicKey
    auction_house: PublicKey
    buyer: PublicKey
    metadata: PublicKey
    token_account: typing.Optional[PublicKey]
    purchase_receipt: typing.Optional[PublicKey]
    price: int
    token_size: int
    bump: int
    trade_state_bump: int
    created_at: int
    canceled_at: typing.Optional[int]

    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: PublicKey,
        commitment: typing.Optional[Commitment] = None,
    ) -> typing.Optional["BidReceipt"]:
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
    ) -> typing.List[typing.Optional["BidReceipt"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["BidReceipt"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != PROGRAM_ID:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "BidReceipt":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = BidReceipt.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(
            trade_state=dec.trade_state,
            bookkeeper=dec.bookkeeper,
            auction_house=dec.auction_house,
            buyer=dec.buyer,
            metadata=dec.metadata,
            token_account=dec.token_account,
            purchase_receipt=dec.purchase_receipt,
            price=dec.price,
            token_size=dec.token_size,
            bump=dec.bump,
            trade_state_bump=dec.trade_state_bump,
            created_at=dec.created_at,
            canceled_at=dec.canceled_at,
        )

    def to_json(self) -> BidReceiptJSON:
        return {
            "trade_state": str(self.trade_state),
            "bookkeeper": str(self.bookkeeper),
            "auction_house": str(self.auction_house),
            "buyer": str(self.buyer),
            "metadata": str(self.metadata),
            "token_account": (
                None if self.token_account is None else str(self.token_account)
            ),
            "purchase_receipt": (
                None if self.purchase_receipt is None else str(self.purchase_receipt)
            ),
            "price": self.price,
            "token_size": self.token_size,
            "bump": self.bump,
            "trade_state_bump": self.trade_state_bump,
            "created_at": self.created_at,
            "canceled_at": self.canceled_at,
        }

    @classmethod
    def from_json(cls, obj: BidReceiptJSON) -> "BidReceipt":
        return cls(
            trade_state=PublicKey(obj["trade_state"]),
            bookkeeper=PublicKey(obj["bookkeeper"]),
            auction_house=PublicKey(obj["auction_house"]),
            buyer=PublicKey(obj["buyer"]),
            metadata=PublicKey(obj["metadata"]),
            token_account=(
                None
                if obj["token_account"] is None
                else PublicKey(obj["token_account"])
            ),
            purchase_receipt=(
                None
                if obj["purchase_receipt"] is None
                else PublicKey(obj["purchase_receipt"])
            ),
            price=obj["price"],
            token_size=obj["token_size"],
            bump=obj["bump"],
            trade_state_bump=obj["trade_state_bump"],
            created_at=obj["created_at"],
            canceled_at=obj["canceled_at"],
        )
