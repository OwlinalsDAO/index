import asyncio
import art
from owlinals import OwlinalsIndexer

__all__ = [OwlinalsIndexer]
async def get_data(page, semaphore):
    async with semaphore:
        async with OwlinalsIndexer(page) as indexer:
            result_json = await indexer.index_page()
            path = './outputs/'+str(page)+".json"
            with open(path, 'w') as file:
                file.write(result_json)
            print(f'page {page} finished')

def make_art():
    art_text = art.text2art('OWLINALS INDEXER')
    lines = "-" * len(art_text.split('\n')[0])
    print(f"{lines}\n{art_text}{lines}")

async def main():
    make_art()

    semaphore = asyncio.Semaphore(10)
    tasks = [get_data(page, semaphore) for page in range(1, 131)]
    await asyncio.gather(*tasks)
    print(f"Data collected!")


if __name__ == "__main__":
    asyncio.run(main())
