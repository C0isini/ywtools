#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: nonps
# @Date:   2019-04-15 11:12:53
# @Site:   www.vict.site
# @email:  nonps@gmail.com
# 生成 1-1000 的数字，以 ， 进行分割

frestule = open("/tmp/number.txt", 'a')
for i in range(1, 1000):
    frestule.fwrite(i)

frestule.close()


