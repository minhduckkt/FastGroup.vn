(function(){
/* Tra ma ASCO: chi muc chia theo 4 ky tu dau cua ma goc (8210, 551A...), chi tai khi can. */
var BASE='/asco-valve-chinh-hang/', V=(document.currentScript&&document.currentScript.src.split('?v=')[1])||'', C={};
window.ASCO_IDX=window.ASCO_IDX||{};
function n(s){return (s||'').toUpperCase().replace(/[^A-Z0-9]/g,'');}
function key(q){var m=q.replace(/^[A-Z]+/,''),d=(m.match(/^\d+/)||[''])[0];
 if(d.length>=4)return d.slice(0,4);if(d.length===3&&/[A-Z]/.test(m.charAt(3)))return d+m.charAt(3);if(!d.length&&q.length>=3)return '_';return null;}
function load(k,cb){if(C[k])return cb(C[k]);var s=document.createElement('script');s.src=BASE+'assets/idx/'+k+'.js?v='+V;
 s.onload=function(){var D=window.ASCO_IDX[k]||{p:[],r:[]};C[k]=D.r.map(function(r){return [r[0],r[1]>=0?BASE+D.p[r[1]]+'/':'',r[2],n(r[0])];});cb(C[k]);};
 s.onerror=function(){C[k]=[];cb([]);};document.head.appendChild(s);}
function anc(c){return c.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'');}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
function find(L,q){var x=[],a=[],b=[];for(var i=0;i<L.length;i++){var c=L[i][3];
 if(c===q)x.push(L[i]);else if(c.indexOf(q)===0)a.push(L[i]);else if(c.indexOf(q)>0)b.push(L[i]);if(x.length+a.length>=30)break;}
 return x.concat(a,b).slice(0,30);}
document.querySelectorAll('[data-asco-search]').forEach(function(f){
 var inp=f.querySelector('input'),box=f.nextElementSibling,cur=-1,last=[];
 function row(x){return x[1]?('<a class="r" href="'+x[1]+'#'+anc(x[0])+'"><span class="r-pn">'+esc(x[0])+'</span><span class="r-type">'+esc(x[2].split(' · ')[0])+'</span>'+
  '<span class="r-info">'+esc(x[2].split(' · ').slice(1).join(' · '))+'</span><span></span></a>'):
  ('<a class="r" href="#rfq" data-q="'+esc(x[0])+'"><span class="r-pn">'+esc(x[0])+'</span><span class="r-type">'+esc(x[2].split(' · ')[0])+'</span>'+
  '<span class="r-info">Chưa có trang – gửi mã để báo giá</span><span></span></a>');}
 function show(){var v=n(inp.value.trim());if(v.length<3){box.innerHTML='';box.classList.remove('on');return;}
  var k=key(v);if(!k){box.innerHTML='<div class="r-wait">Nhập thêm: mã gốc dạng 8210G094, 551A017…</div>';box.classList.add('on');return;}
  box.innerHTML='<div class="r-wait">Đang tải danh sách mã…</div>';box.classList.add('on');
  load(k,function(L){if(n(inp.value.trim())!==v)return;var r=find(L,v);last=r;cur=-1;
   box.innerHTML=r.length?('<div class="r-head">'+r.length+(r.length>=30?'+':'')+' kết quả · bấm để mở đúng dòng mã</div>'+r.map(row).join('')):
    '<a class="r-none" href="#rfq" data-q="'+esc(inp.value.trim().toUpperCase())+'"><b>Chưa có mã “'+esc(inp.value.trim())+'” trên portal.</b> Gửi mã này để Fast Group kiểm tra và báo giá →</a>';
   box.classList.add('on');});}
 function mark(k){var L=box.querySelectorAll('a.r');if(!L.length)return;cur=(cur+k+L.length)%L.length;
  L.forEach(function(a,i){a.classList.toggle('sel',i===cur);});L[cur].scrollIntoView({block:'nearest'});}
 inp.addEventListener('input',show);
 inp.addEventListener('keydown',function(ev){if(ev.key==='ArrowDown'){ev.preventDefault();mark(1);}else if(ev.key==='ArrowUp'){ev.preventDefault();mark(-1);}
  else if(ev.key==='Escape'){box.classList.remove('on');}});
 f.addEventListener('submit',function(ev){ev.preventDefault();var s=box.querySelector('a.r.sel')||box.querySelector('a.r');if(s)s.click();});
 document.addEventListener('click',function(ev){if(!f.contains(ev.target)&&!box.contains(ev.target))box.classList.remove('on');});
 var q=new URLSearchParams(location.search).get('q');if(q&&f.closest('main')){inp.value=q;show();}
});})();