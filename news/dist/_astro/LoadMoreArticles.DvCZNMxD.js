import{j as o}from"./jsx-runtime.D_zvdyIk.js";import{r as n}from"./index.BVOCwoKb.js";function u({articles:s,initialShowCount:a}){const[r,i]=n.useState(a);n.useEffect(()=>{const t=new URLSearchParams(window.location.search),e=parseInt(t.get("count"));!isNaN(e)&&e>a&&i(e)},[a]),n.useEffect(()=>{document.body.classList.remove("fade-out"),new URLSearchParams(window.location.search).get("scroll")==="bottom"&&setTimeout(()=>{const e=document.getElementById(`article-${r-3}`);e&&e.scrollIntoView({behavior:"smooth",block:"start"})},200)},[r]);const l=()=>{const t=r+3;r===a?i(t):(document.body.classList.add("fade-out"),setTimeout(()=>{const e=new URLSearchParams;e.set("count",t),e.set("scroll","bottom"),window.location.replace(`?${e.toString()}`)},100))},c=()=>{window.scrollTo({top:0,behavior:"smooth"})};return o.jsxs(o.Fragment,{children:[o.jsx("style",{children:`
        .related-article {
          background: var(--card-bg, #fff);
          border-radius: var(--radius, 14px);
          box-shadow: var(--shadow, 0 4px 16px rgba(35, 55, 255, 0.08));
          padding: 2.5rem 2rem;
          margin-bottom: 2rem;
        }
        .related-article h2 {
          text-align: center;
          color: #2337ff;
          margin-bottom: 1em;
        }
      `}),o.jsx("section",{id:"related-articles",style:{width:"720px",maxWidth:"100%",margin:"2em auto"},children:s.slice(0,r).map((t,e)=>o.jsxs("div",{className:"related-article",id:`article-${e}`,children:[o.jsx("h2",{children:"Read Next"}),o.jsx("h3",{children:t.title}),o.jsx("p",{children:new Date(t.pubDate).toLocaleDateString()}),o.jsx("div",{dangerouslySetInnerHTML:{__html:t.body}})]},t.id))}),r<s.length&&o.jsxs("div",{style:{textAlign:"center",margin:"2em 0",display:"flex",justifyContent:"center",gap:"1em"},children:[o.jsx("button",{onClick:l,style:{display:"inline-block",padding:"1em 2em",background:"#2337ff",color:"#fff",borderRadius:"8px",textDecoration:"none",fontWeight:"bold",border:"none",cursor:"pointer"},children:"Load More"}),o.jsx("button",{onClick:c,"aria-label":"Scroll to top",style:{display:"inline-block",padding:"1em",background:"#eee",color:"#2337ff",borderRadius:"50%",border:"none",cursor:"pointer",fontSize:"1.5em",lineHeight:"1em",verticalAlign:"middle"},children:"↑"})]})]})}export{u as default};
