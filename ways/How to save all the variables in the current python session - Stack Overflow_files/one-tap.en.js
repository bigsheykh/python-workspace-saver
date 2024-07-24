(()=>{"use strict";var e,n={54742:(e,n,t)=>{t.p=document.getElementById("webpack-public-path").innerText+"Js/"},31564:(e,n,t)=>{t(63480),t(5387);var o=t(89108),c=(t(55763),t(31505)),r=(t(13111),t(46788)),a=(t(50637),t(44098)),i=(t(30501),t(42938),t(84148)),l=t(29864);t(11319);function u(e){const n=function(e){const n=e.replace(/\.(t|j)sx?/,"");return $(`script[type="application/json"][data-role="module-args"][data-module-name="${n}"]`)}(e);return n.toArray().map((e=>JSON.parse($(e).text())))}t(77460);StackExchange=window.StackExchange=window.StackExchange||{},StackOverflow=window.StackOverflow=window.StackOverflow||{},StackExchange=window.StackExchange=window.StackExchange||{},StackOverflow=window.StackOverflow=window.StackOverflow||{};const s=(e,n)=>{!function(e,n,t,o){const c=new FormData;c.append("fKey",null!=o?o:StackExchange.options.user.fkey),c.append("data",JSON.stringify(n)),c.append("event",e);let r={};t&&(r["X-Previous-Event-Id"]=t),fetch("/stackevent",{method:"POST",keepalive:!0,body:c,headers:r}).then((()=>{}))}(e,n)};StackExchange=window.StackExchange=window.StackExchange||{},StackOverflow=window.StackOverflow=window.StackOverflow||{};const{document:f}=c.l;function d(e){let n,t,c,r,a,l,u,s;return{c(){n=(0,o.bG)("script"),n.innerHTML="",c=(0,o.Dh)(),r=(0,o.bG)("form"),a=(0,o.bG)("input"),l=(0,o.Dh)(),u=(0,o.bG)("input"),(0,i.Jn)(n.src,t="https://accounts.google.com/gsi/client")||(0,o.Lj)(n,"src","https://accounts.google.com/gsi/client"),n.async=!0,(0,o.Lj)(a,"type","hidden"),(0,o.Lj)(a,"name","fKey"),a.value=e[1],(0,o.Lj)(u,"type","hidden"),(0,o.Lj)(u,"name","googleIdToken"),u.value="",(0,o.Lj)(r,"id","one-tap-form"),(0,o.Lj)(r,"method","post"),(0,o.Lj)(r,"action",s="/users/auth/gcp?ssrc=google-one-tap&returnurl="+e[0])},m(t,i){(0,o.R3)(f.head,n),(0,o.$T)(t,c,i),(0,o.$T)(t,r,i),(0,o.R3)(r,a),(0,o.R3)(r,l),(0,o.R3)(r,u),e[7](u),e[8](r)},p(e,[n]){2&n&&(a.value=e[1]),1&n&&s!==(s="/users/auth/gcp?ssrc=google-one-tap&returnurl="+e[0])&&(0,o.Lj)(r,"action",s)},i:i.ZT,o:i.ZT,d(t){t&&((0,o.og)(c),(0,o.og)(r)),(0,o.og)(n),e[7](null),e[8](null)}}}function p(e,n,t){let o,c,{returnUrl:i=""}=n,{fKey:l=""}=n,{googleClientId:u=""}=n,{autoselect:f=!1}=n,{oneTapNotShownEvent:d}=n;function p(e){t(3,c.value=e.credential,c),o.submit()}return(0,r.H3)((()=>{window.onload=function(){const e={client_id:u,callback:p,cancel_on_tap_outside:!1,auto_select:f,use_fedcm_for_prompt:!1};google.accounts.id.initialize(e),google.accounts.id.prompt((e=>{!function(e){e.isDisplayMoment()&&e.isDisplayed()&&s("one_tap.shown",{source:window.location.href});e.isDisplayMoment()&&e.isNotDisplayed()&&function(){const e=new CustomEvent(d);window.dispatchEvent(e)}();e.isSkippedMoment()&&"user_cancel"===e.getSkippedReason()&&(document.cookie="notice-signup=0:0:0:1; path=/",s("one_tap.dismissed",{source:window.location.href}))}(e)}))}})),e.$$set=e=>{"returnUrl"in e&&t(0,i=e.returnUrl),"fKey"in e&&t(1,l=e.fKey),"googleClientId"in e&&t(4,u=e.googleClientId),"autoselect"in e&&t(5,f=e.autoselect),"oneTapNotShownEvent"in e&&t(6,d=e.oneTapNotShownEvent)},[i,l,o,c,u,f,d,function(e){a.Vn[e?"unshift":"push"]((()=>{c=e,t(3,c)}))},function(e){a.Vn[e?"unshift":"push"]((()=>{o=e,t(2,o)}))}]}class h extends l.f_{constructor(e){super(),(0,l.S1)(this,e,p,d,i.N8,{returnUrl:0,fKey:1,googleClientId:4,autoselect:5,oneTapNotShownEvent:6})}}const g=h;u("islands/one-tap/index.mod.ts").forEach((e=>{const n=document.getElementById(e.ContainerElementId);new g({target:n,props:{fKey:e.FKey,googleClientId:e.GoogleClientId,autoselect:e.Autoselect,returnUrl:e.ReturnUrl,oneTapNotShownEvent:e.OneTapNotShownEvent}})}))},31505:(e,n,t)=>{t.d(n,{l:()=>o});const o="undefined"!=typeof window?window:"undefined"!=typeof globalThis?globalThis:global},46788:(e,n,t)=>{t.d(n,{H3:()=>a,lu:()=>c,xL:()=>o});t(89108);let o;function c(e){o=e}function r(){if(!o)throw new Error("Function called outside component initialization");return o}function a(e){r().$$.on_mount.push(e)}},44098:(e,n,t)=>{t.d(n,{P$:()=>d,Qk:()=>v,Vn:()=>a,YR:()=>r,y4:()=>f,yl:()=>g});var o=t(84148),c=t(46788);const r=[],a=[];let i=[];const l=[],u=Promise.resolve();let s=!1;function f(){s||(s=!0,u.then(g))}function d(e){i.push(e)}const p=new Set;let h=0;function g(){if(0!==h)return;const e=c.xL;do{try{for(;h<r.length;){const e=r[h];h++,(0,c.lu)(e),w(e.$$)}}catch(e){throw r.length=0,h=0,e}for((0,c.lu)(null),r.length=0,h=0;a.length;)a.pop()();for(let e=0;e<i.length;e+=1){const n=i[e];p.has(n)||(p.add(n),n())}i.length=0}while(r.length);for(;l.length;)l.pop()();s=!1,p.clear(),(0,c.lu)(e)}function w(e){if(null!==e.fragment){e.update(),(0,o.j7)(e.before_update);const n=e.dirty;e.dirty=[-1],e.fragment&&e.fragment.p(e.ctx,n),e.after_update.forEach(d)}}function v(e){const n=[],t=[];i.forEach((o=>-1===e.indexOf(o)?n.push(o):t.push(o))),t.forEach((e=>e())),i=n}},84148:(e,n,t)=>{function o(){}t.d(n,{H1:()=>f,Jn:()=>s,KH:()=>c,N8:()=>l,ZT:()=>o,j7:()=>a,ku:()=>r,sB:()=>i});function c(e){return e()}function r(){return Object.create(null)}function a(e){e.forEach(c)}function i(e){return"function"==typeof e}function l(e,n){return e!=e?n==n:e!==n||e&&"object"==typeof e||"function"==typeof e}let u;function s(e,n){return e===n||(u||(u=document.createElement("a")),u.href=n,e===u.href)}function f(e){return 0===Object.keys(e).length}}},t={};function o(e){var c=t[e];if(void 0!==c)return c.exports;var r=t[e]={exports:{}};return n[e](r,r.exports,o),r.exports}o.m=n,e=[],o.O=(n,t,c,r)=>{if(!t){var a=1/0;for(s=0;s<e.length;s++){for(var[t,c,r]=e[s],i=!0,l=0;l<t.length;l++)(!1&r||a>=r)&&Object.keys(o.O).every((e=>o.O[e](t[l])))?t.splice(l--,1):(i=!1,r<a&&(a=r));if(i){e.splice(s--,1);var u=c();void 0!==u&&(n=u)}}return n}r=r||0;for(var s=e.length;s>0&&e[s-1][2]>r;s--)e[s]=e[s-1];e[s]=[t,c,r]},o.d=(e,n)=>{for(var t in n)o.o(n,t)&&!o.o(e,t)&&Object.defineProperty(e,t,{enumerable:!0,get:n[t]})},o.o=(e,n)=>Object.prototype.hasOwnProperty.call(e,n),o.p="",(()=>{var e={78:0};o.O.j=n=>0===e[n];var n=(n,t)=>{var c,r,[a,i,l]=t,u=0;if(a.some((n=>0!==e[n]))){for(c in i)o.o(i,c)&&(o.m[c]=i[c]);if(l)var s=l(o)}for(n&&n(t);u<a.length;u++)r=a[u],o.o(e,r)&&e[r]&&e[r][0](),e[r]=0;return o.O(s)},t=self.webpackChunkstackoverflow=self.webpackChunkstackoverflow||[];t.forEach(n.bind(null,0)),t.push=n.bind(null,t.push.bind(t))})(),o.O(void 0,[71,3724],(()=>o(54742)));var c=o.O(void 0,[71,3724],(()=>o(31564)));c=o.O(c)})();