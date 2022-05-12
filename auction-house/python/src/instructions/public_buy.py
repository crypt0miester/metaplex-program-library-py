from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class PublicBuyArgs(typing.TypedDict):
    trade_state_bump: int
    escrow_payment_bump: int
    buyer_price: int
    token_size: int


layout = borsh.CStruct(
    "trade_state_bump" / borsh.U8,
    "escrow_payment_bump" / borsh.U8,
    "buyer_price" / borsh.U64,
    "token_size" / borsh.U64,
)


class PublicBuyAccounts(typing.TypedDict):
    wallet: PublicKey
    payment_account: PublicKey
    transfer_authority: PublicKey
    treasury_mint: PublicKey
    token_account: PublicKey
    metadata: PublicKey
    escrow_payment_account: PublicKey
    authority: PublicKey
    auction_house: PublicKey
    auction_house_fee_account: PublicKey
    buyer_trade_state: PublicKey
    token_program: PublicKey
    system_program: PublicKey
    rent: PublicKey


def public_buy(
    args: PublicBuyArgs, accounts: PublicBuyAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["wallet"], is_signer=True, is_writable=False),
        AccountMeta(
            pubkey=accounts["payment_account"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["transfer_authority"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["treasury_mint"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["token_account"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["escrow_payment_account"], is_signer=False, is_writable=True
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
            pubkey=accounts["buyer_trade_state"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    identifier = b"\xa9T\xda#*\xce\x10\xab"
    encoded_args = layout.build(
        {
            "trade_state_bump": args["trade_state_bump"],
            "escrow_payment_bump": args["escrow_payment_bump"],
            "buyer_price": args["buyer_price"],
            "token_size": args["token_size"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
