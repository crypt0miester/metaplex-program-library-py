from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class ApproveUseAuthorityArgs(typing.TypedDict):
    approve_use_authority_args: types.approve_use_authority_args.ApproveUseAuthorityArgs


layout = borsh.CStruct(
    "approve_use_authority_args"
    / types.approve_use_authority_args.ApproveUseAuthorityArgs.layout
)


class ApproveUseAuthorityAccounts(typing.TypedDict):
    use_authority_record: PublicKey
    owner: PublicKey
    payer: PublicKey
    user: PublicKey
    owner_token_account: PublicKey
    metadata: PublicKey
    mint: PublicKey
    burner: PublicKey
    token_program: PublicKey
    system_program: PublicKey
    rent: PublicKey


def approve_use_authority(
    args: ApproveUseAuthorityArgs, accounts: ApproveUseAuthorityAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["use_authority_record"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["owner"], is_signer=True, is_writable=True),
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=True),
        AccountMeta(pubkey=accounts["user"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["owner_token_account"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["mint"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["burner"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    identifier = b"\x0e\x04M\x86V\x17%\xec"
    encoded_args = layout.build(
        {
            "approve_use_authority_args": args[
                "approve_use_authority_args"
            ].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
