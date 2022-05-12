from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class DeprecatedMintPrintingTokensViaTokenArgs(typing.TypedDict):
    mint_printing_tokens_via_token_args: types.mint_printing_tokens_via_token_args.MintPrintingTokensViaTokenArgs


layout = borsh.CStruct(
    "mint_printing_tokens_via_token_args"
    / types.mint_printing_tokens_via_token_args.MintPrintingTokensViaTokenArgs.layout
)


class DeprecatedMintPrintingTokensViaTokenAccounts(typing.TypedDict):
    destination: PublicKey
    token: PublicKey
    one_time_printing_authorization_mint: PublicKey
    printing_mint: PublicKey
    burn_authority: PublicKey
    metadata: PublicKey
    master_edition: PublicKey
    token_program: PublicKey
    rent: PublicKey


def deprecated_mint_printing_tokens_via_token(
    args: DeprecatedMintPrintingTokensViaTokenArgs,
    accounts: DeprecatedMintPrintingTokensViaTokenAccounts,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["destination"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["token"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["one_time_printing_authorization_mint"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["printing_mint"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["burn_authority"], is_signer=True, is_writable=False
        ),
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["master_edition"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    identifier = b'T"\x98\x85\x910\x04\xdf'
    encoded_args = layout.build(
        {
            "mint_printing_tokens_via_token_args": args[
                "mint_printing_tokens_via_token_args"
            ].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
