from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class SetCollectionDuringMintAccounts(typing.TypedDict):
    candy_machine: PublicKey
    metadata: PublicKey
    payer: PublicKey
    collection_pda: PublicKey
    token_metadata_program: PublicKey
    instructions: PublicKey
    collection_mint: PublicKey
    collection_metadata: PublicKey
    collection_master_edition: PublicKey
    authority: PublicKey
    collection_authority_record: PublicKey


def set_collection_during_mint(
    accounts: SetCollectionDuringMintAccounts,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["candy_machine"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=False),
        AccountMeta(
            pubkey=accounts["collection_pda"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["token_metadata_program"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["instructions"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["collection_mint"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["collection_metadata"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["collection_master_edition"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(pubkey=accounts["authority"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["collection_authority_record"],
            is_signer=False,
            is_writable=False,
        ),
    ]
    identifier = b"g\x11\xc8\x19v_}="
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
