from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from anchorpy.borsh_extension import BorshPubkey
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class UpdateAuthorityArgs(typing.TypedDict):
    new_authority: typing.Optional[PublicKey]


layout = borsh.CStruct("new_authority" / borsh.Option(BorshPubkey))


class UpdateAuthorityAccounts(typing.TypedDict):
    candy_machine: PublicKey
    authority: PublicKey
    wallet: PublicKey


def update_authority(
    args: UpdateAuthorityArgs, accounts: UpdateAuthorityAccounts
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["candy_machine"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=accounts["authority"], is_signer=True, is_writable=False),
        AccountMeta(pubkey=accounts["wallet"], is_signer=False, is_writable=False),
    ]
    identifier = b" .@\x1c\x95K\xf3X"
    encoded_args = layout.build(
        {
            "new_authority": args["new_authority"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
