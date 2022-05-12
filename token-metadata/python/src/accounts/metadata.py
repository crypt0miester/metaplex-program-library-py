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
from .. import types


class MetadataJSON(typing.TypedDict):
    key: types.key.KeyJSON
    update_authority: str
    mint: str
    data: types.data.DataJSON
    primary_sale_happened: bool
    is_mut: bool
    edition_nonce: typing.Optional[int]
    token_standard: typing.Optional[types.token_standard.TokenStandardJSON]
    collection: typing.Optional[types.collection.CollectionJSON]
    uses: typing.Optional[types.uses.UsesJSON]


@dataclass
class Metadata:
    discriminator: typing.ClassVar = b"H\x0by\x1ao\xb5U]"
    layout: typing.ClassVar = borsh.CStruct(
        "key" / types.key.layout,
        "update_authority" / BorshPubkey,
        "mint" / BorshPubkey,
        "data" / types.data.Data.layout,
        "primary_sale_happened" / borsh.Bool,
        "is_mut" / borsh.Bool,
        "edition_nonce" / borsh.Option(borsh.U8),
        "token_standard" / borsh.Option(types.token_standard.layout),
        "collection" / borsh.Option(types.collection.Collection.layout),
        "uses" / borsh.Option(types.uses.Uses.layout),
    )
    key: types.key.KeyKind
    update_authority: PublicKey
    mint: PublicKey
    data: types.data.Data
    primary_sale_happened: bool
    is_mut: bool
    edition_nonce: typing.Optional[int]
    token_standard: typing.Optional[types.token_standard.TokenStandardKind]
    collection: typing.Optional[types.collection.Collection]
    uses: typing.Optional[types.uses.Uses]

    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: PublicKey,
        commitment: typing.Optional[Commitment] = None,
    ) -> typing.Optional["Metadata"]:
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
    ) -> typing.List[typing.Optional["Metadata"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["Metadata"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != PROGRAM_ID:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "Metadata":
        # if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
        #     raise AccountInvalidDiscriminator(
        #         "The discriminator for this account is invalid"
        #     )
        dec = Metadata.layout.parse(data)
        return cls(
            key=types.key.from_decoded(dec.key),
            update_authority=dec.update_authority,
            mint=dec.mint,
            data=types.data.Data.from_decoded(dec.data),
            primary_sale_happened=dec.primary_sale_happened,
            is_mut=dec.is_mut,
            edition_nonce=dec.edition_nonce,
            token_standard=(
                None
                if dec.token_standard is None
                else types.token_standard.from_decoded(dec.token_standard)
            ),
            collection=(
                None
                if dec.collection is None
                else types.collection.Collection.from_decoded(dec.collection)
            ),
            uses=(None if dec.uses is None else types.uses.Uses.from_decoded(dec.uses)),
        )

    def to_json(self) -> MetadataJSON:
        return {
            "key": self.key.to_json(),
            "update_authority": str(self.update_authority),
            "mint": str(self.mint),
            "data": self.data.to_json(),
            "primary_sale_happened": self.primary_sale_happened,
            "is_mut": self.is_mut,
            "edition_nonce": self.edition_nonce,
            "token_standard": (
                None if self.token_standard is None else self.token_standard.to_json()
            ),
            "collection": (
                None if self.collection is None else self.collection.to_json()
            ),
            "uses": (None if self.uses is None else self.uses.to_json()),
        }

    @classmethod
    def from_json(cls, obj: MetadataJSON) -> "Metadata":
        return cls(
            key=types.key.from_json(obj["key"]),
            update_authority=PublicKey(obj["update_authority"]),
            mint=PublicKey(obj["mint"]),
            data=types.data.Data.from_json(obj["data"]),
            primary_sale_happened=obj["primary_sale_happened"],
            is_mut=obj["is_mut"],
            edition_nonce=obj["edition_nonce"],
            token_standard=(
                None
                if obj["token_standard"] is None
                else types.token_standard.from_json(obj["token_standard"])
            ),
            collection=(
                None
                if obj["collection"] is None
                else types.collection.Collection.from_json(obj["collection"])
            ),
            uses=(
                None if obj["uses"] is None else types.uses.Uses.from_json(obj["uses"])
            ),
        )
