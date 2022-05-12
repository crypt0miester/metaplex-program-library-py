from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class SetCollectionAccounts(typing.TypedDict):
    candy_machine: PublicKey
    authority: PublicKey
    collection_pda: PublicKey
    payer: PublicKey
    system_program: PublicKey
    rent: PublicKey
    metadata: PublicKey
    mint: PublicKey
    edition: PublicKey
    collection_authority_record: PublicKey
    token_metadata_program: PublicKey


def set_collection(accounts: SetCollectionAccounts) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["candy_machine"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["authority"], is_signer=True, is_writable=False),
        AccountMeta(
            pubkey=accounts["collection_pda"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=False),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["mint"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["edition"], is_signer=False, is_writable=False),
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
    identifier = b"\xc0\xfe\xceL\xa8\xb6;\xdf"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
