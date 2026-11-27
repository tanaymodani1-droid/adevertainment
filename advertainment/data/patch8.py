import sys,json,re
D=sys.argv[1];j=open(D+'/app.js',encoding='utf8').read();b=open(D+'/body.html',encoding='utf8').read()
def rep(s,a,bb,n=1):
    assert s.count(a)==n,(a[:80],s.count(a));return s.replace(a,bb)
P=open('caps44/pairs44.json',encoding='utf8').read(); C=open('caps44/calls44.json',encoding='utf8').read()
a=j.index('const PAIRS=['); e=j.index('\n',a); j=j[:a]+'const PAIRS='+P+';'+j[e:]
a=j.index('const BCALLS={'); e=j.index('\n',a); assert j[e-1]==';' or True; j=j[:a]+'const BCALLS='+C+';'+j[e:]
# Lock 1: fake letters
j=rep(j,"but time scrambled the letters. Unscramble them.</p>","but time scrambled the letters, and <b>'+(pr.fk||0)+' fake letters</b> got mixed in. Throw out the fakes and unscramble the rest.</p>")
# Lock 2 text
j=rep(j,"The 5 pieces of evidence marked <b>“From our customer’s week”</b> (clues A to E in The Faces)","The 6 pieces of evidence marked <b>“From our customer’s week”</b> (clues A to F in The Faces)")
j=rep(j,"who fits all 5.</p>","who fits all 6. Many people below match 5 of them.</p>")
j=rep(j,"' (card '+(p.pc.ans+1)+' of 8)'","' (card '+(p.pc.ans+1)+' of 12)'")
j=rep(j,"'Read clues A to E in The Faces: evidence from our ideal customer’s week. Work out what each one means, then choose the only persona at the bottom of this page who fits all 5.'","'Read clues A to F in The Faces: evidence from our ideal customer’s week. Work out what each one means, then choose the only persona at the bottom of this page who fits all 6.'")
# Jam bug: a wrong persona pick must block every new pick until the jam ends
j=rep(j,"f.addEventListener('submit',async ev=>{ev.preventDefault();const pr=PR_();if(!pr||Date.now()<cool)return;let ok;",
 "f.addEventListener('submit',async ev=>{ev.preventDefault();const pr=PR_();if(!pr||Date.now()<cool)return;if(jamLeft(n)>0){fb.className='lkfb bad';fb.textContent='🔒 The lock is jammed. Wait for the timer.';return}let ok;")
j=rep(j,"const bt=e.target.closest&&e.target.closest('button[data-pick]');if(!bt||bt.disabled)return;","const bt=e.target.closest&&e.target.closest('button[data-pick]');if(!bt||bt.disabled||jamLeft(2)>0)return;")
j=rep(j,"const BUILD='20261126-v16'","const BUILD='20261126-v17'")
b=rep(b,'data-q="Clues A to E in The Faces are about your ideal customer. Work out what each one means. Only one persona fits all 5."','data-q="Clues A to F in The Faces are about your ideal customer. Work out what each one means. Only one persona fits all 6."')
b=rep(b,"8 profiles; clues A–E in The Faces are indirect evidence about the ideal customer; only one profile fits all 5.","12 profiles; clues A–F in The Faces are indirect evidence about the ideal customer; only one profile fits all 6.")
open(D+'/app.js','w',encoding='utf8').write(j);open(D+'/body.html','w',encoding='utf8').write(b);print('ok8')
