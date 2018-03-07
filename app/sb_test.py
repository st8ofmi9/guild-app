from memberobject import *
a = memberobj()
a.gthreads()
a.unpack_and_org(*a.called['log'])
#b = a.stat_threads(a.withdrawal)
c = a.stat_threads(a.deposit)
#a.member(*b,action='withdraw')
a.member(*c, action='deposit')
print(a.deposit)
