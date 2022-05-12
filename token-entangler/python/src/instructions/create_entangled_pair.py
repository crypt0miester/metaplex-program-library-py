from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class CreateEntangledPairArgs(typing.TypedDict):
    bump: int
    reverse_bump: int
    token_a_escrow_bump: int
    token_b_escrow_bump: int
    price: int
    pays_every_time: bool


layout = borsh.CStruct(
    "bump" / borsh.U8,
    "reverse_bump" / borsh.U8,
    "token_a_escrow_bump" / borsh.U8,
    "token_b_escrow_bump" / borsh.U8,
    "price" / borsh.U64,
    "pays_every_time" / borsh.Bool,
)


class CreateEntangledPairAccounts(typing.TypedDict):
    treasury_mint: PublicKey
    payer: PublicKey
    transfer_authority: PublicKey
    authority: PublicKey
    mint_a: PublicKey
    metadata_a: PublicKey
    edition_a: PublicKey
    mint_b: PublicKey
    metadata_b: PublicKey
    edition_b: PublicKey
    token_b: PublicKey
    token_a_escrow: PublicKey
    token_b_escrow: PublicKey
    entangled_pair: PublicKey
    reverse_entangled_pair: PublicKey
    token_program: PublicKey
    system_program: PublicKey
    rent: PublicKey


def create_entangled_pair(
    args: CreateEntangledPairArgs, accounts: CreateEntangledPairAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["treasury_mint"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=True),
        AccountMeta(
            pubkey=accounts["transfer_authority"], is_signer=True, is_writable=False
        ),
        AccountMeta(pubkey=accounts["authority"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["mint_a"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["metadata_a"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["edition_a"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["mint_b"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["metadata_b"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["edition_b"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["token_b"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["token_a_escrow"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["token_b_escrow"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["entangled_pair"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["reverse_entangled_pair"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    identifier = b"\xa6j -\x9c\xd2\xd1\xf0"
    encoded_args = layout.build(
        {
            "bump": args["bump"],
            "reverse_bump": args["reverse_bump"],
            "token_a_escrow_bump": args["token_a_escrow_bump"],
            "token_b_escrow_bump": args["token_b_escrow_bump"],
            "price": args["price"],
            "pays_every_time": args["pays_every_time"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
