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


class EditionJSON(typing.TypedDict):
    key: types.key.KeyJSON
    parent: str
    edition: int


@dataclass
class Edition:
    discriminator: typing.ClassVar = b"\xeau\xf9J\x07c\xeb\xa7"
    layout: typing.ClassVar = borsh.CStruct(
        "key" / types.key.layout, "parent" / BorshPubkey, "edition" / borsh.U64
    )
    key: types.key.KeyKind
    parent: PublicKey
    edition: int

    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: PublicKey,
        commitment: typing.Optional[Commitment] = None,
    ) -> typing.Optional["Edition"]:
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
    ) -> typing.List[typing.Optional["Edition"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["Edition"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != PROGRAM_ID:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "Edition":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = Edition.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(
            key=types.key.from_decoded(dec.key),
            parent=dec.parent,
            edition=dec.edition,
        )

    def to_json(self) -> EditionJSON:
        return {
            "key": self.key.to_json(),
            "parent": str(self.parent),
            "edition": self.edition,
        }

    @classmethod
    def from_json(cls, obj: EditionJSON) -> "Edition":
        return cls(
            key=types.key.from_json(obj["key"]),
            parent=PublicKey(obj["parent"]),
            edition=obj["edition"],
        )
