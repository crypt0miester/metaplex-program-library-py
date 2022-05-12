from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class CancelArgs(typing.TypedDict):
    buyer_price: int
    token_size: int


layout = borsh.CStruct("buyer_price" / borsh.U64, "token_size" / borsh.U64)


class CancelAccounts(typing.TypedDict):
    wallet: PublicKey
    token_account: PublicKey
    token_mint: PublicKey
    authority: PublicKey
    auction_house: PublicKey
    auction_house_fee_account: PublicKey
    trade_state: PublicKey
    token_program: PublicKey


def cancel(args: CancelArgs, accounts: CancelAccounts) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["wallet"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["token_account"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["token_mint"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["authority"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["auction_house"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["auction_house_fee_account"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(pubkey=accounts["trade_state"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
    ]
    identifier = b"\xe8\xdb\xdf)\xdb\xec\xdc\xbe"
    encoded_args = layout.build(
        {
            "buyer_price": args["buyer_price"],
            "token_size": args["token_size"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
