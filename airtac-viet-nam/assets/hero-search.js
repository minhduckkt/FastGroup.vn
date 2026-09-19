(function(){
var HUBS=window.AT_INDEX||[],PARTS=null,partsPending=false;
var indexScript=document.querySelector('script[src$="search-index.js"]')||{};
var SITE_BASE=(indexScript.src||new URL("assets/search-index.js",location.href).href).replace(/assets\/search-index\.js(?:\?.*)?$/,"");
function norm(s){return String(s||"").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g,"");}
function key(s){return norm(s).replace(/[^a-z0-9]/g,"");}
function href(u){return new URL(String(u||"").replace(/^\.\.\//,""),SITE_BASE).href;}
function loadParts(cb){
  if(PARTS){cb();return;}
  if(partsPending){return;}
  partsPending=true;
  var base=indexScript.src||"";
  var s=document.createElement("script");
  s.src=base.replace("search-index.js","parts-index.js");
  s.onload=function(){PARTS=window.AT_PARTS||[];partsPending=false;cb();};
  s.onerror=function(){PARTS=[];partsPending=false;cb();};
  document.head.appendChild(s);
}
function scoreHub(it,q){var k=key(it.c),n=key(q);
  if(!n)return 0;
  if(k===n)return 100;
  if(k.indexOf(n)===0)return 80;
  if(norm([it.c,it.n,it.d,it.g].join(" ")).indexOf(norm(q))>=0)return 40;
  return 0;}
function scorePart(it,q){var k=key(it.c),n=key(q);
  if(!n)return 0;
  if(k===n)return 100;
  if(k.indexOf(n)===0)return 85;
  if(k.indexOf(n)>=0)return 55;
  if(key(it.m).indexOf(n)===0)return 50;
  return 0;}
function ranked(q,limit){
  var out=HUBS.map(function(it){return{it:it,s:scoreHub(it,q),p:false}})
               .filter(function(x){return x.s>0});
  if(PARTS){
    out=out.concat(PARTS.map(function(it){return{it:it,s:scorePart(it,q),p:true}})
                        .filter(function(x){return x.s>0}));
  }
  return out.sort(function(a,b){return b.s-a.s||a.it.c.length-b.it.c.length}).slice(0,limit||12);
}
function card(x){var it=x.it;
  var t=x.p?"Mã hàng":(it.t||"");
  var sub=x.p?("Model "+it.m+(it.d?" · "+it.d:"")):(it.d||"");
  return '<article class="card"><div class="product-meta">'+t+'</div>'+
         '<h3><a href="'+href(it.u)+'">'+it.c+'</a></h3><p>'+sub+'</p></article>';}
/* --- o tra ma o hero --- */
var hero=document.getElementById("heroq"),ac=document.getElementById("heroAc");
if(hero&&ac){
  var draw=function(){
    var q=hero.value.trim();
    if(!q){ac.classList.remove("on");ac.innerHTML="";return;}
    var hits=ranked(q,6);
    ac.innerHTML=hits.map(function(x){var it=x.it;
      return '<a href="'+href(it.u)+'"><span class="code">'+it.c+'</span>'+
             '<span>'+(x.p?("Model "+it.m):(it.d||""))+'</span>'+
             '<span class="mt">'+(x.p?"Mã hàng":(it.t||""))+'</span></a>';}).join("")+
      '<a class="all" href="'+href("tra-cuu-part-number/?q="+encodeURIComponent(q))+'">Xem tất cả kết quả</a>';
    ac.classList.add("on");};
  hero.addEventListener("input",function(){loadParts(draw);draw();});
  hero.addEventListener("focus",function(){loadParts(function(){});});
  document.addEventListener("click",function(e){if(!ac.contains(e.target)&&e.target!==hero)ac.classList.remove("on");});
}
/* --- trang tra ma --- */
var box=document.getElementById("siteSearch"),out=document.getElementById("searchResults");
if(box&&out){
  var params=new URLSearchParams(location.search);
  box.value=params.get("q")||"";
  var render=function(){
    var q=box.value.trim();
    if(!q){out.innerHTML='<article class="card"><h3>Nhập mã hàng hoặc model để tra</h3>'+
      '<p>Ví dụ: 4V210, SC, GAC, LSH.</p></article>';return;}
    var hits=ranked(q,30);
    out.innerHTML=hits.length?hits.map(card).join(""):
      '<article class="card"><h3>Không thấy mã phù hợp</h3>'+
      '<p>Kiểm tra lại cách viết mã, hoặc gửi RFQ để Fast Group tra giúp trong catalog gốc.</p></article>';};
  box.addEventListener("input",function(){loadParts(render);render();});
  loadParts(render);render();
}
})();
