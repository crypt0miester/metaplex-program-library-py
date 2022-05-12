from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class PrintPurchaseReceiptArgs(typing.TypedDict):
    purchase_receipt_bump: int


layout = borsh.CStruct("purchase_receipt_bump" / borsh.U8)


class PrintPurchaseReceiptAccounts(typing.TypedDict):
    purchase_receipt: PublicKey
    listing_receipt: PublicKey
    bid_receipt: PublicKey
    bookkeeper: PublicKey
    system_program: PublicKey
    rent: PublicKey
    instruction: PublicKey


def print_purchase_receipt(
    args: PrintPurchaseReceiptArgs, accounts: PrintPurchaseReceiptAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["purchase_receipt"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["listing_receipt"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["bid_receipt"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["bookkeeper"], is_signer=True, is_writable=True),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["instruction"], is_signer=False, is_writable=False),
    ]
    identifier = b"\xe3\x9a\xfb\x07\xb48d\x8f"
    encoded_args = layout.build(
        {
            "purchase_receipt_bump": args["purchase_receipt_bump"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
