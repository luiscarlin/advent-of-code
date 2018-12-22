#!/usr/bin/env python3

seen_ds = set()
e_values = set()

a = 100
e = 0

d = e | 65536
e = 14464005

while True:
  c = d & 255
  e = e + c
  e = ((e & 16777215) * 65899) & 16777215

  if d < 256:
    if e not in e_values:
      print(e)
    e_values.add(e)
    d = e | 65536
    e = 14464005
  else:
     d = d // 256
