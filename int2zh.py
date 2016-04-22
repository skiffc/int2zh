# -*- coding: utf-8 -*-

def get_zh( value ):
    words = [ '零', '一', '二', '三', '四', '五', '六', '七', '八', '九' ]
    digi0 = [ '', '十', '百', '千' ]
    digi1 = [ '', '萬', '億', '兆', '京', '垓', '秭' ]

    s = ''
    if value < 0:
        k = -value
    else:
        k = value

    lsb_zero = False
    mid_zero = False

    for i in range( 7 ):
        if k > 0:
            if lsb_zero:
                s = digi1[i]
            else:
                s = digi1[i] + s 
        for j in range( 4 ):
            if k == 0:
                if i == 0 and j == 0:
                    return words[0] 
                else:
                    if value < 0:
                        s = '負' + s
                    return omit(s)
            else:
                v = k % 10
                if v == 0:
                    if lsb_zero or mid_zero:
                        pass
                    elif i == 0 and j == 0:
                        lsb_zero = True
                    else:
                        s = words[0] + s
                        mid_zero = True
                else:
                    s = words[v] + digi0[j] + s
                    lsb_zero = False
                    mid_zero = False

                k = k / 10
    if k > 0:
        return '非常多'
    else:
        if value < 0:
            s = '負' + s
        return omit(s)

def omit( s ):
    if s[:6] == '一十':
        s = s[3:]
    return s

if __name__ == '__main__':
    for p in range( -6, 25, 4 ):
        print p, get_zh( p )
    for p in range( 19 ):
        v = 12 ** p
        print v, get_zh( v )
    print 10000020300, get_zh( 10000020300 )
    print 10000000000000, get_zh( 10000000000000 )
    print "too much", get_zh( 1000**10 )
