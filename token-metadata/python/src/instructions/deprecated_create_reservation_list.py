from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class DeprecatedCreateReservationListAccounts(typing.TypedDict):
    reservation_list: PublicKey
    payer: PublicKey
    update_authority: PublicKey
    master_edition: PublicKey
    resource: PublicKey
    metadata: PublicKey
    system_program: PublicKey
    rent: PublicKey


def deprecated_create_reservation_list(
    accounts: DeprecatedCreateReservationListAccounts,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["reservation_list"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=False),
        AccountMeta(
            pubkey=accounts["update_authority"], is_signer=True, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["master_edition"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["resource"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    identifier = b"\xab\xe3\xa1\x9e\x01\xb0iH"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
