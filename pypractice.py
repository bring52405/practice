#!/usr/bin/python3

import re
batRegex = re.compile(r'Bat(man|mobile|copter|Bat)')

mo = batRegex.search('Batmobile has lost a wheel!')
mo1 = batRegex.search('Batcopter has lost a rotor!')

print(mo.group() + '\t' + mo1.group())
print(mo.group(1) + '\t' + mo1.group(1))

print(bool(mo))
print(bool(mo1))

batRegex2 = re.compile(r'Bat(wo)?man')
