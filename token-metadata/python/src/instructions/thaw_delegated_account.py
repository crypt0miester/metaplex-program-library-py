from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class ThawDelegatedAccountAccounts(typing.TypedDict):
    delegate: PublicKey
    token_account: PublicKey
    edition: PublicKey
    mint: PublicKey
    token_program: PublicKey


def thaw_delegated_account(
    accounts: ThawDelegatedAccountAccounts,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["delegate"], is_signer=True, is_writable=True),
        AccountMeta(
            pubkey=accounts["token_account"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["edition"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["mint"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
    ]
    identifier = b'\xef\x98\xe3"\xe1\xc8\xce\xaa'
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
