# test_main.py
import pytest
import httpx
from main import app
from httpx import ASGITransport

transport = ASGITransport(app=app)

@pytest.mark.asyncio
async def test_get_all_products():
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/product")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 3

@pytest.mark.asyncio
async def test_get_single_product():
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/product/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Thinkpad"

@pytest.mark.asyncio
async def test_create_product():
    new_product = {
        "id": 3,
        "title": "Dell",
        "desc": "Ram-16 gb SSD"
    }
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/product", json=new_product)
    assert response.status_code == 200
    assert response.json()["status"] == "created"

@pytest.mark.asyncio
async def test_update_product_put():
    updated_product = {
        "id": 3,
        "title": "Dell Updated",
        "desc": "Ram-32 gb SSD"
    }
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.put("/product/3", json=updated_product)
    assert response.status_code == 200
    assert response.json()["status"] == "upadted"

@pytest.mark.asyncio
async def test_update_product_patch():
    partial_update = {
        "title": "Dell Patched",
        "desc": "Ram-64 gb SSD"
    }
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.patch("/product/3", json=partial_update)
    assert response.status_code == 200
    assert response.json()["status"] == "upadted"

@pytest.mark.asyncio
async def test_delete_product():
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.delete("/product/3")
    assert response.status_code == 200
    assert response.text.strip('"') == "datadeleted"


