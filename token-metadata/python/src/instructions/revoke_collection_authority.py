from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class RevokeCollectionAuthorityAccounts(typing.TypedDict):
    collection_authority_record: PublicKey
    update_authority: PublicKey
    metadata: PublicKey
    mint: PublicKey


def revoke_collection_authority(
    accounts: RevokeCollectionAuthorityAccounts,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["collection_authority_record"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["update_authority"], is_signer=True, is_writable=True
        ),
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["mint"], is_signer=False, is_writable=False),
    ]
    identifier = b"\x1f\x8b\x87\xc6\x1d0\xa0\x9a"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
