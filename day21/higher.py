#!/usr/bin/env python3

import sys

a = 5745418
e = 0

d = e | 65536
e = 14464005
c = d & 255

e = e + c

while True:
  e = e & 16777215
  e = e * 65899
  e = e & 16777215

  if d < 256:
    if e == a:
      print('done')
      sys.exit(0)
  else:
    c = 0

  while True:
    b = c + 1
    b = b * 256

    if (b > d):
      d = c
      c = d & 255
      e = e + c
      break

    c = c + 1