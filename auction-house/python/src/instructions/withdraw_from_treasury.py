from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class WithdrawFromTreasuryArgs(typing.TypedDict):
    amount: int


layout = borsh.CStruct("amount" / borsh.U64)


class WithdrawFromTreasuryAccounts(typing.TypedDict):
    treasury_mint: PublicKey
    authority: PublicKey
    treasury_withdrawal_destination: PublicKey
    auction_house_treasury: PublicKey
    auction_house: PublicKey
    token_program: PublicKey
    system_program: PublicKey


def withdraw_from_treasury(
    args: WithdrawFromTreasuryArgs, accounts: WithdrawFromTreasuryAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["treasury_mint"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["authority"], is_signer=True, is_writable=False),
        AccountMeta(
            pubkey=accounts["treasury_withdrawal_destination"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["auction_house_treasury"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["auction_house"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
    ]
    identifier = b"\x00\xa4VL8H\x0c\xaa"
    encoded_args = layout.build(
        {
            "amount": args["amount"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
