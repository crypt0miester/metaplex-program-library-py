from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class UpdateCandyMachineArgs(typing.TypedDict):
    data: types.candy_machine_data.CandyMachineData


layout = borsh.CStruct("data" / types.candy_machine_data.CandyMachineData.layout)


class UpdateCandyMachineAccounts(typing.TypedDict):
    candy_machine: PublicKey
    authority: PublicKey
    wallet: PublicKey


def update_candy_machine(
    args: UpdateCandyMachineArgs, accounts: UpdateCandyMachineAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["candy_machine"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["authority"], is_signer=True, is_writable=False),
        AccountMeta(pubkey=accounts["wallet"], is_signer=False, is_writable=False),
    ]
    identifier = b"\xf3\xfb|\x9c\xd3\xd3v\xef"
    encoded_args = layout.build(
        {
            "data": args["data"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
