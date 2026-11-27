import sys
D=sys.argv[1]
b=open(D+'/body.html').read();c=open(D+'/app.css').read();j=open(D+'/app.js').read()
h=b.replace('/*CSS*/',c,1).replace('/*JS*/',j,1)
open(D+'/index.html','w').write(h)
open(D+'/admin.html','w').write(h.replace('<title>Advertainment · Round 2</title>','<title>Advertainment · OC panel</title>',1))
print('built',len(h))
