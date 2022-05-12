from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class RemoveCollectionAccounts(typing.TypedDict):
    candy_machine: PublicKey
    authority: PublicKey
    collection_pda: PublicKey
    metadata: PublicKey
    mint: PublicKey
    collection_authority_record: PublicKey
    token_metadata_program: PublicKey


def remove_collection(accounts: RemoveCollectionAccounts) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["candy_machine"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["authority"], is_signer=True, is_writable=False),
        AccountMeta(
            pubkey=accounts["collection_pda"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["mint"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["collection_authority_record"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["token_metadata_program"],
            is_signer=False,
            is_writable=False,
        ),
    ]
    identifier = b"\xdf4j\xd9=\xdc$\xa0"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
