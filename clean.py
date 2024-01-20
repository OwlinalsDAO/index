import asyncio
import aiofiles
import json
import csv
from pathlib import Path
import pandas as pd

whole_list = []

async def process_json_file(file_path):
    async with aiofiles.open(file_path, 'r') as file:
        content = await file.read()
        try:
            j = json.loads(content)
            owlinal_list = j['data']['list']
            print(owlinal_list)
            # Check if the data is in the expected format
            if isinstance(owlinal_list, list):
                for item in owlinal_list:
                    unwanted_fields = [
                        "sat_block_time", "sat_ordinal", "sat_rarity", "sat_block",
                        "satributes", "metadata", "metaprotocol", "offset",
                        "pointer", "provenance"
                    ]
                    for field in unwanted_fields:
                        item.pop(field, None)
                    for key, value in item.items():
                        if value is None:
                            item[key] = "None"
                        elif value is json.JSONEncoder().encode(None):
                            item[key] = "null"
                whole_list.extend(owlinal_list)
            else:
                print(f"Invalid data format in file: {file_path}")
                return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in file {file_path}: {e}")
            return None

async def process_all_json_files(directory):
    tasks = []
    async for file_path in get_json_files(directory):
        task = asyncio.create_task(process_json_file(file_path))
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    return [result for result in results if result is not None]

async def get_json_files(directory):
    path = Path(directory)
    for file_path in path.iterdir():
        if file_path.suffix.lower() == '.json':
            yield file_path

async def write_to_csv(output_file, data):
    header = [
        "address", "block_hash", "block_height", "block_time", "content_decode",
        "content_length", "content_type", "eth_teleburn_address", "ext", "from_address",
        "genesis_block_hash", "genesis_block_height", "genesis_block_time", "genesis_fee",
        "genesis_tx_id", "id", "location", "number", "tx_id", "tx_index"
    ]

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)

    # Select only the desired columns
    df = df[header]

    # Replace "None" with None and "null" with "null" in the DataFrame
    df.replace("None", None, inplace=True)
    df.replace("null", "null", inplace=True)

    # Write the DataFrame to a CSV file
    df.to_csv(output_file, index=False)

async def main():
    input_directory = "./outputs"
    output_file = "./output.csv"
    global whole_list
    processed_data = await process_all_json_files(input_directory)
    # print(len(whole_list))
    await write_to_csv(output_file, whole_list)

if __name__ == "__main__":
    asyncio.run(main())
