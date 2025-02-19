# -*- coding: utf-8 -*-
"""Utilities for Halo library.
"""
import codecs
import platform
import six
import sys

try:
    from shutil import get_terminal_size
except ImportError:
    from backports.shutil_get_terminal_size import get_terminal_size

from termcolor import colored


IS_WIN = any(sys.platform.startswith(i) for i in ["win32", "cygwin"])

if IS_WIN:
    import colorama

    colorama.init(autoreset=True)


def is_supported():
    """Check whether operating system supports main symbols or not.

    Returns
    -------
    boolean
        Whether operating system supports main symbols or not
    """

    os_arch = platform.system()

    return True if os_arch != "Windows" else False


def get_environment():
    """Get the environment in which halo is running

    Returns
    -------
    str
        Environment name
    """
    try:
        from IPython import get_ipython

        shell = get_ipython().__class__.__name__

        if shell == "ZMQInteractiveShell":  # Jupyter notebook or qtconsole
            return "jupyter"
        elif shell == "TerminalInteractiveShell":  # Terminal running IPython
            return "ipython"
        else:
            return "terminal"  # Other type (?)

    except (ImportError, NameError):
        return "terminal"


def colored_frame(frame, color):
    """Color the frame with given color and returns.

    Parameters
    ----------
    frame : str
        Frame to be colored
    color : str
        Color to be applied

    Returns
    -------
    str
        Colored frame
    """
    return colored(frame, color, attrs=["bold"])


def is_text_type(text):
    """Check if given parameter is a string or not

    Parameters
    ----------
    text : *
        Parameter to be checked for text type

    Returns
    -------
    bool
        Whether parameter is a string or not
    """
    return True if isinstance(text, (six.text_type, six.string_types)) else False


def decode_utf_8_text(text):
    """Decode the text from utf-8 format

    Parameters
    ----------
    text : str
        String to be decoded

    Returns
    -------
    str
        Decoded string
    """
    try:
        return codecs.decode(text, "utf-8")
    except (TypeError, ValueError):
        return text


def encode_utf_8_text(text):
    """Encodes the text to utf-8 format

    Parameters
    ----------
    text : str
        String to be encoded

    Returns
    -------
    str
        Encoded string
    """
    try:
        return codecs.encode(text, "utf-8", "ignore")
    except (TypeError, ValueError):
        return text


def get_terminal_columns():
    """Determine the amount of available columns in the terminal

    Returns
    -------
    int
        Terminal width
    """
    terminal_size = get_terminal_size()

    # If column size is 0 either we are not connected
    # to a terminal or something else went wrong. Fallback to 80.
    return 80 if terminal_size.columns == 0 else terminal_size.columns
