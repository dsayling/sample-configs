import os
import shutil

if not os.path.isdir('sample'):
    os.mkdir('sample')

for dpath, dnames, fnames in os.walk('.'):
    if 'config.yml' in fnames and 'sample-' in dpath:
        existing = os.path.join(dpath, 'config.yml')
        app_name = os.path.dirname(dpath).replace('sample-', '')
        app_path = os.path.join('sample',app_name)
        if not os.path.isdir(app_path):
            os.mkdir(app_path)
        config_path = os.path.join(app_path, 'config.yml')
        shutil.copyfile(existing, os.path.normpath(config_path))





