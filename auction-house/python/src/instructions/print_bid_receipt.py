from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class PrintBidReceiptArgs(typing.TypedDict):
    receipt_bump: int


layout = borsh.CStruct("receipt_bump" / borsh.U8)


class PrintBidReceiptAccounts(typing.TypedDict):
    receipt: PublicKey
    bookkeeper: PublicKey
    system_program: PublicKey
    rent: PublicKey
    instruction: PublicKey


def print_bid_receipt(
    args: PrintBidReceiptArgs, accounts: PrintBidReceiptAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["receipt"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["bookkeeper"], is_signer=True, is_writable=True),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["instruction"], is_signer=False, is_writable=False),
    ]
    identifier = b"^\xf9Z\xe6\xef@D\xda"
    encoded_args = layout.build(
        {
            "receipt_bump": args["receipt_bump"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
