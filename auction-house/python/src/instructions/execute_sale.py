from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class ExecuteSaleArgs(typing.TypedDict):
    escrow_payment_bump: int
    free_trade_state_bump: int
    program_as_signer_bump: int
    buyer_price: int
    token_size: int


layout = borsh.CStruct(
    "escrow_payment_bump" / borsh.U8,
    "free_trade_state_bump" / borsh.U8,
    "program_as_signer_bump" / borsh.U8,
    "buyer_price" / borsh.U64,
    "token_size" / borsh.U64,
)


class ExecuteSaleAccounts(typing.TypedDict):
    buyer: PublicKey
    seller: PublicKey
    token_account: PublicKey
    token_mint: PublicKey
    metadata: PublicKey
    treasury_mint: PublicKey
    escrow_payment_account: PublicKey
    seller_payment_receipt_account: PublicKey
    buyer_receipt_token_account: PublicKey
    authority: PublicKey
    auction_house: PublicKey
    auction_house_fee_account: PublicKey
    auction_house_treasury: PublicKey
    buyer_trade_state: PublicKey
    seller_trade_state: PublicKey
    free_trade_state: PublicKey
    token_program: PublicKey
    system_program: PublicKey
    ata_program: PublicKey
    program_as_signer: PublicKey
    rent: PublicKey


def execute_sale(
    args: ExecuteSaleArgs, accounts: ExecuteSaleAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["buyer"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["seller"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["token_account"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["token_mint"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["treasury_mint"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["escrow_payment_account"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["seller_payment_receipt_account"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["buyer_receipt_token_account"],
            is_signer=False,
            is_writable=True,
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
            pubkey=accounts["auction_house_treasury"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["buyer_trade_state"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["seller_trade_state"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["free_trade_state"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["ata_program"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["program_as_signer"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    identifier = b"%J\xd9\x9dO1#\x06"
    encoded_args = layout.build(
        {
            "escrow_payment_bump": args["escrow_payment_bump"],
            "free_trade_state_bump": args["free_trade_state_bump"],
            "program_as_signer_bump": args["program_as_signer_bump"],
            "buyer_price": args["buyer_price"],
            "token_size": args["token_size"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
