from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class SetAndVerifyCollectionAccounts(typing.TypedDict):
    metadata: PublicKey
    collection_authority: PublicKey
    payer: PublicKey
    update_authority: PublicKey
    collection_mint: PublicKey
    collection: PublicKey
    collection_master_edition_account: PublicKey
    collection_authority_record: PublicKey


def set_and_verify_collection(
    accounts: SetAndVerifyCollectionAccounts,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["collection_authority"], is_signer=True, is_writable=True
        ),
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=True),
        AccountMeta(
            pubkey=accounts["update_authority"], is_signer=False, is_writable=False
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
    identifier = b"\xeb\xf2y\xd8\x9e\xea\xb4\xea"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
