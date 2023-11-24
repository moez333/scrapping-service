import pytest
import httpx

base_url = "http://172.18.0.1"

@pytest.mark.asyncio
async def test_scrape_and_save_to_db():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{base_url}/scrape")

        assert response.status_code == 200

        assert "data" in response.json()
        assert "message" in response.json()
        
        data = response.json()["data"]
        assert "id" in data
        assert "name" in data
        assert "posts" in data

        message = response.json()["message"]
        assert "Scraped data saved to the database." in message
