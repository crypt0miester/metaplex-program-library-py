from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class WithdrawFundsAccounts(typing.TypedDict):
    candy_machine: PublicKey
    authority: PublicKey


def withdraw_funds(accounts: WithdrawFundsAccounts) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["candy_machine"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["authority"], is_signer=True, is_writable=False),
    ]
    identifier = b"\xf1$\x1do\xd0\x1fh\xd9"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
