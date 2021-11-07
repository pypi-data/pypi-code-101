from biolib.typing_utils import TypedDict, Dict, List, Literal

UuidStr = str
DiskPath = str


class LargeFileSystemCache(TypedDict):
    active_jobs: List[UuidStr]
    last_used: str
    size_bytes: int
    state: Literal['downloading', 'ready']
    storage_partition_uuid: UuidStr
    uuid: UuidStr


class StoragePartition(TypedDict):
    allocated_size_bytes: int
    path: str
    total_size_bytes: int
    uuid: UuidStr


class CacheStateDict(TypedDict):
    storage_partitions: Dict[UuidStr, StoragePartition]
    large_file_systems: Dict[UuidStr, LargeFileSystemCache]
