import aiohttp
# need refactor: flowise_api does not support context converstaion, temporarily set it aside

async def flowise_query(api_url: str, prompt: str, session: aiohttp.ClientSession, headers: dict = None) -> str:
    """
    Sends a query to the Flowise API and returns the response.

    Args:
        api_url (str): The URL of the Flowise API.
        prompt (str): The question to ask the API.
        session (aiohttp.ClientSession): The aiohttp session to use.
        headers (dict, optional): The headers to use. Defaults to None.

    Returns:
        str: The response from the API.
    """
    if headers:
        response = await session.post(
            api_url, json={"question": prompt}, headers=headers
        )
    else:
        response = await session.post(api_url, json={"question": prompt})
    return await response.json()

async def test():
    session = aiohttp.ClientSession()
    api_url = "http://127.0.0.1:3000/api/v1/prediction/683f9ea8-e670-4d51-b657-0886eab9cea1"
    prompt = "What is the capital of France?"
    response = await flowise_query(api_url, prompt, session)
    print(response)

if __name__ == "__main__":
    import asyncio

    asyncio.run(test())
