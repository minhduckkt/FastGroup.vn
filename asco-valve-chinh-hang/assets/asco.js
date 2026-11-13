(function(){
/* Ma dat hang: sao chep, "Bao gia ma nay" (dien san form RFQ), khung "Ban dang xem ma ..." khi vao #ma. */
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
function rfqBox(){return document.querySelector('[data-fg-rfq]');}
function setModel(code){var b=rfqBox();if(!b)return;if(window.FG_RFQ_SET_MODEL)window.FG_RFQ_SET_MODEL(b,code);else b.setAttribute('data-fg-model',code);}
function rowOf(id){var t=id&&document.getElementById(id);return t&&t.tagName==='TR'?t:null;}
function focus(id,scroll){var tr=rowOf(id),f=document.getElementById('pn-focus');if(!tr)return false;var d=tr.dataset,code=d.code||id;
 document.querySelectorAll('tr.on').forEach(function(x){x.classList.remove('on');});tr.classList.add('on');
 if(f){f.innerHTML='<div class="pn-k">Bạn đang xem mã đặt hàng</div>'+
   '<div class="pn-line"><span class="pn-big">'+esc(code)+'</span><button type="button" class="copy" data-copy="'+esc(code)+'">Sao chép mã</button></div>'+
   '<dl class="pn-dl"><div><dt>Mã gốc</dt><dd>'+esc(d.base||'')+'</dd></div>'+
   (d.info?'<div><dt>Điện áp coil</dt><dd>'+esc(d.info)+'</dd></div>':'')+
   '<div><dt>Thông số</dt><dd>'+esc(d.spec||'')+'</dd></div>'+
   '<div><dt>Tình trạng</dt><dd class="'+(/^Đang/.test(d.life||'')?'ok':'')+'">'+esc(d.life||'')+'</dd></div></dl>'+
   '<div class="hero-actions"><a class="button button-primary" href="#rfq" data-q="'+esc(id)+'">Báo giá mã này</a>'+
   '<a class="button button-secondary" href="#ma-dat-hang">Xem các mã khác</a></div>';
  f.hidden=false;if(scroll)f.scrollIntoView({block:'start'});}
 setModel(code);return true;}
function copy(btn){var c=btn.getAttribute('data-copy'),old=btn.textContent;
 var ok=function(){btn.textContent='Đã chép';btn.classList.add('done');setTimeout(function(){btn.textContent=old;btn.classList.remove('done');},1500);};
 if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(c).then(ok,function(){fallback(c);ok();});else{fallback(c);ok();}}
function fallback(c){var t=document.createElement('textarea');t.value=c;t.style.position='fixed';t.style.opacity='0';document.body.appendChild(t);t.select();
 try{document.execCommand('copy');}catch(e){}document.body.removeChild(t);}
document.addEventListener('click',function(ev){var t=ev.target.closest('[data-copy],[data-q]');if(!t)return;
 if(t.hasAttribute('data-copy')){ev.preventDefault();copy(t);return;}
 var id=t.getAttribute('data-q');if(rowOf(id))focus(id,false);else setModel(id);});
function fromHash(scroll){var h='';try{h=decodeURIComponent(location.hash.slice(1));}catch(e){}if(h)focus(h,scroll);}
fromHash(false);
window.addEventListener('load',function(){if(rowOf(decodeURIComponent(location.hash.slice(1)))){var f=document.getElementById('pn-focus');if(f)f.scrollIntoView({block:'start'});}});
window.addEventListener('hashchange',function(){fromHash(true);});
})();