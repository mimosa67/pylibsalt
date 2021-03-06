#!/usr/bin/env python
# coding: utf-8
# vim:et:sta:sts=2:sw=2:ts=2:tw=0:
"""
SaLT python library.
Used by Salix Live Installer and Bootsetup.
"""
from __future__ import print_function, unicode_literals, absolute_import

__copyright__ = 'Copyright 2011-2014, Salix OS'
__author__ = 'Cyrille Pontvieux <jrd@salixos.org>'
__credits__ = ['Cyrille Pontvieux']
__email__ = 'jrd@salixos.org'
__license__ = 'GPL2+'
__version__ = '0.1.0'

from .chroot import *
from .disk import *
from .execute import *
from .freesize import *
from .fs import *
from .fstab import *
from .kernel import *
from .keyboard import *
from .language import *
from .mounting import *
from .salt import *
from .timezone import *
from .user import *
