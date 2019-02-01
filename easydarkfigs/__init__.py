from . import figuremagic
import os
import glob
import matplotlib as mpl
import shutil

# https://stackoverflow.com/questions/35851201/how-can-i-share-matplotlib-style
here = os.path.abspath(os.path.dirname(__file__))
BASE_LIBRARY_PATH = os.path.join(mpl.get_configdir(), 'stylelib')
STYLE_PATH = os.path.join(here, 'mplstyles/')
STYLE_EXTENSION = 'mplstyle'
style_files = glob.glob(os.path.join(STYLE_PATH, "*.%s" % (STYLE_EXTENSION)))
assert (len(style_files) >= 2), (STYLE_PATH)
for _path_file in style_files:
    _, fname = os.path.split(_path_file)
    dest = os.path.join(BASE_LIBRARY_PATH, fname)
    if not os.path.isfile(dest):
        shutil.copy(_path_file, dest)
        print("%s style installed" % (fname))


__version__ = "0.11"
