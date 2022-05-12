from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class RevokeUseAuthorityAccounts(typing.TypedDict):
    use_authority_record: PublicKey
    owner: PublicKey
    user: PublicKey
    owner_token_account: PublicKey
    mint: PublicKey
    metadata: PublicKey
    token_program: PublicKey
    system_program: PublicKey
    rent: PublicKey


def revoke_use_authority(
    accounts: RevokeUseAuthorityAccounts,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["use_authority_record"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["owner"], is_signer=True, is_writable=True),
        AccountMeta(pubkey=accounts["user"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["owner_token_account"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["mint"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    identifier = b"\xcc\xc2\xd0\x8d\x8e\xddmT"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
