from collections import Counter
from app.memberobject import *

a = memberobj()
a.gthreads()
a.unpack_and_org(*a.called['log'])
r = []
for x in a.invited:
	r.append(x['invited_by'])
q = Counter(r)
recruit_stats = {}
for thing in q:
    recruit_stats[thing] = q[thing]
print(recruit_stats)