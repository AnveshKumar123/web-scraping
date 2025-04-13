import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://docs.crawl4ai.com/api/async-webcrawler/",
        )
        with open("crawl_result.md", "w", encoding="utf-8") as f:
            f.write(result.markdown)
        print("✅ Result saved to crawl_result.md")
        
if __name__ == "__main__":
    asyncio.run(main())