#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set et ai sta sts=2 sw=2 ts=2 tw=0:
"""
Chroot function
"""
from __future__ import print_function, unicode_literals, absolute_import

from .execute import *
import os


def execChroot(path, cmd, shell=False):
  """
  Execute cmd in the chroot defined by path.
  Paths in cmd should be relative to the new root directory.
  """
  checkRoot()
  if not path:
    raise IOError("You should provide a path to change the root directory.")
  elif not os.path.isdir(path):
    raise IOError("'{0}' does not exist or is not a directory.".format(path))
  chrootCmd = ['chroot', path]
  if shell:
    chrootCmd.append('sh')
    chrootCmd.append('-c')
    if type(cmd) == list:
      chrootCmd.append(' '.join(cmd))
    else:
      chrootCmd.append(cmd)
  else:
    if type(cmd) == list:
      chrootCmd.extend(cmd)
    else:
      chrootCmd.append(cmd)
  return execCall(chrootCmd, shell=False)
