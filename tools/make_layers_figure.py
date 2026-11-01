import textwrap,html
W,H=1200,720
cols=[('Design basis','#0B3D91','#E8EEF9','What it adds','The function: what the facility is built to do, the people, process and technology that deliver it, and the limits it works within.','Success','The function is delivered within its operating limits.'),
('Design basis accident','#B34700','#FFF1E6','What it adds','Accidents drawn from experience: fire, flood, storm, a failed component, an operator’s error, a flawed process.','Success','Recover to normal operation, or reach a safe, known condition and recover from it with outside help.'),
('Deliberate military action','#A4161A','#FBE9EA','What it adds','An adversary who chooses the moment, keeps coming, aims at what matters most and blocks repair and outside help.','Success','Reach and hold a protected state using only what is at the facility, for as long as the attack lasts.')]
o=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" aria-labelledby="dblT dblD" style="font-family:Georgia,\'Times New Roman\',serif">'%(W,H),
'<title id="dblT">What is a design basis? Three layers of analysis</title>',
'<desc id="dblD">Simplified from Figure 1 of FD-DBL, Design Basis Layers. The function and the requirement to perform it safely are kept through three layers: design basis, design basis accident and deliberate military action. Each layer adds conditions and changes what counts as success. As conditions widen, the designs that meet them narrow.</desc>',
'<defs><marker id="ah" markerWidth="14" markerHeight="14" refX="12" refY="7" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L14,7 L0,14 z" fill="#111418"/></marker></defs>',
'<rect x="0" y="0" width="%d" height="%d" fill="#FFFFFF"/>'%(W,H),
'<rect x="20" y="20" width="1160" height="74" rx="8" fill="#0A6B3D"/>',
'<text x="600" y="52" text-anchor="middle" font-size="24" font-weight="bold" fill="#FFFFFF">Kept through every layer: the function the facility is built to do</text>',
'<text x="600" y="80" text-anchor="middle" font-size="20" fill="#FFFFFF">and the requirement that whatever it does, it does safely</text>']
def lines(t,x,y,n=34,size=19,col='#111418',bold=False,lh=25):
    w=textwrap.wrap(t,n); b=' font-weight="bold"' if bold else ''
    return ['<text x="%d" y="%d" font-size="%d" fill="%s"%s>%s</text>'%(x,y+i*lh,size,col,b,html.escape(l)) for i,l in enumerate(w)], y+len(w)*lh
cw=360; gap=40; x0=20
for i,(name,c,bg,l1,t1,l2,t2) in enumerate(cols):
    x=x0+i*(cw+gap)
    o.append('<rect x="%d" y="120" width="%d" height="430" rx="10" fill="%s" stroke="%s" stroke-width="4"/>'%(x,cw,bg,c))
    o.append('<rect x="%d" y="120" width="%d" height="58" rx="10" fill="%s"/><rect x="%d" y="160" width="%d" height="18" fill="%s"/>'%(x,cw,c,x,cw,c))
    o.append('<text x="%d" y="158" text-anchor="middle" font-size="23" font-weight="bold" fill="#FFFFFF">%s</text>'%(x+cw/2,name))
    o.append('<text x="%d" y="212" font-size="15" font-weight="bold" letter-spacing="2" fill="%s">%s</text>'%(x+20,c,l1.upper()))
    r,y=lines(t1,x+20,240); o+=r
    y=max(y+14,385)
    o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2"/>'%(x+20,y-22,x+cw-20,y-22,c))
    o.append('<text x="%d" y="%d" font-size="15" font-weight="bold" letter-spacing="2" fill="%s">%s</text>'%(x+20,y+4,c,l2.upper()))
    r,_=lines(t2,x+20,y+32,bold=True); o+=r
    if i<2:
        ax=x+cw+4; o.append('<line x1="%d" y1="335" x2="%d" y2="335" stroke="#111418" stroke-width="4" marker-end="url(#ah)"/>'%(ax,ax+gap-8))
o+=['<line x1="40" y1="600" x2="1150" y2="600" stroke="#111418" stroke-width="4" marker-end="url(#ah)"/>',
'<text x="40" y="590" font-size="20" font-weight="bold" fill="#111418">The conditions the design must withstand widen</text>',
'<line x1="1160" y1="660" x2="50" y2="660" stroke="#111418" stroke-width="4" marker-end="url(#ah)"/>',
'<text x="1160" y="650" text-anchor="end" font-size="20" font-weight="bold" fill="#111418">The designs that meet them narrow</text>',
'<text x="1180" y="705" text-anchor="end" font-size="14" fill="#3D4550">Simplified from FD-DBL (Design Basis Layers), Figure 1. Where this picture and the text differ, the text governs.</text>','</svg>']
open('assets/figures/design-basis-layers.svg','w',encoding='utf-8').write('\n'.join(o)); print('ok')
