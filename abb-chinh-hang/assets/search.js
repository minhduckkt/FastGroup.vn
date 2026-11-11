(function(){
/* Tra ma: chi muc chi tai khi khach bam vao o tim (khong lam nang trang). */
var BASE='/abb-chinh-hang/', V=(document.currentScript&&document.currentScript.src.split('?v=')[1])||'', I=null, N=null, waits=[];
function load(cb){if(I)return cb();waits.push(cb);if(waits.length>1)return;
 var s=document.createElement('script');s.src=BASE+'assets/search-index.js?v='+V;
 s.onload=function(){var D=window.ABB_IDX||{p:[],r:[]};I=D.r.map(function(r){return [r[0],r[1],BASE+D.p[r[2]]+'/',r[3],r[4]];});
  N=I.map(function(r){return [n(r[0]),n(r[1])];});waits.splice(0).forEach(function(f){f();});};document.head.appendChild(s);}
function n(s){return (s||'').toUpperCase().replace(/[\s\-\/.]/g,'');}
function find(q){q=n(q);if(q.length<2||!I)return[];var x=[],a=[],b=[];for(var i=0;i<I.length;i++){var c=N[i];
 if(c[0]===q||c[1]===q)x.push(I[i]);else if(c[0].indexOf(q)===0||c[1].indexOf(q)===0)a.push(I[i]);else if(c[0].indexOf(q)>0||c[1].indexOf(q)>0)b.push(I[i]);
 if(x.length+a.length>=20)break;}return x.concat(a,b).slice(0,20);}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
var ST={A:['ok','Đang sản xuất'],I:['warn','Ngừng – hỏi mã thay thế']};
document.querySelectorAll('[data-abb-search]').forEach(function(f){
 var inp=f.querySelector('input'),box=f.nextElementSibling,cur=-1;
 function row(x){var st=ST[x[4]];return '<a class="r" href="'+x[2]+'#'+esc(x[0])+'"><span class="r-pn">'+esc(x[0])+'</span>'+
  '<span class="r-type">'+esc(x[1])+'</span><span class="r-info">'+esc(x[3]||'')+'</span>'+
  (st?'<span class="badge '+st[0]+'">'+st[1]+'</span>':'<span></span>')+'</a>';}
 function show(){var v=inp.value.trim();if(v.length<2){box.innerHTML='';box.classList.remove('on');return [];}
  if(!I){box.innerHTML='<div class="r-wait">Đang tải danh sách mã…</div>';box.classList.add('on');load(show);return [];}
  var r=find(v);cur=-1;
  box.innerHTML=r.length?('<div class="r-head">'+r.length+(r.length>=20?'+':'')+' kết quả · bấm để mở đúng dòng mã</div>'+r.map(row).join('')):
   '<a class="r-none" href="#rfq" data-q="'+esc(v.toUpperCase())+'"><b>Chưa có mã “'+esc(v)+'” trên portal.</b> Gửi mã này để Fast Group kiểm tra và báo giá →</a>';
  box.classList.add('on');return r;}
 function mark(k){var L=box.querySelectorAll('a.r');if(!L.length)return;cur=(cur+k+L.length)%L.length;
  L.forEach(function(a,i){a.classList.toggle('sel',i===cur);});L[cur].scrollIntoView({block:'nearest'});}
 inp.addEventListener('focus',function(){load(function(){});});
 inp.addEventListener('input',show);
 inp.addEventListener('keydown',function(ev){if(ev.key==='ArrowDown'){ev.preventDefault();mark(1);}else if(ev.key==='ArrowUp'){ev.preventDefault();mark(-1);}
  else if(ev.key==='Escape'){box.classList.remove('on');}});
 f.addEventListener('submit',function(ev){ev.preventDefault();var s=box.querySelector('a.r.sel')||box.querySelector('a.r');
  if(s){location.href=s.getAttribute('href');return;}load(function(){var r=show();if(r.length)location.href=r[0][2]+'#'+r[0][0];});});
 document.addEventListener('click',function(ev){if(!f.contains(ev.target)&&!box.contains(ev.target))box.classList.remove('on');});
 var q=new URLSearchParams(location.search).get('q');if(q&&f.closest('main')){inp.value=q;load(show);}
});})();