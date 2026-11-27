import json,random,sys
sys.path.insert(0,'.'); sys.path.insert(0,'../caps15'); sys.path.insert(0,'../caps33')
from pools import POOL,W
from new29 import N as NEW
from riddle2 import JOB as J15
import vault3, calls as C33
import vault4

ORDER=['Micromax','Celkon','Dyanora','Solidaire','Forhans','Keltron','Educomp','Amrapali','Citra','ModiLuft','Damania Airways','East-West Airlines','TinyOwl',
 'Kingfisher Airlines','Jet Airways','Air Sahara','Housejoy','Yebhi','Cox & Kings','Stayzilla','Pyramid Saimira','PepperTap','Jabong','TaxiForSure','Subhiksha','Weston','Gitanjali Gems']
assert len(ORDER)==27
OLD15={x['brand']:x for x in json.load(open('../caps15/pairs15.json'))}
CALLS15=json.load(open('../caps15/calls15.json'))
OLD33={x['brand']:x for x in json.load(open('../caps33/all33_v5.json'))}
from hard import H as _H
MOVE15={'Kingfisher Airlines':'cab','Jet Airways':'bus','Air Sahara':'scooter','Housejoy':'car','Yebhi':'walks','Cox & Kings':'metro','Stayzilla':'bus',
 'Pyramid Saimira':'scooter','PepperTap':'scooter','Jabong':'metro','TaxiForSure':'cab','Subhiksha':'car','Weston':'scooter','Gitanjali Gems':'cycle','Hike Messenger':'scooter'}
EXTRA=['Aarav','Ira','Dev','Maya']
# ---- per-brand Lock 2 spec: jobs[target,near], job evidence, target values
SPEC={}
for b,(jobs,jev,live,media,shop,rhythm) in J15.items():
    nm=_H[b]['names']; nm=nm+[EXTRA[i]+' '+nm[i].split()[-1] for i in range(4)]
    if b=='TaxiForSure': jev=['Sticky note',W,'“The testers found 2 bugs in MY code. Fix them before the 4 pm release.”']
    nm=[{'Tanya Kapoor':'Kavya Kapoor','Arjun Rao':'Abhay Rao'}.get(z,z) for z in nm]
    SPEC[b]=dict(jobs=jobs[:2],jev=jev,v=dict(live=live,media=media,shop=shop,rhythm=rhythm,move=MOVE15[b]),names=nm[:12])
for b,d in NEW.items():
    SPEC[b]=dict(jobs=d['jobs'],jev=d['jev'],v=dict(zip(['live','media','shop','rhythm','move'],d['v'])),names=d['names'])
ATT=['job','live','media','shop','rhythm','move']

def lock2(b):
    s=SPEC[b]; assert len(s['names'])==12 and len(set(s['names']))==12,b
    rr=random.Random('L2v8'+b)
    # T/N vectors: 12 cards, card 0 = target (all T); each attribute T on exactly 6 cards; >=4 attributes have a decoy failing only it
    for _ in range(200000):
        F=rr.sample(range(6),4)
        ones_=[tuple(0 if i==a else 1 for i in range(6)) for a in F]
        need=[5-sum(v[i] for v in ones_) for i in range(6)]
        cols=[set(rr.sample(range(7),need[i])) for i in range(6)]
        rest=[tuple(1 if d in cols[i] else 0 for i in range(6)) for d in range(7)]
        vecs=[(1,)*6]+ones_+rest
        if len(set(vecs))!=12 or any(sum(v)<1 for v in rest): continue
        one=[a for a in range(6) if any(sum(v)==5 and v[a]==0 for v in vecs[1:])]
        dd=vecs[1:]; rr.shuffle(dd); vecs=[vecs[0]]+dd
        break
    else: raise SystemExit('vec '+b)
    def val(a,t):
        if a=='job': return s['jobs'][0 if t else 1]
        tv=s['v'][a]; return tv if t else POOL[a][tv][1]
    def line(a,t):
        if a=='job': return val(a,t)
        return rr.choice(POOL[a][val(a,t)][0])
    cards=[]
    for k,v in enumerate(vecs):
        L=[line(a,v[i]) for i,a in enumerate(ATT)]; rr.shuffle(L)
        cards.append({'name':s['names'][k],'lines':L,'_v':v})
    order=list(range(12)); rr.shuffle(order)
    cards=[cards[i] for i in order]; ans=order.index(0)
    # check: only the answer card has every target value
    assert [c['_v']==(1,)*6 for c in cards].count(True)==1 and cards[ans]['_v']==(1,)*6
    for a in range(6): assert sum(c['_v'][a] for c in cards)==6
    for c in cards: del c['_v']
    ev=[s['jev']]+[POOL[a][s['v'][a]][2] for a in ATT[1:]]
    re_=random.Random('ev8'+b); re_.shuffle(ev)
    evi=[{'id':'ABCDEF'[k],'type':e[0],'src':e[1],'body':e[2].split('|'),'d':1} for k,e in enumerate(ev)]
    # every target value's evidence must not be shared with its near-miss value
    for a in ATT[1:]:
        tv=s['v'][a]; nv=POOL[a][tv][1]; assert nv in POOL[a] and nv!=tv,(b,a)
    return {'cards':cards,'ans':ans},evi,len(one)

FAKE='RSTLNDMKPHBGCAEIOUY'
def anag(b,city):
    rr=random.Random('an8'+b); up=city.upper()
    k=2 if len(up)>=10 else 3
    pool=[c for c in FAKE if c not in up]; fk=rr.sample(pool,k)
    while True:
        l=list(up)+fk; rr.shuffle(l); an=''.join(l)
        if not an.startswith(up[:2]) and up not in an: break
    return an,k,fk

out=[];calls={}
for n,b in enumerate(ORDER,1):
    if b in OLD15:
        o=OLD15[b]; faces=[i for i in o['comps'][0]['items'] if i['id'].isdigit()]
        noise=[i for i in o['comps'][1]['items'] if int(i['id'])<=26]; shelves=o['comps'][2]['items']
        city,alt,lid,per,fail,who,cust=o['city'],o['alt'],o['lid'],dict(o['per']),o.get('fail'),o['who'],o['cust']
        product=o['product']; cl=CALLS15[str(o['n'])]
        if b=='TaxiForSure': per['home']='Shares a flat in Kakkanad with two college friends. Her family is in Thrissur'
    else:
        o=OLD33[b]; d=NEW[b]
        faces=o['comps'][0]['items']; noise=sorted([i for i in o['comps'][1]['items'] if int(i['id'])<=26],key=lambda i:int(i['id'])); shelves=o['comps'][2]['items']
        for i in faces+noise+shelves: i.setdefault('d',1)
        city=o['city']; alt=sorted(set([city.lower()]+d['alt'])); lid=o['lid']; per=d['per']; fail=None; product=o['product']
        who={'c':[{'name':per['name'],'age':per['age'],'line':per['job']+'.'}],'r':0}
        cust={'o':[per['name']+', '+str(per['age'])+'. '+per['job']+'.'],'r':0,'ev':[]}
        oldn=[x['brand'] for x in json.load(open('../caps33/all33_v5.json'))].index(b)+1
        cl=[list(t) for t in C33.C[oldn]]
    pc,evi,ones=lock2(b)
    assert pc['cards'][pc['ans']]['name']==per['name'],(b,pc['cards'][pc['ans']]['name'],per['name'])
    nz=noise+[{'id':str(27+k),'type':a[0],'src':a[1],'body':a[2].split('|'),'d':1} for k,a in enumerate(vault4.noise(b,city))]
    ids=[i['id'] for i in faces+evi+nz+shelves]; assert len(ids)==len(set(ids)),(b,ids)
    an,fk,fl=anag(b,city)
    out.append(dict(n=n,brand=b,product=product,city=city,alt=alt,lid=lid,fail=fail,
      comps=[{'no':1,'name':'The Faces','at':'0:00','items':faces+evi},{'no':2,'name':'The Noise','at':'0:07','items':nz},{'no':3,'name':'The Shelves','at':'0:14','items':shelves}],
      anag=an,fk=fk,cust=cust,who=who,per=per,vq=[t for t,a in vault4.Q],vc=vault4.CODE,pq=[],grid=None,pc=pc))
    calls[str(n)]=cl
    print(n,b,city,an,'fakes:',''.join(fl),'| L2 ans card',pc['ans']+1,per['name'],'| clues needed',ones)
json.dump(out,open('pairs44.json','w'),ensure_ascii=False)
json.dump(calls,open('calls44.json','w'),ensure_ascii=False)
