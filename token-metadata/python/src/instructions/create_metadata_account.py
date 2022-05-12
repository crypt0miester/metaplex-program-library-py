from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class CreateMetadataAccountArgs(typing.TypedDict):
    create_metadata_account_args: types.create_metadata_account_args.CreateMetadataAccountArgs


layout = borsh.CStruct(
    "create_metadata_account_args"
    / types.create_metadata_account_args.CreateMetadataAccountArgs.layout
)


class CreateMetadataAccountAccounts(typing.TypedDict):
    metadata: PublicKey
    mint: PublicKey
    mint_authority: PublicKey
    payer: PublicKey
    update_authority: PublicKey
    system_program: PublicKey
    rent: PublicKey


def create_metadata_account(
    args: CreateMetadataAccountArgs, accounts: CreateMetadataAccountAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["mint"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["mint_authority"], is_signer=True, is_writable=False
        ),
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=True),
        AccountMeta(
            pubkey=accounts["update_authority"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    identifier = b"KI-\xb2\xd4\xc2\x7fq"
    encoded_args = layout.build(
        {
            "create_metadata_account_args": args[
                "create_metadata_account_args"
            ].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
