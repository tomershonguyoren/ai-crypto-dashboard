def test_submit_onboarding_preferences(client, test_user_token):
    response = client.post(
        "/onboarding",
        headers=test_user_token,
        json={
            "target_assets": "BTC, ETH",
            "investor_persona": "HODLer",
            "content_preference": "Market News"
        }
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["target_assets"] == "BTC, ETH"
    assert data["investor_persona"] == "HODLer"
    assert data["content_preference"] == "Market News"
    assert "id" in data

def test_submit_feedback(client, test_user_token):
    response = client.post(
        "/feedback",
        headers=test_user_token,
        json={
            "widget_type": "ai_insight",
            "is_positive": True,
            "interaction_context": "Found this very helpful regarding ETH buildup."
        }
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["widget_type"] == "ai_insight"
    assert data["is_positive"] is True
    assert data["interaction_context"] == "Found this very helpful regarding ETH buildup."
    assert "id" in data
