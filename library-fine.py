def bla(exp, ret):
    if exp['year'] == ret['year'] and exp['mon'] == ret['mon']:
        if ret['day'] <= exp['day']:
            return 0
        return 15 * (ret['day'] - exp['day'])
    if exp['year'] == ret['year']:
        return 500 * (ret['mon'] - ret['mon'])
    return 10000

# Enter your code here. Read input from STDIN. Print output to STDOUT
ret = map(int, raw_input().split())
exp = map(int, raw_input().split())

ret = {'day': ret[0], 'mon': ret[1], 'year': ret[2]}
exp = {'day': exp[0], 'mon': exp[1], 'year': exp[2]}

# same month
print bla(exp, ret)
