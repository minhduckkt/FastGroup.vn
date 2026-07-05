(function(){
  var input=document.getElementById("heroq"),box=document.getElementById("heroAc"),form=document.getElementById("check-ma");
  if(!input||!box||!form)return;
  var CATN={gauge:"Đồng hồ áp suất",sensor:"Cảm biến áp suất",switch:"Công tắc",thermo:"Đo nhiệt độ",acc:"Phụ kiện"};
  function norm(s){return (s||"").toString().toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g,"").replace(/đ/g,"d").replace(/[^a-z0-9]/g,"");}
  var ITEMS=null,hi=-1,cur=[];
  function ready(){ if(ITEMS)return true;
    var d=window.WIKA_INDEX; if(!d)return false;
    ITEMS=d.items.map(function(it){var g=d.groups[it[2]];
      return{code:it[0],slug:it[1],rng:it[3]||"",dia:it[4]||"",thr:it[5]||"",unit:it[7]||"bar",gname:g[1],cat:g[2],
        hay:norm(it[0])+" "+norm(g[1])+" "+norm(it[3])+" "+norm(it[4])+" "+norm(it[5])+" "+norm(CATN[g[2]]),nc:norm(it[0])};});
    return true;
  }
  function esc(s){return (s+"").replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];});}
  function find(q){
    var qn=norm(q),tk=q.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g,"").replace(/đ/g,"d").split(/[^a-z0-9]+/).filter(Boolean),r=[];
    for(var i=0;i<ITEMS.length;i++){var it=ITEMS[i],sc=0;
      if(it.nc===qn)sc=100;else if(it.nc.indexOf(qn)===0)sc=80;else if(it.nc.indexOf(qn)>=0)sc=60;
      else{var ok=true;for(var t=0;t<tk.length;t++){if(it.hay.indexOf(tk[t])<0){ok=false;break;}}if(!ok)continue;sc=30;}
      r.push([sc,it]); if(r.length>500)break;
    }
    r.sort(function(a,b){return b[0]-a[0]||(a[1].code<b[1].code?-1:1);});
    return r.slice(0,7).map(function(x){return x[1];});
  }
  function draw(q){
    if(!ready())return; cur=find(q);hi=-1;
    if(!cur.length){box.classList.remove("on");box.innerHTML="";return;}
    var html=cur.map(function(it){
      var mt=[it.rng?it.rng+" "+it.unit:"",it.dia?"Ø"+it.dia:""].filter(Boolean).join(" · ");
      return '<a href="san-pham/'+encodeURIComponent(it.slug)+'/index.html"><span class="code">WIKA '+esc(it.code)+'</span><span class="mt">'+esc(mt)+'</span></a>';
    }).join("");
    html+='<a class="all" href="tim-kiem/index.html?q='+encodeURIComponent(q)+'">Xem tất cả kết quả cho “'+esc(q)+'” →</a>';
    box.innerHTML=html;box.classList.add("on");
  }
  var t;input.addEventListener("input",function(){var q=input.value.trim();
    if(q.length<1){box.classList.remove("on");return;}
    clearTimeout(t);t=setTimeout(function(){draw(q);},110);});
  input.addEventListener("keydown",function(e){
    var links=box.querySelectorAll("a");
    if(e.key==="ArrowDown"){e.preventDefault();hi=Math.min(hi+1,links.length-1);}
    else if(e.key==="ArrowUp"){e.preventDefault();hi=Math.max(hi-1,-1);}
    else if(e.key==="Enter"){if(hi>=0&&links[hi]){e.preventDefault();window.location.href=links[hi].href;return;}return;}
    else return;
    for(var i=0;i<links.length;i++)links[i].classList.toggle("hl",i===hi);
  });
  document.addEventListener("click",function(e){if(!form.contains(e.target))box.classList.remove("on");});
})();
