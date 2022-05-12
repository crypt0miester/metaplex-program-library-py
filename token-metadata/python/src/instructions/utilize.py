from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class UtilizeArgs(typing.TypedDict):
    utilize_args: types.utilize_args.UtilizeArgs


layout = borsh.CStruct("utilize_args" / types.utilize_args.UtilizeArgs.layout)


class UtilizeAccounts(typing.TypedDict):
    metadata: PublicKey
    token_account: PublicKey
    mint: PublicKey
    use_authority: PublicKey
    owner: PublicKey
    token_program: PublicKey
    ata_program: PublicKey
    system_program: PublicKey
    rent: PublicKey
    use_authority_record: PublicKey
    burner: PublicKey


def utilize(args: UtilizeArgs, accounts: UtilizeAccounts) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["token_account"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["mint"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["use_authority"], is_signer=True, is_writable=True),
        AccountMeta(pubkey=accounts["owner"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["ata_program"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["use_authority_record"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["burner"], is_signer=False, is_writable=False),
    ]
    identifier = b"h\x92\xf2\xd1\xb0\xae\xb9\xa3"
    encoded_args = layout.build(
        {
            "utilize_args": args["utilize_args"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
