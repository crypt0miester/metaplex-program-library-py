from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class UpdateMetadataAccountArgs(typing.TypedDict):
    update_metadata_account_args: types.update_metadata_account_args.UpdateMetadataAccountArgs


layout = borsh.CStruct(
    "update_metadata_account_args"
    / types.update_metadata_account_args.UpdateMetadataAccountArgs.layout
)


class UpdateMetadataAccountAccounts(typing.TypedDict):
    metadata: PublicKey
    update_authority: PublicKey


def update_metadata_account(
    args: UpdateMetadataAccountArgs, accounts: UpdateMetadataAccountAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["update_authority"], is_signer=True, is_writable=False
        ),
    ]
    identifier = b"\x8d\x0e\x17h\xf7\xc05\xad"
    encoded_args = layout.build(
        {
            "update_metadata_account_args": args[
                "update_metadata_account_args"
            ].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
