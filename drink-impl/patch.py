import re,sys
p='/Users/yuki/akiba-where-to-eat/drink/index.html'
s=open(p,encoding='utf-8').read()
assert 'id="ld"' not in s
CSS='''<style id="ld-css">
#ld{--ink:#121212;--foam:#FBFAF6;--ac:#F4B223;--ac2:#F5B454;--mu:#5D5A54;--out:cubic-bezier(.22,1,.36,1);--io:cubic-bezier(.65,0,.35,1);position:fixed;inset:0;z-index:99999;background:#F1EFEA;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:26px;overflow:hidden;transition:opacity .45s cubic-bezier(.4,0,.2,1)}
#ld.out{opacity:0;pointer-events:none}
#ld .brand{text-align:center}
#ld .brand b{display:block;font:900 16px/1.2 Archivo,"Noto Sans JP",sans-serif;letter-spacing:.32em;padding-left:.32em;color:var(--ink)}
#ld .brand span{display:block;margin-top:4px;font:700 13px/1.4 Archivo,"Noto Sans JP",sans-serif;color:var(--mu);letter-spacing:.06em}
#ld .stage{position:relative;width:180px;height:172px}
#ld .glass{position:absolute;border:3px solid var(--ink);overflow:hidden;background:#F1EFEA;z-index:2}
#ld .liq{position:absolute;inset:0;background:linear-gradient(180deg,var(--ac2),var(--ac) 70%)}
#ld .liq::before{content:"";position:absolute;left:0;right:0;top:0;height:13px;background:var(--foam);border-bottom:2px solid rgba(18,18,18,.12)}
#ld .glint{position:absolute;left:7px;top:20px;width:5px;height:46%;border-radius:3px;background:rgba(251,250,246,.55);z-index:3}
#ld .hdl{position:absolute;border:3px solid var(--ink);border-radius:0 18px 18px 0;z-index:1}
#ld .bub{position:absolute;bottom:6px;width:6px;height:6px;border-radius:50%;border:1.5px solid var(--foam);opacity:0;animation:ldbub 1.5s cubic-bezier(.5,0,.85,.6) infinite}
@keyframes ldbub{0%{transform:translateY(0);opacity:0}15%{opacity:.95}100%{transform:translateY(-62px);opacity:0}}
#ld .floor{position:absolute;height:3px;border-radius:2px;background:var(--ink);left:8px;right:8px;bottom:22px}
#ld svg.foamsvg{position:absolute;overflow:visible;z-index:3;left:-4px;top:2px;width:64px;height:18px}
#ld svg.foamsvg path{fill:var(--foam);stroke:var(--ink);stroke-width:2.6;stroke-linejoin:round}
#ld .w{position:absolute;bottom:25px;width:56px;height:86px;transform-origin:50% 100%}
#ld .wl{left:14px;animation:ldl 2.4s infinite}#ld .wr{right:14px;animation:ldr 2.4s infinite}
#ld .glass{left:0;bottom:0;width:56px;height:72px;border-radius:4px 4px 12px 12px}
#ld .wl .hdl{left:-20px;bottom:14px;width:23px;height:38px;border-right:0;border-radius:16px 0 0 16px}
#ld .wr .hdl{left:53px;bottom:14px;width:23px;height:38px;border-left:0}
#ld .burst{position:absolute;left:90px;top:68px;width:0;height:0;z-index:5}
#ld .sp{position:absolute;left:-1.5px;bottom:0;width:3px;height:11px;border-radius:2px;background:var(--ink);transform-origin:50% 100%;opacity:0;animation:ldsp 2.4s infinite}
#ld .dr{position:absolute;left:-4px;top:-4px;width:8px;height:8px;border-radius:50%;border:2px solid var(--ink);background:var(--foam);opacity:0;animation:lddr 2.4s infinite}
@keyframes ldl{0%{transform:translate(-10px,0) rotate(-6deg);animation-timing-function:cubic-bezier(.55,0,.8,.45)}30%{transform:translate(5px,-10px) rotate(13deg);animation-timing-function:cubic-bezier(.2,.8,.3,1)}38%{transform:translate(-1px,-9px) rotate(9deg);animation-timing-function:var(--io)}50%{transform:translate(2px,-10px) rotate(11deg);animation-timing-function:var(--io)}78%,100%{transform:translate(-10px,0) rotate(-6deg)}}
@keyframes ldr{0%{transform:translate(10px,0) rotate(6deg);animation-timing-function:cubic-bezier(.55,0,.8,.45)}30%{transform:translate(-5px,-10px) rotate(-13deg);animation-timing-function:cubic-bezier(.2,.8,.3,1)}38%{transform:translate(1px,-9px) rotate(-9deg);animation-timing-function:var(--io)}50%{transform:translate(-2px,-10px) rotate(-11deg);animation-timing-function:var(--io)}78%,100%{transform:translate(10px,0) rotate(6deg)}}
@keyframes ldsp{0%,29%{opacity:0;transform:rotate(var(--a)) translateY(-6px) scaleY(.3)}31%{opacity:1;transform:rotate(var(--a)) translateY(-8px) scaleY(1);animation-timing-function:var(--out)}46%,100%{opacity:0;transform:rotate(var(--a)) translateY(-24px) scaleY(.4)}}
@keyframes lddr{0%,29%{opacity:0;transform:translate(0,0) scale(.4)}31%{opacity:1;animation-timing-function:cubic-bezier(.2,.7,.4,1)}42%{opacity:1;transform:translate(calc(var(--dx)*.6),var(--dy)) scale(1);animation-timing-function:cubic-bezier(.5,0,.9,.5)}56%,100%{opacity:0;transform:translate(var(--dx),calc(var(--dy) + 22px)) scale(.8)}}
@media(prefers-reduced-motion:reduce){#ld *{animation:none!important}}
</style><noscript><style>#ld{display:none}</style></noscript>'''
C='<path d="M3 25 C1 16 8 10 16 13 C18 4 31 1 37 8 C42 0 56 1 58 9 C64 3 77 6 76 15 C84 13 88 20 85 25 Z"/>'
def mug(cls,b1,b2):
    return f'<div class="w {cls}"><div class="hdl"></div><div class="glass"><div class="liq"><i class="bub" style="left:{b1[0]}px"></i><i class="bub" style="left:{b2[0]}px;animation-delay:{b2[1]}s;width:4px;height:4px"></i></div><div class="glint"></div></div><svg class="foamsvg" viewBox="0 0 88 26" preserveAspectRatio="none">{C}</svg></div>'
sp=''.join(f'<span class="sp" style="--a:{a}deg"></span>' for a in [-72,-38,0,38,72])
dr=''.join(f'<span class="dr" style="--dx:{x}px;--dy:{y}px"></span>' for x,y in [(-26,-26),(24,-30),(4,-40)])
HTML=f'<div id="ld" role="status" aria-label="Loading"><div class="stage"><div class="floor"></div>{mug("wl",(14,0),(32,-.8))}{mug("wr",(20,-.4),(36,-1.1))}<div class="burst">{sp}{dr}</div></div><div class="brand"><b>DRINK MAP</b><span>Getting the first round ready</span></div></div><script>window.__ld0=Date.now();</script>'
JS='''<script>(function(){var e=document.getElementById("ld");if(!e)return;var d=0;function done(){if(d)return;d=1;setTimeout(function(){e.classList.add("out");setTimeout(function(){e.remove();var c=document.getElementById("ld-css");if(c)c.remove()},450)},Math.max(0,1700-(Date.now()-window.__ld0)))}
try{if(document.readyState==="complete")done();else addEventListener("load",done)}catch(_){done()}
addEventListener("error",function(){},true);setTimeout(done,6000)})();</script>'''
# css into head end, overlay right after <body>, js at end of body
assert s.count('</style></head><body>')==1
s=s.replace('</style></head><body>','</style>'+CSS+'</head><body>'+HTML,1)
assert s.count('</script></body></html>')==1
s=s.replace('</script></body></html>','</script>'+JS+'</body></html>',1)
open(p,'w',encoding='utf-8').write(s)
