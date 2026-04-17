"""
Tests for the admin aggregator endpoint.

The default conformance server is started without an aggregator controller,
so this module verifies the baseline 503 Service Unavailable behavior.

Happy-path tests (with a controller wired in) live with the implementation
tests in `tests/lean_spec/subspecs/api/`.
"""

from __future__ import annotations

import httpx


def test_status_returns_503_without_controller(server_url: str) -> None:
    """GET returns 503 when the controller is not wired."""
    response = httpx.get(f"{server_url}/lean/v0/admin/aggregator")
    assert response.status_code == 503


def test_toggle_returns_503_without_controller(server_url: str) -> None:
    """POST returns 503 when the controller is not wired."""
    response = httpx.post(
        f"{server_url}/lean/v0/admin/aggregator",
        json={"enabled": True},
    )
    assert response.status_code == 503


def test_unsupported_method_returns_405(server_url: str) -> None:
    """DELETE against the admin aggregator route is not allowed."""
    response = httpx.delete(f"{server_url}/lean/v0/admin/aggregator")
    assert response.status_code == 405
