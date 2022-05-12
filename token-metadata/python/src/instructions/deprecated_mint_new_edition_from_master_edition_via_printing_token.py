from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class DeprecatedMintNewEditionFromMasterEditionViaPrintingTokenAccounts(
    typing.TypedDict
):
    metadata: PublicKey
    edition: PublicKey
    master_edition: PublicKey
    mint: PublicKey
    mint_authority: PublicKey
    printing_mint: PublicKey
    master_token_account: PublicKey
    edition_marker: PublicKey
    burn_authority: PublicKey
    payer: PublicKey
    master_update_authority: PublicKey
    master_metadata: PublicKey
    token_program: PublicKey
    system_program: PublicKey
    rent: PublicKey
    reservation_list: PublicKey


def deprecated_mint_new_edition_from_master_edition_via_printing_token(
    accounts: DeprecatedMintNewEditionFromMasterEditionViaPrintingTokenAccounts,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["edition"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["master_edition"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["mint"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["mint_authority"], is_signer=True, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["printing_mint"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["master_token_account"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["edition_marker"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["burn_authority"], is_signer=True, is_writable=False
        ),
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=False),
        AccountMeta(
            pubkey=accounts["master_update_authority"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["master_metadata"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["reservation_list"], is_signer=False, is_writable=True
        ),
    ]
    identifier = b"\x9a$\xaeo\xbeP\x9b\xe4"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
