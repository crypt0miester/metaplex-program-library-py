from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class CancelBidReceiptAccounts(typing.TypedDict):
    receipt: PublicKey
    system_program: PublicKey
    instruction: PublicKey


def cancel_bid_receipt(accounts: CancelBidReceiptAccounts) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["receipt"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["instruction"], is_signer=False, is_writable=False),
    ]
    identifier = b"\xf6l\x1b\xe5\xdc*\xb0+"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
