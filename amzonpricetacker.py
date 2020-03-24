import requests 
from bs4 import BeautifulSoup
def extract_url(url):

    if url.find("www.amazon.in") != -1:
        index = url.find("/dp/")
        if index != -1:
            index2 = index + 14
            url = "https://www.amazon.in" + url[index:index2]
        else:
            index = url.find("/gp/")
            if index != -1:
                index2 = index + 22
                url = "https://www.amazon.in" + url[index:index2]
            else:
                url = None
    else:
        url = None
    return url
def get_converted_price(price):

    stripped_price = price.strip("₹ ,")
    replaced_price = stripped_price.replace(",", "")
    find_dot = replaced_price.find(".")
    to_convert_price = replaced_price[0:find_dot]
    converted_price = int(to_convert_price)
    return converted_price
def get_converted_price(price):
    stripped_price = price.strip("₹ ,")
    replaced_price = stripped_price.replace(",", "")
    find_dot = replaced_price.find(".")
    to_convert_price = replaced_price[0:find_dot]
    converted_price = int(to_convert_price)

    return converted_price
#details = {"name": "", "price": 0, "deal": True, "url": ""}
#headers = { "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
def get_product_details(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    details = {"name": "", "price": 0, "deal": True, "url": ""}
    _url = extract_url(url)
    if _url == "":
        details = None
    else:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html5lib")
        title = soup.find(id="productTitle")
        price = soup.find(id="priceblock_dealprice")
        if price is None:
            price = soup.find(id="priceblock_ourprice")
            details["deal"] = False
        if title is not None and price is not None:
            details["name"] = title.get_text().strip()
            details["price"] = get_converted_price(price.get_text())
            details["url"] = _url
        else:
            return None
    return details
print(get_product_details("https://www.amazon.in/gp/product/B07HGJKDQL/ref=s9_acss_bw_cg_Offers_3b1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-6&pf_rd_r=F76S7N09HAP4VRAKTMKS&pf_rd_t=101&pf_rd_p=b8fceb3c-ae25-4b7f-b220-89c0c01ea563&pf_rd_i=1389401031"))
