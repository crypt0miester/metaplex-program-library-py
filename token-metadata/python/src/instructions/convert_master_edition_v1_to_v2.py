from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class ConvertMasterEditionV1ToV2Accounts(typing.TypedDict):
    master_edition: PublicKey
    one_time_auth: PublicKey
    printing_mint: PublicKey


def convert_master_edition_v1_to_v2(
    accounts: ConvertMasterEditionV1ToV2Accounts,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["master_edition"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["one_time_auth"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["printing_mint"], is_signer=False, is_writable=True
        ),
    ]
    identifier = b"\xd9\x1al\x007~\xa7\xee"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
