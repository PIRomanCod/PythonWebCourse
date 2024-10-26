"""
exchanger.py

Console utility that retrieves the cash exchange rates for EUR and USD from the Public API of PrivatBank.

Using command-line parameters:

-d 5  - Retrieve currency rates for a specified number of days, up to the last 10 days.
-add PLN  - Retrieve the exchange rate for an additional currency.

Example Usage:
- py exchanger.py
- py exchanger.py -d 8 -add PLN
"""

import argparse
import asyncio
import logging
import platform
from datetime import datetime, date
from typing import Dict, Any, List, Optional

import aiohttp

parser = argparse.ArgumentParser(description='App get exchange rate NBU')
parser.add_argument('-d', '--days', default=1, help="How much days")
parser.add_argument('-add', '--add_currency', default=None)
args = vars(parser.parse_args())
days = args.get('days')
user_currency = args.get('add_currency')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def create_urls(value: int) -> list:
    """
    Generate a list of URLs for API requests based on the number of days.

    :param value: Number of days.
    :return: List of URLs for requests.
    """
    url_prefix = 'https://api.privatbank.ua/p24api/exchange_rates?json&date='
    current_datetime = datetime.today().date()
    users_input = int(value)
    if users_input > 10:
        users_input = 10
    urls = []
    for i in range(users_input):
        new_date = date(year=current_datetime.year, month=current_datetime.month, day=current_datetime.day - i)
        urls.append(url_prefix + new_date.strftime("%d.%m.%Y"))
    return urls[::-1]


async def request(url) -> Dict[str, Any] | None:
    """
    Make an asynchronous HTTP request using aiohttp and return the decoded JSON.

    :param url: URL for the request.
    :return: Decoded JSON or None in case of an error.
    """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    r = await response.json()
                    return r
                logging.error(f"Error status {response.status} for {url}")
        except aiohttp.ClientConnectorError as e:
            logging.error(f"Connection error {url}: {e}")
            return None


def output(all_currencies: List[Dict[str, Any]], additional_currency: Optional[str] = None) -> str:
    """
    Generate a formatted string with currency information.

    :param all_currencies: List of JSON objects with currency information.
    :param additional_currency: Optional currency added by the user.
    :return: String with currency information.
    """
    default_currencies = ["USD", "EUR"]
    answer = ""
    if additional_currency:
        default_currencies.append(additional_currency)
    for item in all_currencies:
        answer += item['date'] + '\n'
        for currencies in item['exchangeRate']:
            if currencies['currency'] in default_currencies:
                answer += f"\t\t{currencies.get('currency')} buy : {currencies.get('saleRate')} sale: {currencies.get('purchaseRate')}\n"
    return answer


async def exchanger_run(days: int = 1, additional_currency: Optional[str] = None) -> str:
    """
    Perform a group of asynchronous HTTP requests and format the output result.

    :param days: Number of days to get the exchange rate.
    :param additional_currency: Optional currency added by the user.
    :return: String with exchange rate information.
    """
    urls = create_urls(days)
    r = []
    for url in urls:
        r.append(request(url))

    result = await asyncio.gather(*r)
    return output(result, additional_currency)


if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    res = asyncio.run(exchanger_run(days, user_currency))
    print(res)
