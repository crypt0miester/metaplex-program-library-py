from .src.accounts.metadata import Metadata
import asyncio
from solana.rpc.async_api import AsyncClient
from solana.publickey import PublicKey
from .program_id import PROGRAM_ID as METADATA_PROGRAM_ID


def get_metadata_account(mint_key):
    return PublicKey.find_program_address(
        [b'metadata', bytes(METADATA_PROGRAM_ID), bytes(PublicKey(mint_key))],
        METADATA_PROGRAM_ID
    )[0]

async def fetch_metadata(mint_address):
    client = AsyncClient("https://api.mainnet-beta.solana.com")
    res = await client.is_connected()

    token_address = get_metadata_account(mint_address)
    metadata = await Metadata.fetch(client, token_address)
    print(metadata)
    await client.close()

mint_address = "6VxGFK7NTv8tmRS2NvMNGAdqwkN5Q1b4X2qEk71Uf8N2"
asyncio.run(fetch_metadata(mint_address))


