from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class SellArgs(typing.TypedDict):
    trade_state_bump: int
    free_trade_state_bump: int
    program_as_signer_bump: int
    buyer_price: int
    token_size: int


layout = borsh.CStruct(
    "trade_state_bump" / borsh.U8,
    "free_trade_state_bump" / borsh.U8,
    "program_as_signer_bump" / borsh.U8,
    "buyer_price" / borsh.U64,
    "token_size" / borsh.U64,
)


class SellAccounts(typing.TypedDict):
    wallet: PublicKey
    token_account: PublicKey
    metadata: PublicKey
    authority: PublicKey
    auction_house: PublicKey
    auction_house_fee_account: PublicKey
    seller_trade_state: PublicKey
    free_seller_trade_state: PublicKey
    token_program: PublicKey
    system_program: PublicKey
    program_as_signer: PublicKey
    rent: PublicKey


def sell(args: SellArgs, accounts: SellAccounts) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["wallet"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["token_account"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=False),
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
            pubkey=accounts["seller_trade_state"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["free_seller_trade_state"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["program_as_signer"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    identifier = b"3\xe6\x85\xa4\x01\x7f\x83\xad"
    encoded_args = layout.build(
        {
            "trade_state_bump": args["trade_state_bump"],
            "free_trade_state_bump": args["free_trade_state_bump"],
            "program_as_signer_bump": args["program_as_signer_bump"],
            "buyer_price": args["buyer_price"],
            "token_size": args["token_size"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
