import sys
import os.path
# add 'lib' subdirectory to 'sys.path', so that our 'main' module can load 
# third-party libraries.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
