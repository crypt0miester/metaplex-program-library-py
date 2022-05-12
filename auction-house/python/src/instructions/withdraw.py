from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class WithdrawArgs(typing.TypedDict):
    escrow_payment_bump: int
    amount: int


layout = borsh.CStruct("escrow_payment_bump" / borsh.U8, "amount" / borsh.U64)


class WithdrawAccounts(typing.TypedDict):
    wallet: PublicKey
    receipt_account: PublicKey
    escrow_payment_account: PublicKey
    treasury_mint: PublicKey
    authority: PublicKey
    auction_house: PublicKey
    auction_house_fee_account: PublicKey
    token_program: PublicKey
    system_program: PublicKey
    ata_program: PublicKey
    rent: PublicKey


def withdraw(args: WithdrawArgs, accounts: WithdrawAccounts) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["wallet"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["receipt_account"], is_signer=False, is_writable=True
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
        AccountMeta(pubkey=accounts["ata_program"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    identifier = b'\xb7\x12F\x9c\x94m\xa1"'
    encoded_args = layout.build(
        {
            "escrow_payment_bump": args["escrow_payment_bump"],
            "amount": args["amount"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
