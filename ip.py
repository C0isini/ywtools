#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: nonps
# @Date:   2019-04-18 10:35:26
# @Site:   www.vict.site
# @email:
#
#
import os

print(os.name)
s = os.system('ipconfig')
content = os.popen('opconfig').read()
print(content)
