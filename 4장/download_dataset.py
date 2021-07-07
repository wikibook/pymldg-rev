import sys
from os import rename
from os.path import exists

sys.path.append('..')

from Dataset.download import Download

if __name__ == "__main__":
    if not exists('human_activity'):
        Download().run('uci_har')
        rename('UCI HAR Dataset', 'human_activity')
        print('Downloading human_activity dataset is done.')
    else:
        print('Already exist human_acitivity dataset.')
