from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class DeprecatedCreateMasterEditionArgs(typing.TypedDict):
    create_master_edition_args: types.create_master_edition_args.CreateMasterEditionArgs


layout = borsh.CStruct(
    "create_master_edition_args"
    / types.create_master_edition_args.CreateMasterEditionArgs.layout
)


class DeprecatedCreateMasterEditionAccounts(typing.TypedDict):
    edition: PublicKey
    mint: PublicKey
    printing_mint: PublicKey
    one_time_printing_authorization_mint: PublicKey
    update_authority: PublicKey
    printing_mint_authority: PublicKey
    mint_authority: PublicKey
    metadata: PublicKey
    payer: PublicKey
    token_program: PublicKey
    system_program: PublicKey
    rent: PublicKey
    one_time_printing_authorization_mint_authority: PublicKey


def deprecated_create_master_edition(
    args: DeprecatedCreateMasterEditionArgs,
    accounts: DeprecatedCreateMasterEditionAccounts,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["edition"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["mint"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["printing_mint"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["one_time_printing_authorization_mint"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["update_authority"], is_signer=True, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["printing_mint_authority"],
            is_signer=True,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["mint_authority"], is_signer=True, is_writable=False
        ),
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=False),
        AccountMeta(
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["one_time_printing_authorization_mint_authority"],
            is_signer=True,
            is_writable=False,
        ),
    ]
    identifier = b"\x9b\x7f\xa5\x9f\xec\\O\x15"
    encoded_args = layout.build(
        {
            "create_master_edition_args": args[
                "create_master_edition_args"
            ].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
