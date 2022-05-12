from src.accounts.candy_machine import CandyMachine
import asyncio
from solana.rpc.async_api import AsyncClient
from solana.publickey import PublicKey
from src.program_id import PROGRAM_ID as CANDY_MACHINE_ID

async def fetch_candy_machine(cm_address):
    client = AsyncClient("https://api.mainnet-beta.solana.com")
    res = await client.is_connected()

    cm_address = PublicKey(cm_address)
    candy_data = await CandyMachine.fetch(client, cm_address)
    print(candy_data)
    await client.close()

cm_address = "<candy machine address>"
asyncio.run(fetch_candy_machine(cm_address))


