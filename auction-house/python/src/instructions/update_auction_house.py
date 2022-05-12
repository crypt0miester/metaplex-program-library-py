from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class UpdateAuctionHouseArgs(typing.TypedDict):
    seller_fee_basis_points: typing.Optional[int]
    requires_sign_off: typing.Optional[bool]
    can_change_sale_price: typing.Optional[bool]


layout = borsh.CStruct(
    "seller_fee_basis_points" / borsh.Option(borsh.U16),
    "requires_sign_off" / borsh.Option(borsh.Bool),
    "can_change_sale_price" / borsh.Option(borsh.Bool),
)


class UpdateAuctionHouseAccounts(typing.TypedDict):
    treasury_mint: PublicKey
    payer: PublicKey
    authority: PublicKey
    new_authority: PublicKey
    fee_withdrawal_destination: PublicKey
    treasury_withdrawal_destination: PublicKey
    treasury_withdrawal_destination_owner: PublicKey
    auction_house: PublicKey
    token_program: PublicKey
    system_program: PublicKey
    ata_program: PublicKey
    rent: PublicKey


def update_auction_house(
    args: UpdateAuctionHouseArgs, accounts: UpdateAuctionHouseAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["treasury_mint"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=False),
        AccountMeta(pubkey=accounts["authority"], is_signer=True, is_writable=False),
        AccountMeta(
            pubkey=accounts["new_authority"], is_signer=False, is_writable=False
        ),
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
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["ata_program"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    identifier = b"T\xd7\x02\xac\xf1\x00\xf5\xdb"
    encoded_args = layout.build(
        {
            "seller_fee_basis_points": args["seller_fee_basis_points"],
            "requires_sign_off": args["requires_sign_off"],
            "can_change_sale_price": args["can_change_sale_price"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
