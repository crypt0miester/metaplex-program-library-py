from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class UpdatePrimarySaleHappenedViaTokenAccounts(typing.TypedDict):
    metadata: PublicKey
    owner: PublicKey
    token: PublicKey


def update_primary_sale_happened_via_token(
    accounts: UpdatePrimarySaleHappenedViaTokenAccounts,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["owner"], is_signer=True, is_writable=False),
        AccountMeta(pubkey=accounts["token"], is_signer=False, is_writable=False),
    ]
    identifier = b"\xac\x81\xad\xd2\xde\x81\xf3b"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
