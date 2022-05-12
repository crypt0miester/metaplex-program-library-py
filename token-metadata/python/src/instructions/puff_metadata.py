from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class PuffMetadataAccounts(typing.TypedDict):
    metadata: PublicKey


def puff_metadata(accounts: PuffMetadataAccounts) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=True)
    ]
    identifier = b"W\xd9\x15\x84i\xeeGr"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
