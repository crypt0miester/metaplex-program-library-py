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


class CollectionPDAJSON(typing.TypedDict):
    mint: str
    candy_machine: str


@dataclass
class CollectionPDA:
    discriminator: typing.ClassVar = b"2\xb7\x7fg\x04\xd5\\5"
    layout: typing.ClassVar = borsh.CStruct(
        "mint" / BorshPubkey, "candy_machine" / BorshPubkey
    )
    mint: PublicKey
    candy_machine: PublicKey

    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: PublicKey,
        commitment: typing.Optional[Commitment] = None,
    ) -> typing.Optional["CollectionPDA"]:
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
    ) -> typing.List[typing.Optional["CollectionPDA"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["CollectionPDA"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != PROGRAM_ID:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "CollectionPDA":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = CollectionPDA.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(
            mint=dec.mint,
            candy_machine=dec.candy_machine,
        )

    def to_json(self) -> CollectionPDAJSON:
        return {
            "mint": str(self.mint),
            "candy_machine": str(self.candy_machine),
        }

    @classmethod
    def from_json(cls, obj: CollectionPDAJSON) -> "CollectionPDA":
        return cls(
            mint=PublicKey(obj["mint"]),
            candy_machine=PublicKey(obj["candy_machine"]),
        )
