# LFIprobe
LFIprobe is a Python script that checks whether a given URL is vulnerable to a path traversal attack. Specifically, it looks for the string ../ (the path traversal operator) in the URL's query parameters.

# Requirements
LFIprobe requires Python 3.x and the requests library to be installed. You can install requests using pip:

re: This package provides support for regular expressions.
time: This package provides time-related functions.
argparse: This package provides a command-line argument parsing module.
urllib: This package provides a high-level interface for fetching data from the internet.
requests: This package provides support for sending HTTP requests using Python.
os: This package provides support for operating system related functionalities.


# Usage
To use LFIprobe, simply run the script and provide a URL as a command-line argument:
python lfiprobe.py -u/--url http://example.com/?page=about.php

# Additional
python lfiprobe.py -u/--url http://example.com/?page=about.php --time-sec 5
this is for wait 5 sec before every requests

# License
LFIprobe is released under the MIT License. See LICENSE for more information.
