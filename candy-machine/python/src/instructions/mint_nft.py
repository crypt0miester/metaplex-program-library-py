from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class MintNftArgs(typing.TypedDict):
    creator_bump: int


layout = borsh.CStruct("creator_bump" / borsh.U8)


class MintNftAccounts(typing.TypedDict):
    candy_machine: PublicKey
    candy_machine_creator: PublicKey
    payer: PublicKey
    wallet: PublicKey
    metadata: PublicKey
    mint: PublicKey
    mint_authority: PublicKey
    update_authority: PublicKey
    master_edition: PublicKey
    token_metadata_program: PublicKey
    token_program: PublicKey
    system_program: PublicKey
    rent: PublicKey
    clock: PublicKey
    recent_blockhashes: PublicKey
    instruction_sysvar_account: PublicKey


def mint_nft(args: MintNftArgs, accounts: MintNftAccounts) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["candy_machine"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["candy_machine_creator"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=False),
        AccountMeta(pubkey=accounts["wallet"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["mint"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["mint_authority"], is_signer=True, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["update_authority"], is_signer=True, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["master_edition"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["token_metadata_program"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["token_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["system_program"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["clock"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["recent_blockhashes"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["instruction_sysvar_account"],
            is_signer=False,
            is_writable=False,
        ),
    ]
    identifier = b"\xd39\x06\xa7\x0f\xdb#\xfb"
    encoded_args = layout.build(
        {
            "creator_bump": args["creator_bump"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
