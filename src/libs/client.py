from urllib.parse import urljoin, urlencode

import httpx


class EStatClient:
    BASE_META = "https://api.e-stat.go.jp/rest/3.0/app/json/"

    def __init__(self, app_id: str):
        self.app_id = app_id

    def build_url(self, path: str) -> str:
        return urljoin(
            self.BASE_META,
            path,
        )

    def get_url(self, stats_data_id: str, **kwargs) -> str:
        params = {
            "appId": self.app_id,
            "statsDataId": stats_data_id,
            **kwargs,
        }
        path = f"getMetaInfo?{urlencode(params)}"
        url = self.build_url(path)
        return url

    def get(self, stats_data_id: str, **kwargs) -> httpx.Response:
        url = self.get_url(stats_data_id, **kwargs)
        res = httpx.get(url)
        return res
