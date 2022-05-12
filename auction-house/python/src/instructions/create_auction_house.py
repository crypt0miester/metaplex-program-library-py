from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class CreateAuctionHouseArgs(typing.TypedDict):
    bump: int
    fee_payer_bump: int
    treasury_bump: int
    seller_fee_basis_points: int
    requires_sign_off: bool
    can_change_sale_price: bool


layout = borsh.CStruct(
    "bump" / borsh.U8,
    "fee_payer_bump" / borsh.U8,
    "treasury_bump" / borsh.U8,
    "seller_fee_basis_points" / borsh.U16,
    "requires_sign_off" / borsh.Bool,
    "can_change_sale_price" / borsh.Bool,
)


class CreateAuctionHouseAccounts(typing.TypedDict):
    treasury_mint: PublicKey
    payer: PublicKey
    authority: PublicKey
    fee_withdrawal_destination: PublicKey
    treasury_withdrawal_destination: PublicKey
    treasury_withdrawal_destination_owner: PublicKey
    auction_house: PublicKey
    auction_house_fee_account: PublicKey
    auction_house_treasury: PublicKey
    token_program: PublicKey
    system_program: PublicKey
    ata_program: PublicKey
    rent: PublicKey


def create_auction_house(
    args: CreateAuctionHouseArgs, accounts: CreateAuctionHouseAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["treasury_mint"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=True),
        AccountMeta(pubkey=accounts["authority"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["fee_withdrawal_destination"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["treasury_withdrawal_destination"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["treasury_withdrawal_destination_owner"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["auction_house"], is_signer=False, is_writable=True
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
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["ata_program"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    identifier = b"\xddB\xf2\x9f\xf9\xce\x86\xf1"
    encoded_args = layout.build(
        {
            "bump": args["bump"],
            "fee_payer_bump": args["fee_payer_bump"],
            "treasury_bump": args["treasury_bump"],
            "seller_fee_basis_points": args["seller_fee_basis_points"],
            "requires_sign_off": args["requires_sign_off"],
            "can_change_sale_price": args["can_change_sale_price"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
