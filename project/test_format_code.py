
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol                  #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU Affero General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU Affero General Public License for more details.                          #
#                                                                              #
# You should have received a copy of the GNU Affero General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
################################################################################

def format_code(code_seq):
    code = map(int, str(code_seq))
    code_len = len(code)
    while len(code) < 14:
        code.insert(0, 0)
    while len(code) < 16:
        print code
        print list(enumerate(code))
        print [(len(code) + 1 - i) * v for i, v in enumerate(code)]
        print sum([(len(code) + 1 - i) * v for i, v in enumerate(code)])
        n = sum([(len(code) + 1 - i) * v for i, v in enumerate(code)]) % 11
        if n > 1:
            f = 11 - n
        else:
            f = 0
        code.append(f)
    code_str = "%s.%s.%s.%s.%s-%s" % (str(code[0]) + str(code[1]),
                                      str(code[2]) + str(code[3]) + str(code[4]),
                                      str(code[5]) + str(code[6]) + str(code[7]),
                                      str(code[8]) + str(code[9]) + str(code[10]),
                                      str(code[11]) + str(code[12]) + str(code[13]),
                                      str(code[14]) + str(code[15]))
    if code_len <= 3:
        code_form = code_str[18 - code_len:21]
    elif code_len > 3 and code_len <= 6:
        code_form = code_str[17 - code_len:21]
    elif code_len > 6 and code_len <= 9:
        code_form = code_str[16 - code_len:21]
    elif code_len > 9 and code_len <= 12:
        code_form = code_str[15 - code_len:21]
    elif code_len > 12 and code_len <= 14:
        code_form = code_str[14 - code_len:21]
    return code_form

def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],[(t*1000,),1000,60,60])

if __name__ == '__main__':

    from time import time
    start = time()

    print '--> Executing test_format_code.py ...'

    print '--> format_code("036731518")'
    print format_code("036731518")

    print '--> format_code("000036731518")'
    print format_code("000036731518")

    print '--> format_code("158522278")'
    print format_code("158522278")

    print '--> format_code("01000000001")'
    print format_code("01000000001")

    print '--> format_code("02000000001")'
    print format_code("02000000001")

    print '--> format_code("03000000001")'
    print format_code("03000000001")

    print '--> test_format_code.py'
    print '--> Execution time:', secondsToStr(time() - start)
