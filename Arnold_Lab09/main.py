import requests as requests

url_ddg = "https://api.duckduckgo.com"


def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo/UnitedStatesPresidents/list/all/lastname&format=json")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]
