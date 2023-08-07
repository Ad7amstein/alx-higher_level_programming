#!/usr/bin/python3
import sys, os

data = "and that piece of art is useful - Dora Korpar, 2015-10-19\n"
data_bytes = data.encode()
stderr_fd = sys.stderr.fileno()
os.write(stderr_fd, data_bytes)
sys.exit(1)
