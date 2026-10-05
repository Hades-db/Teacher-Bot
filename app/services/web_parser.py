import aiohttp
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_random_headers() -> dict:
    ua = UserAgent()
    return {"user-agent": ua.random}

async def fetch_education_themes() -> list:
    target_url = "https://code.mu"
    headers = get_random_headers()
    themes_list = []

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(target_url, headers=headers, timeout=15) as response:
                if response.status == 200:
                    html_content = await response.text()
                    
                    soup = BeautifulSoup(html_content, "lxml")
                    main_blocks = soup.find_all("nav")
                    
                    for block in main_blocks:
                        clean_text = block.text.strip()
                        if clean_text:
                            themes_list.append(clean_text)
                            
                    return themes_list
                else:
                    print(f"Web Parser Error: Received status code {response.status}")
                    return []
                    
    except Exception as e:
        print(f"Web Parser Exception: {e}")
        return []