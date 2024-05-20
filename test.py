from arxivscraper import Scraper
import requests
import os

def download_paper(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f'Downloaded {filename}')

def fetch_and_download_papers():
    print("Fetching new papers...")

    # Config Scraper
    scraper = Scraper(category='cond-mat.mtrl-sci', date_from='2022-05-01', date_until='2022-05-07', filters={'categories': ['cond-mat.mtrl-sci']})
    output = scraper.scrape()

    # Create directory for papers
    if not os.path.exists('papers'):
        os.makedirs('papers')

    for paper in output:
        paper_id = paper['id'].split('/')[-1]
        pdf_url = f'http://arxiv.org/pdf/{paper_id}.pdf'
        download_paper(pdf_url, f'papers/{paper_id}.pdf')

fetch_and_download_papers()