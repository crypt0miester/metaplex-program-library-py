from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class UnverifyCollectionAccounts(typing.TypedDict):
    metadata: PublicKey
    collection_authority: PublicKey
    collection_mint: PublicKey
    collection: PublicKey
    collection_master_edition_account: PublicKey
    collection_authority_record: PublicKey


def unverify_collection(accounts: UnverifyCollectionAccounts) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["collection_authority"], is_signer=True, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["collection_mint"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["collection"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["collection_master_edition_account"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["collection_authority_record"],
            is_signer=False,
            is_writable=False,
        ),
    ]
    identifier = b"\xfa\xfb*j)\x89\xba\xa8"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
