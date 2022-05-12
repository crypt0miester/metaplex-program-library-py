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


class CandyMachineJSON(typing.TypedDict):
    authority: str
    wallet: str
    token_mint: typing.Optional[str]
    items_redeemed: int
    data: types.candy_machine_data.CandyMachineDataJSON


@dataclass
class CandyMachine:
    discriminator: typing.ClassVar = b"3\xad\xb1q\x19\xf1m\xbd"
    layout: typing.ClassVar = borsh.CStruct(
        "authority" / BorshPubkey,
        "wallet" / BorshPubkey,
        "token_mint" / borsh.Option(BorshPubkey),
        "items_redeemed" / borsh.U64,
        "data" / types.candy_machine_data.CandyMachineData.layout,
    )
    authority: PublicKey
    wallet: PublicKey
    token_mint: typing.Optional[PublicKey]
    items_redeemed: int
    data: types.candy_machine_data.CandyMachineData

    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: PublicKey,
        commitment: typing.Optional[Commitment] = None,
    ) -> typing.Optional["CandyMachine"]:
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
    ) -> typing.List[typing.Optional["CandyMachine"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["CandyMachine"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != PROGRAM_ID:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "CandyMachine":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = CandyMachine.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(
            authority=dec.authority,
            wallet=dec.wallet,
            token_mint=dec.token_mint,
            items_redeemed=dec.items_redeemed,
            data=types.candy_machine_data.CandyMachineData.from_decoded(dec.data),
        )

    def to_json(self) -> CandyMachineJSON:
        return {
            "authority": str(self.authority),
            "wallet": str(self.wallet),
            "token_mint": (None if self.token_mint is None else str(self.token_mint)),
            "items_redeemed": self.items_redeemed,
            "data": self.data.to_json(),
        }

    @classmethod
    def from_json(cls, obj: CandyMachineJSON) -> "CandyMachine":
        return cls(
            authority=PublicKey(obj["authority"]),
            wallet=PublicKey(obj["wallet"]),
            token_mint=(
                None if obj["token_mint"] is None else PublicKey(obj["token_mint"])
            ),
            items_redeemed=obj["items_redeemed"],
            data=types.candy_machine_data.CandyMachineData.from_json(obj["data"]),
        )
