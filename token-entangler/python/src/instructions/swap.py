from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class SwapAccounts(typing.TypedDict):
    treasury_mint: PublicKey
    payer: PublicKey
    payment_account: PublicKey
    payment_transfer_authority: PublicKey
    token: PublicKey
    token_mint: PublicKey
    replacement_token_metadata: PublicKey
    replacement_token_mint: PublicKey
    replacement_token: PublicKey
    transfer_authority: PublicKey
    token_a_escrow: PublicKey
    token_b_escrow: PublicKey
    entangled_pair: PublicKey
    token_program: PublicKey
    system_program: PublicKey
    ata_program: PublicKey
    rent: PublicKey


def swap(accounts: SwapAccounts) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["treasury_mint"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=False),
        AccountMeta(
            pubkey=accounts["payment_account"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["payment_transfer_authority"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(pubkey=accounts["token"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["token_mint"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["replacement_token_metadata"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["replacement_token_mint"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["replacement_token"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["transfer_authority"], is_signer=True, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["token_a_escrow"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["token_b_escrow"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["entangled_pair"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["ata_program"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    identifier = b"\xf8\xc6\x9e\x91\xe1u\x87\xc8"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
