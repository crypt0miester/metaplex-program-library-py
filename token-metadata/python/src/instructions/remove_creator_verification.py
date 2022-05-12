from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class RemoveCreatorVerificationAccounts(typing.TypedDict):
    metadata: PublicKey
    creator: PublicKey


def remove_creator_verification(
    accounts: RemoveCreatorVerificationAccounts,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["creator"], is_signer=True, is_writable=False),
    ]
    identifier = b")\xc2\x8c\xd9Z\xa0\x8b\x06"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
