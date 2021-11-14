# EpyNN/__init__.py
import tarfile
import os

version = ''

def copy(path):

    print('EpyNN %s - florian.malard@gmail.com and solivier@mcw.edu\n' % version)

    print('Please visit https://epynn.net for documentation\n')

    init_path = os.path.dirname(__file__)

    tar_path = os.path.join(init_path, 'EpyNN.tar')

    print('Extract %s' % tar_path)

    tar = tarfile.open(tar_path).extractall('.')

    target_path = os.path.join(path, 'EpyNN')

    print('Move to %s' % target_path)

    os.rename('EpyNN', target_path)

    print('\nYou must add the following path in your PYTHONPATH:\n')

    print(target_path)

    print()

    return None

