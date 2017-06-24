import requests
from bs4 import BeautifulSoup


QUOTE_URL = "https://talaikis.com/api/quotes/random/"
CONVERT_URL = "http://www.text2image.com/pit_t2i/saver"
request_session = requests.Session()


def get_quotes():
	res = requests.request('GET', QUOTE_URL).json()
	string = res['quote'] + '\n' + '\n' + '- ' + res['author']
	return string


def get_antiSpamKey():
	res = request_session.get(CONVERT_URL).text
	soup = BeautifulSoup(res, 'html.parser')
	key = soup.find(id='antiSpamKey')['value']
	return key


def get_payload(quote, antiSpamKey):
	data = {
		"antiSpamKey":antiSpamKey,
		"debugLevel": "",
		"imageBackcolor":"#000000",
		"imageFont":16,
		"imageFontFace":"comic",
		"imageForecolor":"#FFFFFF",
		"imageFormat":0,
		"imageHeight":500,
		"imageText": quote,
		'imageVAlign':"centre",
		"imageWidth":500,
		"lang":"en",
		"saveImage":"",
		"submit":"",
		"userID":""
	}
	return data


def get_headers():
	data = {
		'accept-encoding': "gzip",
		'content-type': "application/x-www-form-urlencoded",
		'cache-control': "no-cache"
	}
	return data


def convert_text_to_img():
	data = get_quotes()
	antiSpamKey = get_antiSpamKey()
	payload = get_payload(data, antiSpamKey)
	headers = get_headers()
	res = request_session.post(CONVERT_URL, data=payload, headers=headers).text
	soup = BeautifulSoup(res, 'html.parser')
	img_url = soup.find('img')['src']
	return img_url
