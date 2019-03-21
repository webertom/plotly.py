"""
https://plot.ly/python/

Plotly's Python API allows users to programmatically access Plotly's
server resources.

This package is organized as follows:

Subpackages:

- plotly: all functionality that requires access to Plotly's servers

- graph_objs: objects for designing figures and visualizing data

- matplotlylib: tools to convert matplotlib figures

Modules:

- tools: some helpful tools that do not require access to Plotly's servers

- utils: functions that you probably won't need, but that subpackages use

- version: holds the current API version

- exceptions: defines our custom exception classes

"""

from __future__ import absolute_import

from plotly import (
    graph_objs,
    tools,
    utils,
    offline,
    colors,
    io
)

# from plotly.version import __version__
from _plotly_future_ import _future_flags

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

# Set default template here to make sure import process is complete
if 'template_defaults' in _future_flags:
    io.templates._default = 'plotly'
