import sys
from typing import Tuple
import wikipedia
import requests


number_of_requests = int(sys.argv[-1])


with open("template.html") as f:
	template = f.read()


def get_article() -> Tuple[str, str]:
	req = requests.get("https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard")
	article_url = req.url
	print(f"Trying {article_url}")
	article_id = article_url.split("/")[-1]
	return article_url, article_id

def write_article(art_id: str, art_url: str, sentences: str):
	with open(f"output/{art_id}.html", "w") as f:
		f.write(template.format(
			url=art_url,
			data=sentences
		))

wikipedia.set_lang("fr")

while number_of_requests > 0:
	try:
		art_url, art_id = get_article()
		write_article(art_id, art_url, wikipedia.summary(art_id, sentences=3))
		number_of_requests -= 1
	except Exception as e:
		print(e)