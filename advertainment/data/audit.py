import json,collections
from pools import POOL
from build44 import SPEC
P=json.load(open('pairs44.json'));prob=[]
L2V={}
for a,pool in POOL.items():
    for v,(ph,nr,ev) in pool.items():
        for p in ph: L2V.setdefault(p,set()).add((a,v))
for x in P:
    b=x['brand'];s=SPEC[b]
    # lock 1
    c=collections.Counter(x['city'].upper()); an=collections.Counter(x['anag'])
    fakes=an-c
    if c-an or sum(fakes.values())!=x['fk'] or any(f in c for f in fakes): prob.append((b,'anagram'))
    # lock 2
    tgt={'job':s['jobs'][0],**s['v']}
    fits=[]
    for card in x['pc']['cards']:
        got={}
        for l in card['lines']:
            if l in s['jobs']: got['job']=l
            else:
                m=[av for av in L2V.get(l,[])]
                if len(m)!=1: prob.append((b,'line?',l))
                else: got[m[0][0]]=m[0][1]
        if len(got)!=6: prob.append((b,'card attrs',card['name']))
        fits.append(all(got.get(k)==v for k,v in tgt.items()))
        # each value is target or its near-miss
        for k,v in got.items():
            if k!='job' and v!=tgt[k] and v!=POOL[k][tgt[k]][1]: prob.append((b,'odd value',k,v))
    if fits.count(True)!=1 or not fits[x['pc']['ans']]: prob.append((b,'lock2 answer',fits))
    faces=x['comps'][0]['items']; ev=[i for i in faces if i['id'] in 'ABCDEF' and len(i['id'])==1]
    if len(ev)!=6: prob.append((b,'evidence count'))
    want=[s['jev'][2]]+[POOL[a][tgt[a]][2][2] for a in ['live','media','shop','rhythm','move']]
    have=['|'.join(i['body']) for i in ev]
    if sorted(want)!=sorted(have): prob.append((b,'evidence mismatch'))
    # vault
    nz={i['id']:' '.join(i['body']) for i in x['comps'][1]['items']}
    for q in x['vq']:
        for cid in __import__('re').findall(r'#(\d+)',q):
            if cid not in nz: prob.append((b,'missing clue',cid))
    for need in ['27,000','4 out of every 9','1 in 3','180K','₹2,000 per post for every 60K','₹1,000','1 free post for every 3 paid','₹48,000','₹4,000 each','packs of 4','₹84,000','Half','A quarter']:
        if need not in ' '.join(nz.values()): prob.append((b,'vault number missing',need))
    if x['vc']!='87384': prob.append((b,'code'))
    ids=[i['id'] for c in x['comps'] for i in c['items']]
    if len(ids)!=len(set(ids)): prob.append((b,'dup ids'))
    if not x.get('per') or not x['per'].get('needs'): prob.append((b,'persona'))
print('brands',len(P),'problems',len(prob));[print(p) for p in prob[:30]]
