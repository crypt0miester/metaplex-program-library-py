from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class DeprecatedMintPrintingTokensArgs(typing.TypedDict):
    mint_printing_tokens_via_token_args: types.mint_printing_tokens_via_token_args.MintPrintingTokensViaTokenArgs


layout = borsh.CStruct(
    "mint_printing_tokens_via_token_args"
    / types.mint_printing_tokens_via_token_args.MintPrintingTokensViaTokenArgs.layout
)


class DeprecatedMintPrintingTokensAccounts(typing.TypedDict):
    destination: PublicKey
    printing_mint: PublicKey
    update_authority: PublicKey
    metadata: PublicKey
    master_edition: PublicKey
    token_program: PublicKey
    rent: PublicKey


def deprecated_mint_printing_tokens(
    args: DeprecatedMintPrintingTokensArgs,
    accounts: DeprecatedMintPrintingTokensAccounts,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["destination"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["printing_mint"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["update_authority"], is_signer=True, is_writable=False
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
    identifier = b"\xc2k\x90\t~\x8f5y"
    encoded_args = layout.build(
        {
            "mint_printing_tokens_via_token_args": args[
                "mint_printing_tokens_via_token_args"
            ].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
