from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from construct import Construct
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class AddConfigLinesArgs(typing.TypedDict):
    index: int
    config_lines: list[types.config_line.ConfigLine]


layout = borsh.CStruct(
    "index" / borsh.U32,
    "config_lines"
    / borsh.Vec(typing.cast(Construct, types.config_line.ConfigLine.layout)),
)


class AddConfigLinesAccounts(typing.TypedDict):
    candy_machine: PublicKey
    authority: PublicKey


def add_config_lines(
    args: AddConfigLinesArgs, accounts: AddConfigLinesAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["candy_machine"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["authority"], is_signer=True, is_writable=False),
    ]
    identifier = b"\xdf2\xe0\xe3\x97\x08sj"
    encoded_args = layout.build(
        {
            "index": args["index"],
            "config_lines": list(
                map(lambda item: item.to_encodable(), args["config_lines"])
            ),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
