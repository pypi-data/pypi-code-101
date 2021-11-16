"""FASTGenomics base library"""

__version__ = "3.4.0"

from .fg import (
    FASTGenomicsClient,
    FASTGenomicsLargeFileStorageClient,
    FASTGenomicsDatasetClient,
    ToolConfiguration,
    run_zip,
)

from .FASTGenomicsPlatformUpdater import (
    FASTGenomicsPlatformUpdater
)
