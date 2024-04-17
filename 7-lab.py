import asyncio
from utils import read_from_file
from web_utils import fetch_from_web
from data_processing import process_data
from comp_module import compose


async def main():
    file_path = 'D:/stp.txt'
    web_url = 'http://127.0.0.1:5000'

    file_line = compose(process_data, read_from_file)
    web_line = compose(process_data, fetch_from_web)

    file_result = await file_line(file_path)

    web_result = await web_line(web_url)

    print("File result:", file_result)
    print("Web result:", web_result)

asyncio.run(main())
