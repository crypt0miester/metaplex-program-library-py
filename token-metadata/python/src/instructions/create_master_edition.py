from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class CreateMasterEditionArgs(typing.TypedDict):
    create_master_edition_args: types.create_master_edition_args.CreateMasterEditionArgs


layout = borsh.CStruct(
    "create_master_edition_args"
    / types.create_master_edition_args.CreateMasterEditionArgs.layout
)


class CreateMasterEditionAccounts(typing.TypedDict):
    edition: PublicKey
    mint: PublicKey
    update_authority: PublicKey
    mint_authority: PublicKey
    payer: PublicKey
    metadata: PublicKey
    token_program: PublicKey
    system_program: PublicKey
    rent: PublicKey


def create_master_edition(
    args: CreateMasterEditionArgs, accounts: CreateMasterEditionAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["edition"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["mint"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["update_authority"], is_signer=True, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["mint_authority"], is_signer=True, is_writable=False
        ),
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=True),
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    identifier = b"\xb3\xd2``9\x19OE"
    encoded_args = layout.build(
        {
            "create_master_edition_args": args[
                "create_master_edition_args"
            ].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
