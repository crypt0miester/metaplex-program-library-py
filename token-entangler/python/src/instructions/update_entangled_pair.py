from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class UpdateEntangledPairArgs(typing.TypedDict):
    price: int
    pays_every_time: bool


layout = borsh.CStruct("price" / borsh.U64, "pays_every_time" / borsh.Bool)


class UpdateEntangledPairAccounts(typing.TypedDict):
    authority: PublicKey
    new_authority: PublicKey
    entangled_pair: PublicKey


def update_entangled_pair(
    args: UpdateEntangledPairArgs, accounts: UpdateEntangledPairAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["authority"], is_signer=True, is_writable=False),
        AccountMeta(
            pubkey=accounts["new_authority"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["entangled_pair"], is_signer=False, is_writable=True
        ),
    ]
    identifier = b")a\xf7\xdab\xa2K\xf4"
    encoded_args = layout.build(
        {
            "price": args["price"],
            "pays_every_time": args["pays_every_time"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
