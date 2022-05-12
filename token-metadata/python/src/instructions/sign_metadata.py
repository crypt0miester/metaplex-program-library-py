from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class SignMetadataAccounts(typing.TypedDict):
    metadata: PublicKey
    creator: PublicKey


def sign_metadata(accounts: SignMetadataAccounts) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["creator"], is_signer=True, is_writable=False),
    ]
    identifier = b"\xb2\xf5\xfd\xcd\xec\xfa\xe9\xd1"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
