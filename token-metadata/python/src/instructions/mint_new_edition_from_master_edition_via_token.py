from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class MintNewEditionFromMasterEditionViaTokenArgs(typing.TypedDict):
    mint_new_edition_from_master_edition_via_token_args: types.mint_new_edition_from_master_edition_via_token_args.MintNewEditionFromMasterEditionViaTokenArgs


layout = borsh.CStruct(
    "mint_new_edition_from_master_edition_via_token_args"
    / types.mint_new_edition_from_master_edition_via_token_args.MintNewEditionFromMasterEditionViaTokenArgs.layout
)


class MintNewEditionFromMasterEditionViaTokenAccounts(typing.TypedDict):
    new_metadata: PublicKey
    new_edition: PublicKey
    master_edition: PublicKey
    new_mint: PublicKey
    edition_mark_pda: PublicKey
    new_mint_authority: PublicKey
    payer: PublicKey
    token_account_owner: PublicKey
    token_account: PublicKey
    new_metadata_update_authority: PublicKey
    metadata: PublicKey
    token_program: PublicKey
    system_program: PublicKey
    rent: PublicKey


def mint_new_edition_from_master_edition_via_token(
    args: MintNewEditionFromMasterEditionViaTokenArgs,
    accounts: MintNewEditionFromMasterEditionViaTokenAccounts,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["new_metadata"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["new_edition"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["master_edition"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["new_mint"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["edition_mark_pda"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["new_mint_authority"], is_signer=True, is_writable=False
        ),
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=True),
        AccountMeta(
            pubkey=accounts["token_account_owner"], is_signer=True, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["token_account"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["new_metadata_update_authority"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    identifier = b"\xfc\xda\xbf\xa8~E}v"
    encoded_args = layout.build(
        {
            "mint_new_edition_from_master_edition_via_token_args": args[
                "mint_new_edition_from_master_edition_via_token_args"
            ].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
