from __future__ import annotations

import http.server
import socketserver
import subprocess
import threading
from pathlib import Path
from urllib.parse import urljoin

import pytest
from playwright.sync_api import sync_playwright


REPO_ROOT = Path(__file__).resolve().parents[1]
DIST_DIR = REPO_ROOT / "dist"
BASE_URL = "http://127.0.0.1:8000"
EXPECTED_PAGES = [
    ("/", "On Growth and Form"),
    ("/workflow/", "Proposal Workflow"),
    ("/repository-map/", "Repository Map"),
]


@pytest.fixture(scope="session")
def built_site() -> Path:
    subprocess.run(
        [
            "python3",
            "-m",
            "mkdocs",
            "build",
            "--strict",
            "--clean",
            "--site-dir",
            str(DIST_DIR),
        ],
        check=True,
        cwd=REPO_ROOT,
    )
    return DIST_DIR


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args) -> None:
        return


@pytest.fixture(scope="session")
def site_server(built_site: Path) -> str:
    handler = lambda *args, **kwargs: QuietHandler(*args, directory=str(built_site), **kwargs)
    with socketserver.TCPServer(("127.0.0.1", 8000), handler) as httpd:
        thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        thread.start()
        try:
            yield BASE_URL
        finally:
            httpd.shutdown()
            thread.join(timeout=5)


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        try:
            yield browser
        finally:
            browser.close()


def new_page(browser):
    page = browser.new_page()
    console_errors = []
    page_errors = []
    failed_responses = []

    page.on(
        "console",
        lambda msg: console_errors.append(msg.text)
        if msg.type == "error"
        else None,
    )
    page.on("pageerror", lambda err: page_errors.append(str(err)))
    page.on(
        "response",
        lambda response: failed_responses.append(
            f"{response.status} {response.url}"
        )
        if response.status >= 400
        else None,
    )
    return page, console_errors, page_errors, failed_responses


def test_expected_pages_render(site_server: str, browser) -> None:
    page, console_errors, page_errors, failed_responses = new_page(browser)

    for route, heading in EXPECTED_PAGES:
        response = page.goto(urljoin(site_server, route), wait_until="networkidle")
        assert response is not None
        assert response.ok, f"Expected {route} to load successfully"
        assert page.get_by_role("heading", name=heading).is_visible()

    assert not console_errors, f"Browser console errors: {console_errors}"
    assert not page_errors, f"Browser page errors: {page_errors}"
    assert not failed_responses, f"Failed network responses: {failed_responses}"

    page.close()


def test_homepage_internal_links_resolve(site_server: str, browser) -> None:
    page, _, _, _ = new_page(browser)
    page.goto(site_server, wait_until="networkidle")

    hrefs = []
    for href in page.locator("a[href]").evaluate_all(
        "(elements) => elements.map((element) => element.getAttribute('href'))"
    ):
        if href and not href.startswith(("http://", "https://", "mailto:", "#")):
            hrefs.append(href)

    checked_routes = sorted(set(hrefs))
    assert checked_routes, "Expected at least one internal link on the homepage"

    for href in checked_routes:
        response = page.goto(urljoin(site_server, href), wait_until="networkidle")
        assert response is not None
        assert response.ok, f"Internal link failed: {href}"

    page.close()
