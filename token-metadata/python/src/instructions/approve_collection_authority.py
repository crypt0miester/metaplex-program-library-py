from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class ApproveCollectionAuthorityAccounts(typing.TypedDict):
    collection_authority_record: PublicKey
    new_collection_authority: PublicKey
    update_authority: PublicKey
    payer: PublicKey
    metadata: PublicKey
    mint: PublicKey
    system_program: PublicKey
    rent: PublicKey


def approve_collection_authority(
    accounts: ApproveCollectionAuthorityAccounts,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["collection_authority_record"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["new_collection_authority"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["update_authority"], is_signer=True, is_writable=True
        ),
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=True),
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["mint"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    identifier = b"\xfe\x88\xd0'AB\x1bo"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
