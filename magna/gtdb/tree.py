import os
import shutil
import tempfile

import dendropy

from magna.config import MAGNA_DIR
from magna.io import download_file, md5sum


class _GtdbTree:

    def __init__(self, source: str, path: str, md5: str):
        self.source = source
        self.path = path
        self.md5 = md5
        if not os.path.isfile(self.path):
            self._download()
        self.tree = self._read()

    def _read(self):
        return dendropy.Tree.get(path=self.path, schema='newick', preserve_underscores=True)

    def _download(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Download
            tmp_path = os.path.join(tmpdir, 'tree.tree')
            download_file(self.source, tmp_path)

            # Extract and validate
            if md5sum(tmp_path) != self.md5:
                raise ValueError('MD5 checksum mismatch')

            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            shutil.copyfile(tmp_path, self.path)


class GtdbTreeR95Arc(_GtdbTree):
    source = 'https://data.gtdb.ecogenomic.org/releases/release95/95.0/ar122_r95.tree'
    path = os.path.join(MAGNA_DIR, 'dataset', 'gtdb', 'tree', 'ar122_r95.tree')
    md5 = '2f5e072b9095617e7b5cff09653f8bec'

    def __init__(self):
        super().__init__(self.source, self.path, self.md5)


class GtdbTreeR95Bac(_GtdbTree):
    source = 'https://data.gtdb.ecogenomic.org/releases/release95/95.0/bac120_r95.tree'
    path = os.path.join(MAGNA_DIR, 'dataset', 'gtdb', 'tree', 'bac120_r95.tree')
    md5 = 'c896d0eece01b281e09bd38534cd072e'

    def __init__(self):
        super().__init__(self.source, self.path, self.md5)


class GtdbTreeR202Arc(_GtdbTree):
    source = 'https://data.gtdb.ecogenomic.org/releases/release202/202.0/ar122_r202.tree'
    path = os.path.join(MAGNA_DIR, 'dataset', 'gtdb', 'tree', 'ar122_r202.tree')
    md5 = '5b2dd87b0836fd63a223a556eae2906d'

    def __init__(self):
        super().__init__(self.source, self.path, self.md5)


class GtdbTreeR202Bac(_GtdbTree):
    source = 'https://data.gtdb.ecogenomic.org/releases/release202/202.0/bac120_r202.tree'
    path = os.path.join(MAGNA_DIR, 'dataset', 'gtdb', 'tree', 'bac120_r202.tree')
    md5 = 'aebfc092ff6f2d81ef1226da6f1477c9'

    def __init__(self):
        super().__init__(self.source, self.path, self.md5)
