(function(){
var I=window.ABB_IDX||[];function n(s){return (s||'').toUpperCase().replace(/[\s\-\/.]/g,'');}
var N=I.map(function(r){return [n(r[0]),n(r[1])];});
function find(q){q=n(q);if(q.length<2)return[];var a=[],b=[];for(var i=0;i<I.length;i++){var c=N[i];
 if(c[0].indexOf(q)===0||c[1].indexOf(q)===0)a.push(I[i]);else if(c[0].indexOf(q)>0||c[1].indexOf(q)>0)b.push(I[i]);
 if(a.length>=15)break;}return a.concat(b).slice(0,15);}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
document.querySelectorAll('[data-abb-search]').forEach(function(f){
 var inp=f.querySelector('input'),box=f.nextElementSibling;
 function show(){var r=find(inp.value);box.innerHTML=r.map(function(x){return '<a href="'+x[2]+'#'+x[0]+'"><span><b>'+esc(x[1])+'</b> <small>'+esc(x[0])+'</small></span><small>'+esc(x[3])+'</small></a>';}).join('')||(inp.value.length>1?'<a href="#rfq"><span>Chưa có mã này trên portal – gửi yêu cầu báo giá</span></a>':'');box.classList.toggle('on',!!box.innerHTML);return r;}
 inp.addEventListener('input',show);
 f.addEventListener('submit',function(ev){ev.preventDefault();var r=show();if(r.length)location.href=r[0][2]+'#'+r[0][0];});
 var q=new URLSearchParams(location.search).get('q');if(q&&f.closest('main')){inp.value=q;show();}
});})();