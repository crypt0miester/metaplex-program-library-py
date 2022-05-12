from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class WithdrawFromFeeArgs(typing.TypedDict):
    amount: int


layout = borsh.CStruct("amount" / borsh.U64)


class WithdrawFromFeeAccounts(typing.TypedDict):
    authority: PublicKey
    fee_withdrawal_destination: PublicKey
    auction_house_fee_account: PublicKey
    auction_house: PublicKey
    system_program: PublicKey


def withdraw_from_fee(
    args: WithdrawFromFeeArgs, accounts: WithdrawFromFeeAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["authority"], is_signer=True, is_writable=False),
        AccountMeta(
            pubkey=accounts["fee_withdrawal_destination"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["auction_house_fee_account"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["auction_house"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
    ]
    identifier = b"\xb3\xd0\xbe\x9a \xb3\x13;"
    encoded_args = layout.build(
        {
            "amount": args["amount"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
