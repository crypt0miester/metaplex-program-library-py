from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class CancelListingReceiptAccounts(typing.TypedDict):
    receipt: PublicKey
    system_program: PublicKey
    instruction: PublicKey


def cancel_listing_receipt(
    accounts: CancelListingReceiptAccounts,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["receipt"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["instruction"], is_signer=False, is_writable=False),
    ]
    identifier = b"\xab;\x8a~\xf6\xbd[\x0b"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
