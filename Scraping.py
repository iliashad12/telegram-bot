import requests
from bs4 import BeautifulSoup

def translate_number(num):
    translation = str.maketrans("۰۱۲۳۴۵۶۷۸۹","0123456789")
    new_number = num.translate(translation)
    # Delete تومان
    new_price = new_number.replace(",", "").replace(" تومان", "")
    return new_price


# NEW name
def collect_prices (price_number, search_result=10) :
    prices = []
    count = 0
    for i in price_number :
        if count == search_result :
            break
        try:
            final_price = int(translate_number(i.text))
            if final_price > 1000 :
                prices.append(final_price)
                count += 1
        except ValueError:
            continue
    return prices


def get_average_price (user_input):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    params = {
        "q": user_input
    }
    url = "https://divar.ir/s/iran"
    response = requests.get(url, headers=headers, params=params)
    response.encoding = 'utf-8'
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    price = soup.find_all(class_='kt-post-card__description')
    price_list = collect_prices(price)
    try:
        return int(sum(price_list) / len(price_list))
    except ZeroDivisionError:
        return None
