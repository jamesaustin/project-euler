def int2string(n):

    one2nine = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    ten2ninteen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                   "sixteen", "seventeen", "eighteen", "nineteen"]
    twenty2ninety = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    m = [int(x) for x in "%04i" % n]

    if m[0] > 0:
        return "onethousand"
    answer = ""
    if m[1] > 0:
        answer += "%shundred" % one2nine[m[1] - 1]
        if m[2] > 0 or m[3] > 0:
            answer += "and"
    if m[2] > 1:
        answer += "%s" % twenty2ninety[m[2] - 2]
    elif m[2] == 1:
        answer += "%s" % ten2ninteen[m[3]]
        return answer
    if m[3] > 0:
        answer += "%s" % one2nine[m[3] - 1]

    return answer.strip()

m = 0
for x in xrange(1, 1001):
    m += len(int2string(x))
print m

# or

def int2string2(n):

    one2nine = [3, 3, 5, 4, 4, 3, 5, 5, 4]
    ten2ninteen = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    twenty2ninety = [6, 6, 5, 5, 5, 7, 6, 6]
    
    m = [int(x) for x in "%04i" % n]

    if m[0] > 0:
        return 11
    answer = 0
    if m[1] > 0:
        answer += one2nine[m[1] - 1] + 7
        if m[2] > 0 or m[3] > 0:
            answer += 3
    if m[2] > 1:
        answer += twenty2ninety[m[2] - 2]
    elif m[2] == 1:
        answer += ten2ninteen[m[3]]
        return answer
    if m[3] > 0:
        answer += one2nine[m[3] - 1]

    return answer

m = 0
for x in xrange(1, 1001):
    m += int2string2(x)
print m