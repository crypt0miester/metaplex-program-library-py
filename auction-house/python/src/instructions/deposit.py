from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class DepositArgs(typing.TypedDict):
    escrow_payment_bump: int
    amount: int


layout = borsh.CStruct("escrow_payment_bump" / borsh.U8, "amount" / borsh.U64)


class DepositAccounts(typing.TypedDict):
    wallet: PublicKey
    payment_account: PublicKey
    transfer_authority: PublicKey
    escrow_payment_account: PublicKey
    treasury_mint: PublicKey
    authority: PublicKey
    auction_house: PublicKey
    auction_house_fee_account: PublicKey
    token_program: PublicKey
    system_program: PublicKey
    rent: PublicKey


def deposit(args: DepositArgs, accounts: DepositAccounts) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["wallet"], is_signer=True, is_writable=False),
        AccountMeta(
            pubkey=accounts["payment_account"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["transfer_authority"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["escrow_payment_account"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["treasury_mint"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["authority"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["auction_house"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["auction_house_fee_account"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    identifier = b"\xf2#\xc6\x89R\xe1\xf2\xb6"
    encoded_args = layout.build(
        {
            "escrow_payment_bump": args["escrow_payment_bump"],
            "amount": args["amount"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
