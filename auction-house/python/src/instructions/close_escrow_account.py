from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class CloseEscrowAccountArgs(typing.TypedDict):
    escrow_payment_bump: int


layout = borsh.CStruct("escrow_payment_bump" / borsh.U8)


class CloseEscrowAccountAccounts(typing.TypedDict):
    wallet: PublicKey
    escrow_payment_account: PublicKey
    auction_house: PublicKey
    system_program: PublicKey


def close_escrow_account(
    args: CloseEscrowAccountArgs, accounts: CloseEscrowAccountAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["wallet"], is_signer=True, is_writable=False),
        AccountMeta(
            pubkey=accounts["escrow_payment_account"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["auction_house"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
    ]
    identifier = b"\xd1*\xd0\xb3\x8cN\x12+"
    encoded_args = layout.build(
        {
            "escrow_payment_bump": args["escrow_payment_bump"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
