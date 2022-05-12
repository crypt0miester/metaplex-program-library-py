from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class DeprecatedSetReservationListArgs(typing.TypedDict):
    set_reservation_list_args: types.set_reservation_list_args.SetReservationListArgs


layout = borsh.CStruct(
    "set_reservation_list_args"
    / types.set_reservation_list_args.SetReservationListArgs.layout
)


class DeprecatedSetReservationListAccounts(typing.TypedDict):
    master_edition: PublicKey
    reservation_list: PublicKey
    resource: PublicKey


def deprecated_set_reservation_list(
    args: DeprecatedSetReservationListArgs,
    accounts: DeprecatedSetReservationListAccounts,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["master_edition"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["reservation_list"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["resource"], is_signer=True, is_writable=False),
    ]
    identifier = b"D\x1cB\x13;\xcb\xbe\x8e"
    encoded_args = layout.build(
        {
            "set_reservation_list_args": args[
                "set_reservation_list_args"
            ].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
