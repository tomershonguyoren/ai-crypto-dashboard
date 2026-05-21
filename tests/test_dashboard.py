import pytest
from unittest.mock import patch, AsyncMock

# Note: The async endpoints use asyncio.gather on async functions so we patch and ensure proper AsyncMocks are wrapped in Python's mock library standards.

@patch("app.routers.dashboard.fetch_coin_prices", new_callable=AsyncMock)
@patch("app.routers.dashboard.fetch_market_news", new_callable=AsyncMock)
@patch("app.routers.dashboard.generate_ai_insight", new_callable=AsyncMock)
@patch("app.routers.dashboard.get_daily_meme", new_callable=AsyncMock)
def test_get_dashboard(
    mock_get_meme, 
    mock_generate_insight, 
    mock_fetch_news, 
    mock_fetch_prices, 
    client, 
    test_user_token
):
    # 1. Provide preferences for user (Dashboard requires them, else 400 Bad Request)
    client.post(
        "/onboarding",
        headers=test_user_token,
        json={
            "target_assets": "BTC",
            "investor_persona": "Day Trader",
            "content_preference": "Charts"
        }
    )
    
    # 2. Setup mock return payloads precisely imitating actual async JSON responses
    mock_fetch_prices.return_value = {"bitcoin": {"usd": 65000, "usd_24h_change": 2.5}}
    mock_fetch_news.return_value = [{"title": "Mock Market News"}]
    mock_generate_insight.return_value = "Mock 2-sentence AI insight simulating OpenRouter payload logic."
    mock_get_meme.return_value = "https://mock.com/meme.jpg"
    
    # 3. Call endpoint (Mocked)
    response = client.get("/dashboard", headers=test_user_token)
    
    # 4. Standard verification
    assert response.status_code == 200
    data = response.json()
    
    # Validate structure and mock implementations
    assert data["prices"] == {"bitcoin": {"usd": 65000, "usd_24h_change": 2.5}}
    assert data["news"] == [{"title": "Mock Market News"}]
    assert data["insight"] == "Mock 2-sentence AI insight simulating OpenRouter payload logic."
    assert data["meme"] == "https://mock.com/meme.jpg"
    
    # Validates data parsing of nested database structures 
    assert data["preferences"]["investor_persona"] == "Day Trader"
    assert data["preferences"]["target_assets"] == "BTC"
