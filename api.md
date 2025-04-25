# Assets

Types:

```python
from photos.types import AssetResponse, AssetDeleteResponse
```

Methods:

- <code title="post /api/assets">client.assets.<a href="./src/photos/resources/assets.py">create</a>(\*\*<a href="src/photos/types/asset_create_params.py">params</a>) -> <a href="./src/photos/types/asset_response.py">AssetResponse</a></code>
- <code title="get /api/assets/{asset_id}">client.assets.<a href="./src/photos/resources/assets.py">retrieve</a>(asset_id) -> <a href="./src/photos/types/asset_response.py">AssetResponse</a></code>
- <code title="get /api/assets">client.assets.<a href="./src/photos/resources/assets.py">list</a>(\*\*<a href="src/photos/types/asset_list_params.py">params</a>) -> <a href="./src/photos/types/asset_response.py">SyncCursorPage[AssetResponse]</a></code>
- <code title="delete /api/assets/{asset_id}">client.assets.<a href="./src/photos/resources/assets.py">delete</a>(asset_id) -> <a href="./src/photos/types/asset_delete_response.py">object</a></code>
- <code title="get /api/assets/{asset_id}/download">client.assets.<a href="./src/photos/resources/assets.py">download</a>(asset_id) -> None</code>
- <code title="get /api/assets/{asset_id}/thumbnail">client.assets.<a href="./src/photos/resources/assets.py">download_thumbnail</a>(asset_id, \*\*<a href="src/photos/types/asset_download_thumbnail_params.py">params</a>) -> None</code>

# Albums

Types:

```python
from photos.types import AlbumResponse, AlbumDeleteResponse
```

Methods:

- <code title="post /api/albums">client.albums.<a href="./src/photos/resources/albums/albums.py">create</a>(\*\*<a href="src/photos/types/album_create_params.py">params</a>) -> <a href="./src/photos/types/album_response.py">AlbumResponse</a></code>
- <code title="get /api/albums/{album_id}">client.albums.<a href="./src/photos/resources/albums/albums.py">retrieve</a>(album_id) -> <a href="./src/photos/types/album_response.py">AlbumResponse</a></code>
- <code title="patch /api/albums/{album_id}">client.albums.<a href="./src/photos/resources/albums/albums.py">update</a>(album_id, \*\*<a href="src/photos/types/album_update_params.py">params</a>) -> <a href="./src/photos/types/album_response.py">AlbumResponse</a></code>
- <code title="get /api/albums">client.albums.<a href="./src/photos/resources/albums/albums.py">list</a>(\*\*<a href="src/photos/types/album_list_params.py">params</a>) -> <a href="./src/photos/types/album_response.py">SyncCursorPage[AlbumResponse]</a></code>
- <code title="delete /api/albums/{album_id}">client.albums.<a href="./src/photos/resources/albums/albums.py">delete</a>(album_id) -> <a href="./src/photos/types/album_delete_response.py">object</a></code>

## Assets

Types:

```python
from photos.types.albums import (
    AlbumAssetAssociation,
    AssetListResponse,
    AssetAddResponse,
    AssetRemoveResponse,
)
```

Methods:

- <code title="get /api/albums/{album_id}/assets">client.albums.assets.<a href="./src/photos/resources/albums/assets.py">list</a>(album_id) -> <a href="./src/photos/types/albums/asset_list_response.py">AssetListResponse</a></code>
- <code title="post /api/albums/{album_id}/assets">client.albums.assets.<a href="./src/photos/resources/albums/assets.py">add</a>(album_id, \*\*<a href="src/photos/types/albums/asset_add_params.py">params</a>) -> <a href="./src/photos/types/albums/asset_add_response.py">object</a></code>
- <code title="delete /api/albums/{album_id}/assets">client.albums.assets.<a href="./src/photos/resources/albums/assets.py">remove</a>(album_id, \*\*<a href="src/photos/types/albums/asset_remove_params.py">params</a>) -> <a href="./src/photos/types/albums/asset_remove_response.py">object</a></code>
