import finnhub

def scrape_news():
    finnhub_client = finnhub.Client(api_key="cpsgv11r01qkode1ftj0cpsgv11r01qkode1ftjg")

    news = finnhub_client.general_news('general', min_id=0)

    return news
