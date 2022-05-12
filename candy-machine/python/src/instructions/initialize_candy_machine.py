from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class InitializeCandyMachineArgs(typing.TypedDict):
    data: types.candy_machine_data.CandyMachineData


layout = borsh.CStruct("data" / types.candy_machine_data.CandyMachineData.layout)


class InitializeCandyMachineAccounts(typing.TypedDict):
    candy_machine: PublicKey
    wallet: PublicKey
    authority: PublicKey
    payer: PublicKey
    system_program: PublicKey
    rent: PublicKey


def initialize_candy_machine(
    args: InitializeCandyMachineArgs, accounts: InitializeCandyMachineAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["candy_machine"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["wallet"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["authority"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=False),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    identifier = b"\x8e\x89\xa7k/'\xf0|"
    encoded_args = layout.build(
        {
            "data": args["data"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
