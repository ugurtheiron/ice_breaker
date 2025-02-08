from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str):
    """Searches for Linkedin or twitter Profile Page."""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res

from firecrawl import FirecrawlApp
from pydantic import BaseModel, Field

app = FirecrawlApp(api_key="fc-1b4e643d426a4834b5b7a1a0e78330be")

class EcommerceProdoctSchema(BaseModel):
    product_name: str
    product_catagory: str
    barcode_code: str
    seller_name: str
    stock: str



# List of product URLs
urls = [
    "https://www.propointsports.com/urun/k-swiss-speed-trac-41-5",
    "https://www.decathlon.com.tr/p/yetiskin-tenis-raketi-270-g-tr160-lite/_/R-p-171345?mc=8489539"
    # "https://www.decathlon.com.tr/p/erkek-su-gecirmez-outdoor-kar-montu-kislik-mont-siyah-mavi-sh500-10-degc/_/R-p-331992?mc=8641931&c=S%C4%B0YAH_KAHVERENG%C4%B0",
    # "https://www.trendyol.com/telvesse/pro-futbol-topu-maestro-sampiyonlar-ligi-pompali-sert-zemin-hali-saha-futbol-topu-no-5-mavi-p-710911514?boutiqueId=61&merchantId=130527",
    # "https://www.trendyol.com/sng-ayakkabi/siyah-cilt-kadin-bot-p-211939375?boutiqueId=61&merchantId=126486&sav=true",
    # "https://www.dovuskralligi.com/cleto-reyes-traditional-training-boks-eldiveni/?srsltid=AfmBOoruvSzVrCtln7r0CT4xJyQmFPcGElYtNqE0xESXWfhuCn9sqwKiTZI"
]

# Loop over all URLs and scrape data
for url in urls:
    try:
        data = app.scrape_url(url, {
            'formats': ['json'],
            'jsonOptions': {
                'schema': EcommerceProdoctSchema.model_json_schema(),
            }
        })
        print("--------------------")
        print(data["json"])
    except Exception as e:
        print(f"Error processing URL {url}: {e}")


