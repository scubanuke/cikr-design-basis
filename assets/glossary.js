(function(){
  var G=window.CIKR_GLOSSARY||{}, root=document.documentElement.getAttribute('data-root')||'';
  var terms=Object.keys(G).sort(function(a,b){return b.length-a.length});
  var done={}, pop=null;
  function close(){if(pop){pop.remove();pop=null}}
  function open(btn){
    close(); var k=btn.getAttribute('data-term'), g=G[k]; if(!g) return;
    pop=document.createElement('div'); pop.className='pop'; pop.setAttribute('role','dialog');
    pop.innerHTML='<b></b><span></span> <a>Glossary →</a>';
    pop.querySelector('b').textContent=g.t; pop.querySelector('span').textContent=g.d;
    pop.querySelector('a').href=root+'glossary.html#'+k;
    document.body.appendChild(pop);
    var r=btn.getBoundingClientRect(), w=Math.min(360,window.innerWidth-32);
    pop.style.width=w+'px';
    pop.style.left=Math.max(16,Math.min(window.scrollX+r.left,window.scrollX+window.innerWidth-w-16))+'px';
    pop.style.top=(window.scrollY+r.bottom+8)+'px';
  }
  document.addEventListener('click',function(e){
    var b=e.target.closest&&e.target.closest('button.term');
    if(b){e.preventDefault();open(b);return}
    if(pop&&!pop.contains(e.target)) close();
  });
  document.addEventListener('keydown',function(e){if(e.key==='Escape')close()});
  if(document.body.classList.contains('no-terms')) return;
  var scope=document.querySelectorAll('.card p, .prose p, .qa dd, .sowhat');
  scope.forEach(function(el){
    var walker=document.createTreeWalker(el,NodeFilter.SHOW_TEXT,null), nodes=[], n;
    while((n=walker.nextNode())){ if(!n.parentNode.closest('a,button,code')) nodes.push(n) }
    nodes.forEach(function(node){
      for(var i=0;i<terms.length;i++){
        var k=terms[i]; if(done[k]) continue;
        var re=new RegExp('\\b('+G[k].m+')\\b','i'), m=node.nodeValue.match(re);
        if(!m) continue;
        var idx=m.index, before=node.nodeValue.slice(0,idx), word=m[0], after=node.nodeValue.slice(idx+word.length);
        var b=document.createElement('button'); b.className='term'; b.type='button'; b.setAttribute('data-term',k);
        b.setAttribute('aria-label',word+': show definition'); b.textContent=word;
        var p=node.parentNode; p.insertBefore(document.createTextNode(before),node); p.insertBefore(b,node);
        var rest=document.createTextNode(after); p.insertBefore(rest,node); p.removeChild(node); node=rest;
        done[k]=true;
      }
    });
  });
})();
