from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class VerifyCollectionAccounts(typing.TypedDict):
    metadata: PublicKey
    collection_authority: PublicKey
    payer: PublicKey
    collection_mint: PublicKey
    collection: PublicKey
    collection_master_edition_account: PublicKey


def verify_collection(accounts: VerifyCollectionAccounts) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["collection_authority"], is_signer=True, is_writable=True
        ),
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=True),
        AccountMeta(
            pubkey=accounts["collection_mint"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["collection"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["collection_master_edition_account"],
            is_signer=False,
            is_writable=False,
        ),
    ]
    identifier = b"8qe\xfdO7z\xa9"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
