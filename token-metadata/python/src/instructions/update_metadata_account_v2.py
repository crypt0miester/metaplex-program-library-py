from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class UpdateMetadataAccountV2Args(typing.TypedDict):
    update_metadata_account_args_v2: types.update_metadata_account_args_v2.UpdateMetadataAccountArgsV2


layout = borsh.CStruct(
    "update_metadata_account_args_v2"
    / types.update_metadata_account_args_v2.UpdateMetadataAccountArgsV2.layout
)


class UpdateMetadataAccountV2Accounts(typing.TypedDict):
    metadata: PublicKey
    update_authority: PublicKey


def update_metadata_account_v2(
    args: UpdateMetadataAccountV2Args, accounts: UpdateMetadataAccountV2Accounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["update_authority"], is_signer=True, is_writable=False
        ),
    ]
    identifier = b"\xca\x84\x98\xe5\xd8\xd9\x89\xd4"
    encoded_args = layout.build(
        {
            "update_metadata_account_args_v2": args[
                "update_metadata_account_args_v2"
            ].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
