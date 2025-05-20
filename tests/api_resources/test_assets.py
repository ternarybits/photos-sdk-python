# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from photos import Photos, AsyncPhotos
from tests.utils import assert_matches_type
from photos.types import AssetResponse
from photos._utils import parse_datetime
from photos.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Photos) -> None:
        asset = client.assets.create(
            asset_data=b"raw file contents",
            device_asset_id="device_asset_id",
            device_id="device_id",
            file_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Photos) -> None:
        response = client.assets.with_raw_response.create(
            asset_data=b"raw file contents",
            device_asset_id="device_asset_id",
            device_id="device_id",
            file_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetResponse, asset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Photos) -> None:
        with client.assets.with_streaming_response.create(
            asset_data=b"raw file contents",
            device_asset_id="device_asset_id",
            device_id="device_id",
            file_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Photos) -> None:
        asset = client.assets.retrieve(
            "asset_id",
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Photos) -> None:
        response = client.assets.with_raw_response.retrieve(
            "asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetResponse, asset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Photos) -> None:
        with client.assets.with_streaming_response.retrieve(
            "asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Photos) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Photos) -> None:
        asset = client.assets.list()
        assert_matches_type(SyncCursorPage[AssetResponse], asset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Photos) -> None:
        asset = client.assets.list(
            album_id="album_id",
            limit=1,
            person_id="person_id",
            starting_after_id="starting_after_id",
        )
        assert_matches_type(SyncCursorPage[AssetResponse], asset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Photos) -> None:
        response = client.assets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(SyncCursorPage[AssetResponse], asset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Photos) -> None:
        with client.assets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(SyncCursorPage[AssetResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Photos) -> None:
        asset = client.assets.delete(
            "asset_id",
        )
        assert asset is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Photos) -> None:
        response = client.assets.with_raw_response.delete(
            "asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert asset is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Photos) -> None:
        with client.assets.with_streaming_response.delete(
            "asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Photos) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.with_raw_response.delete(
                "",
            )


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncPhotos) -> None:
        asset = await async_client.assets.create(
            asset_data=b"raw file contents",
            device_asset_id="device_asset_id",
            device_id="device_id",
            file_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPhotos) -> None:
        response = await async_client.assets.with_raw_response.create(
            asset_data=b"raw file contents",
            device_asset_id="device_asset_id",
            device_id="device_id",
            file_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetResponse, asset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPhotos) -> None:
        async with async_client.assets.with_streaming_response.create(
            asset_data=b"raw file contents",
            device_asset_id="device_asset_id",
            device_id="device_id",
            file_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPhotos) -> None:
        asset = await async_client.assets.retrieve(
            "asset_id",
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPhotos) -> None:
        response = await async_client.assets.with_raw_response.retrieve(
            "asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetResponse, asset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPhotos) -> None:
        async with async_client.assets.with_streaming_response.retrieve(
            "asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPhotos) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPhotos) -> None:
        asset = await async_client.assets.list()
        assert_matches_type(AsyncCursorPage[AssetResponse], asset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPhotos) -> None:
        asset = await async_client.assets.list(
            album_id="album_id",
            limit=1,
            person_id="person_id",
            starting_after_id="starting_after_id",
        )
        assert_matches_type(AsyncCursorPage[AssetResponse], asset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPhotos) -> None:
        response = await async_client.assets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AsyncCursorPage[AssetResponse], asset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPhotos) -> None:
        async with async_client.assets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AsyncCursorPage[AssetResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPhotos) -> None:
        asset = await async_client.assets.delete(
            "asset_id",
        )
        assert asset is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPhotos) -> None:
        response = await async_client.assets.with_raw_response.delete(
            "asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert asset is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPhotos) -> None:
        async with async_client.assets.with_streaming_response.delete(
            "asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPhotos) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.with_raw_response.delete(
                "",
            )
