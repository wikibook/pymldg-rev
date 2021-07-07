#!/usr/bin/env python
import zipfile
import subprocess
from os import remove
from os.path import join as pjoin
from os.path import dirname, abspath

import fire

from swyo.utils import Config


class Download:
    def __init__(self):
        self.root = dirname(abspath(__file__))
        self.config = Config(pjoin(self.root, 'url.yml'), yaml=True)

    def run(self, dataset):
        assert dataset in self.config.keys()
        subprocess.run(f'wget -O download.file {self.config.get(dataset)}', shell=True, check=True)
        with zipfile.ZipFile('download.file') as zin:
            zin.extractall('.')
        remove('download.file')


if __name__ == "__main__":
    fire.Fire(Download)
