import os
import httpx
from typing import List, Dict, Any

async def fetch_coin_prices() -> Dict[str, Any]:
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=10.0)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching coin prices: {e}")
            return {
                "bitcoin": {"usd": 0, "usd_24h_change": 0}, 
                "ethereum": {"usd": 0, "usd_24h_change": 0}, 
                "solana": {"usd": 0, "usd_24h_change": 0}
            }

async def fetch_market_news() -> List[Dict[str, Any]]:
    # Mocking cryptopanic call. If actual token is invalid, it will fail and hit the fallback
    url = "https://cryptopanic.com/api/v1/posts/?auth_token=mock_token_replace_me&public=true"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=5.0)
            response.raise_for_status()
            return response.json().get("results", [])
        except Exception as e:
            print(f"CryptoPanic API failed, using fallback mock data. Error: {e}")
            return [
                {"id": 101, "title": "Bitcoin surges as market analysts predict new ATH", "url": "https://www.coindesk.com/"},
                {"id": 102, "title": "Ethereum upgrades show promising scalability improvements", "url": "https://cointelegraph.com/"},
                {"id": 103, "title": "Top 10 DeFi projects to watch this quarter", "url": "https://decrypt.co/"}
            ]

async def generate_ai_insight(user_preferences: Any) -> str:
    # Check if preferences exist, otherwise default values
    assets = user_preferences.target_assets if user_preferences else "Crypto assets"
    persona = user_preferences.investor_persona if user_preferences else "investor"
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    api_key = os.getenv("OPENROUTER_API_KEY", "sk-or-v1-mock-key")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    system_prompt = """You are a professional yet engaging crypto financial advisor. Your task is to provide a highly tailored daily market insight based on the user's specific investor persona and the crypto assets they are tracking. 

Strict Instructions:
1. You must respond with EXACTLY two concise, punchy sentences.
2. Do NOT include any conversational filler, greetings, or prefixes (e.g., do not say "Here is your insight," or "As a Day Trader..."). 
3. Output ONLY the raw insight text.
4. NEVER apologize for lacking real-time data or state that your knowledge cutoff is in the past."""

    payload = {
        "model": "google/gemini-2.5-flash",
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"Investor Persona: {persona}\nTarget Assets: {assets}\n\nProvide my daily insight."
            }
        ]
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=payload, timeout=10.0)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"OpenRouter API failed, using fallback insight. Error: {e}")
            return f"Based on your profile as a '{persona}' tracking '{assets}', the current market indicators suggest strong accumulation. Keep an eye on macro-economic shifts later this week."

async def get_daily_meme() -> str:
    # Returning a static crypto meme URL
    return "https://i.imgflip.com/1g8my4.jpg"
