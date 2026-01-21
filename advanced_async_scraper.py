import asyncio
import aiohttp
import time

class AsyncDataAggregator:
    def __init__(self, urls):
        self.urls = urls
        self.results = []

    async def fetch_url(self, session, url):
        try:
            async with session.get(url, timeout=5) as response:
                print(f"Fetching: {url}")
                return await response.text()
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

    async def process_all(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_url(session, url) for url in self.urls]
            self.results = await asyncio.gather(*tasks)

    def run(self):
        start_time = time.time()
        asyncio.run(self.process_all())
        duration = time.time() - start_time
        print(f"Processed {len(self.urls)} URLs in {duration:.2f} seconds.")

if __name__ == "__main__":
    targets = [
        "https://www.google.com",
        "https://www.python.org",
        "https://www.github.com"
    ]
    aggregator = AsyncDataAggregator(targets)
    aggregator.run()
