import favicon
from urllib3.exceptions import HTTPError
from urllib.parse import urlparse
from interface.driver.favicon_driver import FaviconDriver
from util.logger import AppLog

_logger = AppLog(__name__)


class FaviconDriverImpl(FaviconDriver):
    def get_favicon(self, url: str) -> str:
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        try:
            icons = favicon.get(base_url)
        except HTTPError as e:
            _logger.warn(f"Can not get Entry Favicon at {base_url} cause by {e}")
            icons = []
        if len(icons) == 0:
            return ""
        else:
            return icons[0].url
