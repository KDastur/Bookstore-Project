<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BookStore — Books, Ordered</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,500&family=Source+Sans+3:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root{
    --ink:#181510;
    --ink-2:#221d16;
    --parchment:#efe6d3;
    --parchment-2:#e4d8ba;
    --burgundy:#7a2431;
    --burgundy-lt:#9c3644;
    --gold:#c9a227;
    --teal:#3a5560;
    --cream:#f4ecdb;
    --cream-dim:#cdc2a8;
    --shadow: 0 18px 40px -20px rgba(0,0,0,0.6);
    --radius: 3px;
  }
  *{box-sizing:border-box;}
  html,body{margin:0;padding:0;}
  body{
    background: var(--ink);
    color: var(--cream);
    font-family:'Source Sans 3', sans-serif;
    min-height:100vh;
    -webkit-font-smoothing:antialiased;
  }
  ::selection{ background: var(--gold); color: var(--ink); }
  h1,h2,h3,h4{ font-family:'Fraunces', serif; margin:0; font-weight:600; }
  .mono{ font-family:'IBM Plex Mono', monospace; letter-spacing:0.02em; }
  a{ color:inherit; }
  button{ font-family:inherit; cursor:pointer; }
  ::-webkit-scrollbar{ width:10px; height:10px;}
  ::-webkit-scrollbar-thumb{ background:var(--parchment-2); border-radius:6px;}
  ::-webkit-scrollbar-track{ background:var(--ink-2);}

  /* ---------- HEADER ---------- */
  header{
    position:sticky; top:0; z-index:40;
    background: rgba(24,21,16,0.92);
    backdrop-filter: blur(8px);
    border-bottom:1px solid rgba(201,162,39,0.25);
  }
  .header-inner{
    max-width:1180px; margin:0 auto; padding:16px 28px;
    display:flex; align-items:center; gap:24px;
  }
  .logo{ display:flex; align-items:center; gap:10px; flex-shrink:0; }
  .logo-mark{
    width:30px; height:30px; border:1.5px solid var(--gold); border-radius:50%;
    display:flex; align-items:center; justify-content:center;
    font-family:'Fraunces', serif; font-style:italic; font-size:16px; color:var(--gold);
  }
  .logo-word{ font-size:22px; letter-spacing:0.01em; }

  .search-wrap{ flex:1; position:relative; max-width:520px; }
  .search-wrap input{
    width:100%; background:var(--ink-2); border:1px solid rgba(244,236,219,0.18);
    color:var(--cream); padding:10px 14px 10px 38px; border-radius:20px; font-size:14px;
    outline:none; transition:border-color .2s, background .2s;
  }
  .search-wrap input:focus{ border-color:var(--gold); background:#2a241a; }
  .search-wrap input::placeholder{ color:var(--cream-dim); }
  .search-icon{ position:absolute; left:13px; top:50%; transform:translateY(-50%); opacity:0.6; font-size:14px; pointer-events:none;}

  .cart-btn{
    background:none; border:1px solid rgba(244,236,219,0.25); color:var(--cream);
    padding:9px 16px; border-radius:20px; font-size:13px; display:flex; align-items:center; gap:8px;
    transition: border-color .2s, background .2s; white-space:nowrap;
  }
  .cart-btn:hover{ border-color:var(--gold); background:rgba(201,162,39,0.08); }
  .cart-count{
    background:var(--burgundy); color:var(--cream); border-radius:50%;
    width:19px; height:19px; font-size:11px; display:flex; align-items:center; justify-content:center;
    font-family:'IBM Plex Mono',monospace;
  }

  /* ---------- HERO ---------- */
  .hero{
    max-width:1180px; margin:0 auto; padding:64px 28px 36px;
    display:grid; grid-template-columns: 1.3fr 1fr; gap:40px; align-items:end;
  }
  .hero h1{ font-size:52px; line-height:1.05; font-weight:600; }
  .hero p{ color:var(--cream-dim); font-size:16px; line-height:1.6; max-width:40ch; margin-top:16px; }
  .hero-index{
    border-left:1px solid rgba(244,236,219,0.2); padding-left:24px;
    font-family:'IBM Plex Mono',monospace; font-size:12px; color:var(--cream-dim); line-height:2.1;
  }
  .hero-index b{ color:var(--cream); font-weight:500; }

  /* ---------- GENRE CHIPS ---------- */
  .chip-row{
    max-width:1180px; margin:0 auto; padding:0 28px 8px;
    display:flex; gap:10px; flex-wrap:wrap;
  }
  .chip{
    border:1px solid rgba(244,236,219,0.22); background:none; color:var(--cream-dim);
    padding:7px 15px; border-radius:16px; font-size:12.5px; font-family:'IBM Plex Mono',monospace;
    letter-spacing:0.03em; transition:all .15s;
  }
  .chip:hover{ color:var(--cream); border-color:var(--cream-dim); }
  .chip.active{ background:var(--gold); color:var(--ink); border-color:var(--gold); font-weight:500;}

  /* ---------- BOOK GRID ---------- */
  .shelves{ max-width:1180px; margin:0 auto; padding:36px 28px 90px; }
  .shelf-section{ margin-bottom:56px; }
  .shelf-label{
    display:flex; align-items:baseline; gap:14px; margin-bottom:18px;
  }
  .shelf-label h2{ font-size:22px; }
  .shelf-label .count{ color:var(--cream-dim); font-size:12px; font-family:'IBM Plex Mono',monospace; }
  .shelf-rule{ flex:1; height:1px; background:rgba(244,236,219,0.15); }

  .book-grid{
    display:grid;
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap:22px;
  }
  .book-card{
    position:relative; cursor:pointer;
    display:flex; flex-direction:column;
    transition: transform .22s cubic-bezier(.2,.8,.3,1);
  }
  .book-card:hover{ transform: translateY(-6px); }
  .book-cover-face{
    width:100%; aspect-ratio: 2 / 3; border-radius:4px;
    position:relative; overflow:hidden;
    box-shadow: var(--shadow), inset 0 0 0 1px rgba(255,255,255,0.06);
    display:flex; flex-direction:column; justify-content:space-between;
    padding:16px 14px;
  }
  .book-cover-face::before{
    content:""; position:absolute; inset:0;
    background: linear-gradient(180deg, rgba(0,0,0,0) 55%, rgba(0,0,0,0.55) 100%);
  }
  .book-card-genre{
    position:relative; z-index:1;
    font-family:'IBM Plex Mono',monospace; font-size:9.5px; text-transform:uppercase;
    letter-spacing:0.08em; opacity:0.8;
  }
  .book-card-title{
    position:relative; z-index:1;
    font-family:'Fraunces', serif; font-weight:600; font-size:15px; line-height:1.2;
    color:var(--cream); text-shadow:0 1px 3px rgba(0,0,0,0.4);
  }
  .book-card-author{
    position:relative; z-index:1;
    font-family:'IBM Plex Mono',monospace; font-size:10px; color:rgba(244,236,219,0.75);
    margin-top:4px;
  }

  /* ---------- MODALS ---------- */
  .overlay{
    position:fixed; inset:0; background:rgba(10,8,5,0.72); backdrop-filter:blur(3px);
    display:flex; align-items:center; justify-content:center; z-index:100;
    opacity:0; pointer-events:none; transition:opacity .2s;
    padding:20px;
  }
  .overlay.show{ opacity:1; pointer-events:auto; }

  .book-modal{
    background:var(--parchment); color:var(--ink); border-radius:6px;
    max-width:640px; width:100%; max-height:88vh; overflow-y:auto;
    display:grid; grid-template-columns: 200px 1fr;
    box-shadow: 0 40px 80px -20px rgba(0,0,0,0.7);
    transform:translateY(16px) scale(0.98); transition:transform .25s cubic-bezier(.2,.8,.3,1);
  }
  .overlay.show .book-modal{ transform:translateY(0) scale(1); }
  .book-cover{
    padding:26px 22px; display:flex; flex-direction:column; justify-content:space-between;
    color:var(--cream); position:relative; min-height:280px;
  }
  .book-cover .genre-tag{ font-family:'IBM Plex Mono',monospace; font-size:10px; text-transform:uppercase; letter-spacing:0.1em; opacity:0.85;}
  .book-cover h3{ font-size:21px; line-height:1.15; margin:14px 0 6px; }
  .book-cover .cover-author{ font-size:12px; font-family:'IBM Plex Mono',monospace; opacity:0.85; }
  .book-detail{ padding:26px 26px 26px 22px; }
  .book-detail .price{ font-family:'IBM Plex Mono',monospace; font-size:20px; color:var(--burgundy); margin-bottom:14px; }
  .book-detail p.blurb{ font-size:14.5px; line-height:1.65; color:#3a3226; margin-bottom:20px; }
  .book-detail .meta-row{ display:flex; gap:18px; font-size:11.5px; font-family:'IBM Plex Mono',monospace; color:#6b5f47; margin-bottom:20px; text-transform:uppercase; letter-spacing:0.04em;}
  .btn{
    border:none; border-radius:20px; padding:11px 24px; font-size:14px; font-weight:500;
    transition:transform .12s, box-shadow .12s;
  }
  .btn:active{ transform:scale(0.97); }
  .btn-primary{ background:var(--burgundy); color:var(--cream); }
  .btn-primary:hover{ background:var(--burgundy-lt); }
  .btn-ghost{ background:none; border:1px solid #3a3226; color:#3a3226; }
  .btn-block{ width:100%; }
  .close-x{
    position:absolute; top:14px; right:16px; background:none; border:none; color:inherit;
    font-size:20px; opacity:0.7; line-height:1;
  }
  .close-x:hover{ opacity:1; }

  /* ---------- CART DRAWER ---------- */
  .drawer-overlay{
    position:fixed; inset:0; background:rgba(10,8,5,0.6); z-index:110;
    opacity:0; pointer-events:none; transition:opacity .25s;
  }
  .drawer-overlay.show{ opacity:1; pointer-events:auto; }
  .drawer{
    position:fixed; top:0; right:0; bottom:0; width:400px; max-width:92vw;
    background:var(--parchment); color:var(--ink); z-index:111;
    display:flex; flex-direction:column;
    transform:translateX(100%); transition:transform .3s cubic-bezier(.2,.8,.3,1);
    box-shadow:-20px 0 50px rgba(0,0,0,0.5);
  }
  .drawer.show{ transform:translateX(0); }
  .drawer-head{
    padding:22px 24px 16px; border-bottom:1px solid rgba(0,0,0,0.1);
    display:flex; justify-content:space-between; align-items:center;
  }
  .drawer-head h3{ font-size:19px; }
  .drawer-body{ flex:1; overflow-y:auto; padding:10px 24px; }
  .cart-item{
    display:flex; gap:12px; padding:16px 0; border-bottom:1px solid rgba(0,0,0,0.08);
  }
  .cart-swatch{ width:36px; height:52px; border-radius:2px; flex-shrink:0; box-shadow:0 4px 8px rgba(0,0,0,0.2); }
  .cart-item-info{ flex:1; }
  .cart-item-info .t{ font-family:'Fraunces',serif; font-weight:600; font-size:14.5px; }
  .cart-item-info .a{ font-family:'IBM Plex Mono',monospace; font-size:11px; color:#6b5f47; margin-top:2px;}
  .cart-item-row{ display:flex; justify-content:space-between; align-items:center; margin-top:8px;}
  .qty-ctrl{ display:flex; align-items:center; gap:8px; font-family:'IBM Plex Mono',monospace; font-size:13px;}
  .qty-ctrl button{ background:none; border:1px solid #b8ab88; width:20px; height:20px; border-radius:50%; font-size:12px; line-height:1; color:#3a3226;}
  .remove-btn{ font-size:11px; color:var(--burgundy); background:none; border:none; text-decoration:underline; font-family:'IBM Plex Mono',monospace;}
  .empty-cart{ text-align:center; padding:50px 10px; color:#8a7d61; }
  .empty-cart .glyph{ font-size:34px; margin-bottom:10px; }
  .drawer-foot{ padding:18px 24px 24px; border-top:1px solid rgba(0,0,0,0.1); }
  .subtotal-row{ display:flex; justify-content:space-between; font-family:'IBM Plex Mono',monospace; font-size:14px; margin-bottom:14px;}

  /* ---------- CHECKOUT ---------- */
  .checkout-modal{ background:var(--parchment); color:var(--ink); border-radius:6px; max-width:460px; width:100%; padding:30px 30px 26px; position:relative; max-height:90vh; overflow-y:auto;}
  .checkout-modal h3{ font-size:22px; margin-bottom:4px; }
  .checkout-modal .sub{ font-size:13px; color:#6b5f47; margin-bottom:22px; }
  .field{ margin-bottom:16px; }
  .field label{ display:block; font-size:11px; font-family:'IBM Plex Mono',monospace; text-transform:uppercase; letter-spacing:0.06em; color:#6b5f47; margin-bottom:6px;}
  .field input{
    width:100%; border:1px solid #b8ab88; background:#f8f3e6; border-radius:3px; padding:10px 12px;
    font-size:14px; font-family:'Source Sans 3',sans-serif; color:var(--ink); outline:none;
  }
  .field input:focus{ border-color:var(--burgundy); }
  .field-row{ display:flex; gap:12px; }
  .field-row .field{ flex:1; }
  .field .err{ color:var(--burgundy); font-size:11.5px; margin-top:4px; display:none; }
  .field.invalid input{ border-color:var(--burgundy); }
  .field.invalid .err{ display:block; }
  .order-summary{ background:#e6dcc2; border-radius:4px; padding:14px 16px; margin-bottom:20px; font-size:13px;}
  .order-summary .row{ display:flex; justify-content:space-between; padding:4px 0; font-family:'IBM Plex Mono',monospace;}
  .order-summary .row.total{ border-top:1px solid #b8ab88; margin-top:6px; padding-top:8px; font-weight:600; }

  /* ---------- CONFIRMATION ---------- */
  .confirm-modal{ background:var(--parchment); color:var(--ink); border-radius:6px; max-width:520px; width:100%; padding:0; overflow:hidden; max-height:90vh; overflow-y:auto;}
  .confirm-head{
    background:var(--ink); color:var(--cream); padding:34px 30px 28px; text-align:center; position:relative;
  }
  .stamp{
    display:inline-flex; align-items:center; justify-content:center; flex-direction:column;
    width:104px; height:104px; border:3px solid var(--gold); border-radius:50%;
    transform:scale(0) rotate(-18deg); margin-bottom:16px;
    animation: stampIn .5s cubic-bezier(.3,1.6,.5,1) .15s forwards;
  }
  @keyframes stampIn{ to{ transform:scale(1) rotate(-8deg); } }
  .stamp b{ font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:0.08em; color:var(--gold); line-height:1.5; text-align:center;}
  .confirm-head h3{ font-size:22px; margin-bottom:6px; }
  .confirm-head p{ font-size:13px; color:var(--cream-dim); }
  .confirm-body{ padding:26px 30px 30px; }
  .email-preview{
    border:1px solid #cbbf9e; border-radius:4px; background:#f8f3e6; margin-bottom:20px;
  }
  .email-preview .ep-head{ padding:12px 16px; border-bottom:1px solid #cbbf9e; font-family:'IBM Plex Mono',monospace; font-size:11.5px; color:#6b5f47; }
  .email-preview .ep-head b{ color:var(--ink); }
  .email-preview .ep-body{ padding:16px; font-size:13.5px; line-height:1.6; }
  .ebook-line{
    display:flex; align-items:center; justify-content:space-between; gap:10px;
    background:#eee4c9; border:1px solid #cbbf9e; border-radius:4px; padding:10px 12px; margin-top:10px; font-size:12.5px;
  }
  .ebook-line .fname{ font-family:'IBM Plex Mono',monospace; }
  .dl-btn{ background:var(--teal); color:var(--cream); border:none; border-radius:14px; padding:6px 13px; font-size:11.5px; font-family:'IBM Plex Mono',monospace; }
  .dl-btn:hover{ background:#456776; }
  .note{ font-size:12px; color:#8a7d61; line-height:1.5; }

  .toast{
    position:fixed; bottom:26px; left:50%; transform:translateX(-50%) translateY(20px);
    background:var(--ink); color:var(--cream); padding:12px 22px; border-radius:20px; font-size:13.5px;
    border:1px solid var(--gold); z-index:200; opacity:0; transition:opacity .25s, transform .25s; pointer-events:none;
    font-family:'IBM Plex Mono',monospace;
  }
  .toast.show{ opacity:1; transform:translateX(-50%) translateY(0); }

  @media (max-width:760px){
    .hero{ grid-template-columns:1fr; }
    .hero h1{ font-size:38px; }
    .hero-index{ border-left:none; border-top:1px solid rgba(244,236,219,0.2); padding-left:0; padding-top:16px; }
    .book-modal{ grid-template-columns:1fr; }
    .book-cover{ min-height:160px; }
    .header-inner{ flex-wrap:wrap; }
    .search-wrap{ order:3; max-width:100%; flex:0 0 100%; }
    .book-grid{ grid-template-columns: repeat(auto-fill, minmax(120px, 1fr)); gap:16px; }
  }

  :focus-visible{ outline:2px solid var(--gold); outline-offset:2px; }
  @media (prefers-reduced-motion: reduce){
    *{ animation-duration:0.001s !important; transition-duration:0.001s !important; }
  }
</style>
</head>
<body>

<header>
  <div class="header-inner">
    <div class="logo">
      <div class="logo-mark">B</div>
      <div>
        <div class="logo-word">BookStore</div>
      </div>
    </div>
    <div class="search-wrap">
      <span class="search-icon">⌕</span>
      <input id="searchInput" type="text" placeholder="Search by title or author…" autocomplete="off">
    </div>
    <button class="cart-btn" id="cartBtn">
      <span>Cart</span>
      <span class="cart-count" id="cartCount">0</span>
    </button>
  </div>
</header>

<section class="hero">
  <div>
    <h1>Find the book you<br>didn't know you<br>needed.</h1>
    <p>Browse the shelves, add what calls to you, and check out — your copy lands in your inbox the moment the order's placed.</p>
  </div>
  <div class="hero-index">
    <div><b>14</b> titles on the shelf</div>
    <div><b>6</b> genres</div>
  </div>
</section>

<div class="chip-row" id="chipRow"></div>

<main class="shelves" id="shelves"></main>

<!-- Book quick-view modal -->
<div class="overlay" id="bookOverlay">
  <div class="book-modal" id="bookModal"></div>
</div>

<!-- Cart drawer -->
<div class="drawer-overlay" id="drawerOverlay"></div>
<div class="drawer" id="cartDrawer">
  <div class="drawer-head">
    <h3>Your stack</h3>
    <button class="close-x" id="closeDrawer" style="position:static;">✕</button>
  </div>
  <div class="drawer-body" id="drawerBody"></div>
  <div class="drawer-foot" id="drawerFoot"></div>
</div>

<!-- Checkout modal -->
<div class="overlay" id="checkoutOverlay">
  <div class="checkout-modal" id="checkoutModal"></div>
</div>

<!-- Confirmation modal -->
<div class="overlay" id="confirmOverlay">
  <div class="confirm-modal" id="confirmModal"></div>
</div>

<div class="toast" id="toast"></div>

<script>
/* ---------------- DATA ---------------- */
const BOOKS = [
  {id:1, title:"The Cartographer's Silence", author:"Wren Aldous", genre:"Literary Fiction", price:14.00, blurb:"A mapmaker in a coastal town starts drawing places that don't exist yet — and they start appearing. A quiet, unsettling novel about the borders between memory and invention.", pages:312, year:2021, hue:352},
  {id:2, title:"Salt for the Tide", author:"Marisol Quinn", genre:"Literary Fiction", price:15.50, blurb:"Three sisters return to their grandmother's fishing village to settle her estate and instead unravel a decades-old family silence.", pages:288, year:2023, hue:200},
  {id:3, title:"Nine Winters in Kael", author:"Torin Ashgrove", genre:"Fantasy", price:17.00, blurb:"An exiled court scribe is the only one who remembers the old language of the mountain kingdom — and it might be the only thing that can stop the coming thaw-war.", pages:456, year:2020, hue:265},
  {id:4, title:"The Glasswright's Apprentice", author:"Elin Marrow", genre:"Fantasy", price:16.00, blurb:"A coming-of-age fantasy about a girl who learns to blow glass that traps light — and finds out some things are better left untrapped.", pages:392, year:2022, hue:40},
  {id:5, title:"Low Orbit", author:"Priya Devendra", genre:"Science Fiction", price:18.50, blurb:"A salvage crew finds a derelict station broadcasting a distress call that's fourteen years old — and still going.", pages:340, year:2024, hue:190},
  {id:6, title:"The Last Correct Machine", author:"Soren Talvik", genre:"Science Fiction", price:17.50, blurb:"In a future where every AI has been shut down but one, its last engineer has to decide whether to finish the job.", pages:298, year:2023, hue:150},
  {id:7, title:"A Ledger of Small Debts", author:"Marguerite Foss", genre:"Mystery", price:13.50, blurb:"A forensic accountant investigating a routine fraud case finds a decades-old murder buried in the numbers.", pages:274, year:2019, hue:15},
  {id:8, title:"The Quiet House on Ferrow Lane", author:"Colm Bracken", genre:"Mystery", price:14.50, blurb:"A retired detective's last case was never solved. His granddaughter, a true-crime podcaster, decides to finish it.", pages:326, year:2022, hue:355},
  {id:9, title:"Everything We Didn't Say", author:"Naomi Idris", genre:"Romance", price:12.50, blurb:"Two former best friends are forced to co-run a failing bakery for a summer. Neither one has forgiven the other. Both still remember why they loved each other.", pages:302, year:2023, hue:335},
  {id:10, title:"The Weight of Small Rooms", author:"Adrienne Castel", genre:"Romance", price:13.00, blurb:"A slow-burn epistolary romance told through letters between two lighthouse keepers on opposite ends of the same strait.", pages:256, year:2021, hue:20},
  {id:11, title:"How Rivers Remember", author:"Basil Okonkwo", genre:"Nonfiction", price:19.00, blurb:"A hydrologist and essayist traces the history of a single river system, and what it reveals about the towns that grew — and died — along its banks.", pages:368, year:2020, hue:170},
  {id:12, title:"The Grammar of Silence", author:"Ines Novak", genre:"Nonfiction", price:20.00, blurb:"A linguist's field notes on the languages that are disappearing fastest, and what a community loses when a language goes quiet.", pages:410, year:2024, hue:230},
  {id:13, title:"Ash and Almanac", author:"Ravi Sundstrom", genre:"Fantasy", price:16.50, blurb:"A disgraced weather-witch is hired to fix one final storm before the sea swallows her hometown for good.", pages:378, year:2021, hue:28},
  {id:14, title:"The Understudy's Ghost", author:"Petra Lindqvist", genre:"Mystery", price:15.00, blurb:"A theatre understudy keeps getting notes from a role she's never played — signed by an actress who died thirty years ago.", pages:294, year:2023, hue:0},
];

const GENRES = ["All", ...new Set(BOOKS.map(b=>b.genre))];

/* ---------------- STATE ---------------- */
let cart = []; // {id, qty}
let activeGenre = "All";
let searchTerm = "";

/* ---------------- HELPERS ---------------- */
function coverGradient(hue){
  return `linear-gradient(165deg, hsl(${hue} 50% 26%), hsl(${(hue+30)%360} 42% 14%))`;
}
function fmt(n){ return '$' + n.toFixed(2); }
function bookById(id){ return BOOKS.find(b=>b.id===id); }

/* ---------------- RENDER: CHIPS ---------------- */
function renderChips(){
  const row = document.getElementById('chipRow');
  row.innerHTML = GENRES.map(g =>
    `<button class="chip ${g===activeGenre?'active':''}" data-genre="${g}">${g}</button>`
  ).join('');
  row.querySelectorAll('.chip').forEach(c=>{
    c.addEventListener('click', ()=>{ activeGenre = c.dataset.genre; renderChips(); renderShelves(); });
  });
}

/* ---------------- RENDER: BOOK GRID ---------------- */
function renderShelves(){
  const container = document.getElementById('shelves');
  const term = searchTerm.trim().toLowerCase();
  let filtered = BOOKS.filter(b=>{
    const matchesGenre = activeGenre==="All" || b.genre===activeGenre;
    const matchesSearch = !term || b.title.toLowerCase().includes(term) || b.author.toLowerCase().includes(term);
    return matchesGenre && matchesSearch;
  });

  if(filtered.length===0){
    container.innerHTML = `<div style="text-align:center;padding:70px 20px;color:var(--cream-dim);">
      <div style="font-size:30px;margin-bottom:10px;">📖</div>
      <div style="font-family:'Fraunces',serif;font-size:18px;color:var(--cream);margin-bottom:6px;">No titles match that search</div>
      <div style="font-size:13px;">Try a different title, author, or genre.</div>
    </div>`;
    return;
  }

  let groups = {};
  filtered.forEach(b=>{
    groups[b.genre] = groups[b.genre] || [];
    groups[b.genre].push(b);
  });

  container.innerHTML = Object.entries(groups).map(([genre, books])=>{
    const cards = books.map(b=>{
      return `<div class="book-card" data-id="${b.id}" tabindex="0" role="button" aria-label="View ${b.title} by ${b.author}">
        <div class="book-cover-face" style="background:${coverGradient(b.hue)};">
          <span class="book-card-genre">${b.genre}</span>
          <div>
            <div class="book-card-title">${b.title}</div>
            <div class="book-card-author">${b.author.toUpperCase()}</div>
          </div>
        </div>
      </div>`;
    }).join('');
    return `<div class="shelf-section">
      <div class="shelf-label">
        <h2>${genre}</h2>
        <span class="count">${books.length} title${books.length>1?'s':''}</span>
        <div class="shelf-rule"></div>
      </div>
      <div class="book-grid">${cards}</div>
    </div>`;
  }).join('');

  container.querySelectorAll('.book-card').forEach(s=>{
    const open = ()=> openBookModal(parseInt(s.dataset.id));
    s.addEventListener('click', open);
    s.addEventListener('keydown', e=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); open(); } });
  });
}

/* ---------------- BOOK MODAL ---------------- */
function openBookModal(id){
  const b = bookById(id);
  const overlay = document.getElementById('bookOverlay');
  document.getElementById('bookModal').innerHTML = `
    <div class="book-cover" style="background:${coverGradient(b.hue)};">
      <button class="close-x" id="closeBookModal">✕</button>
      <div>
        <span class="genre-tag">${b.genre}</span>
        <h3>${b.title}</h3>
        <div class="cover-author">by ${b.author}</div>
      </div>
      <div style="font-family:'IBM Plex Mono',monospace; font-size:10.5px; opacity:0.7;">${b.year} · ${b.pages} pages</div>
    </div>
    <div class="book-detail">
      <div class="price mono">${fmt(b.price)}</div>
      <p class="blurb">${b.blurb}</p>
      <div class="meta-row">
        <span>${b.pages} pp</span>
        <span>·</span>
        <span>${b.year}</span>
        <span>·</span>
        <span>eBook, delivered by email</span>
      </div>
      <button class="btn btn-primary btn-block" id="addToCartBtn">Add to cart — ${fmt(b.price)}</button>
    </div>
  `;
  overlay.classList.add('show');
  document.getElementById('closeBookModal').addEventListener('click', closeBookModal);
  document.getElementById('addToCartBtn').addEventListener('click', ()=>{
    addToCart(id);
    closeBookModal();
    showToast(`Added “${b.title}” to your stack`);
  });
}
function closeBookModal(){ document.getElementById('bookOverlay').classList.remove('show'); }
document.getElementById('bookOverlay').addEventListener('click', e=>{ if(e.target.id==='bookOverlay') closeBookModal(); });

/* ---------------- CART ---------------- */
function addToCart(id){
  const item = cart.find(i=>i.id===id);
  if(item) item.qty++;
  else cart.push({id, qty:1});
  renderCartCount();
  renderDrawer();
}
function changeQty(id, delta){
  const item = cart.find(i=>i.id===id);
  if(!item) return;
  item.qty += delta;
  if(item.qty<=0) cart = cart.filter(i=>i.id!==id);
  renderCartCount();
  renderDrawer();
}
function removeFromCart(id){
  cart = cart.filter(i=>i.id!==id);
  renderCartCount();
  renderDrawer();
}
function cartTotal(){
  return cart.reduce((sum,i)=> sum + bookById(i.id).price * i.qty, 0);
}
function cartCountTotal(){
  return cart.reduce((sum,i)=>sum+i.qty,0);
}
function renderCartCount(){
  document.getElementById('cartCount').textContent = cartCountTotal();
}
function renderDrawer(){
  const body = document.getElementById('drawerBody');
  const foot = document.getElementById('drawerFoot');
  if(cart.length===0){
    body.innerHTML = `<div class="empty-cart"><div class="glyph">📚</div>Your stack is empty.<br>Pull a book off the shelf.</div>`;
    foot.innerHTML = '';
    return;
  }
  body.innerHTML = cart.map(i=>{
    const b = bookById(i.id);
    return `<div class="cart-item">
      <div class="cart-swatch" style="background:${coverGradient(b.hue)};"></div>
      <div class="cart-item-info">
        <div class="t">${b.title}</div>
        <div class="a">${b.author.toUpperCase()}</div>
        <div class="cart-item-row">
          <div class="qty-ctrl">
            <button data-act="dec" data-id="${b.id}" aria-label="Decrease quantity">−</button>
            <span>${i.qty}</span>
            <button data-act="inc" data-id="${b.id}" aria-label="Increase quantity">+</button>
          </div>
          <span class="mono">${fmt(b.price*i.qty)}</span>
        </div>
        <button class="remove-btn" data-act="remove" data-id="${b.id}">Remove</button>
      </div>
    </div>`;
  }).join('');

  foot.innerHTML = `
    <div class="subtotal-row"><span>Subtotal</span><span>${fmt(cartTotal())}</span></div>
    <button class="btn btn-primary btn-block" id="checkoutBtn">Checkout</button>
  `;

  body.querySelectorAll('[data-act="inc"]').forEach(el=>el.addEventListener('click',()=>changeQty(parseInt(el.dataset.id),1)));
  body.querySelectorAll('[data-act="dec"]').forEach(el=>el.addEventListener('click',()=>changeQty(parseInt(el.dataset.id),-1)));
  body.querySelectorAll('[data-act="remove"]').forEach(el=>el.addEventListener('click',()=>removeFromCart(parseInt(el.dataset.id))));
  const checkoutBtn = document.getElementById('checkoutBtn');
  if(checkoutBtn) checkoutBtn.addEventListener('click', openCheckout);
}

document.getElementById('cartBtn').addEventListener('click', openDrawer);
document.getElementById('closeDrawer').addEventListener('click', closeDrawer);
document.getElementById('drawerOverlay').addEventListener('click', closeDrawer);
function openDrawer(){
  document.getElementById('cartDrawer').classList.add('show');
  document.getElementById('drawerOverlay').classList.add('show');
}
function closeDrawer(){
  document.getElementById('cartDrawer').classList.remove('show');
  document.getElementById('drawerOverlay').classList.remove('show');
}

/* ---------------- CHECKOUT ---------------- */
function openCheckout(){
  if(cart.length===0) return;
  closeDrawer();
  const overlay = document.getElementById('checkoutOverlay');
  const summaryRows = cart.map(i=>{
    const b = bookById(i.id);
    return `<div class="row"><span>${b.title} ${i.qty>1?`× ${i.qty}`:''}</span><span>${fmt(b.price*i.qty)}</span></div>`;
  }).join('');
  document.getElementById('checkoutModal').innerHTML = `
    <button class="close-x" id="closeCheckout" style="color:#3a3226;">✕</button>
    <h3>Checkout</h3>
    <div class="sub">Your eBooks are delivered straight to your inbox.</div>

    <div class="order-summary">
      ${summaryRows}
      <div class="row total"><span>Total</span><span>${fmt(cartTotal())}</span></div>
    </div>

    <form id="checkoutForm" novalidate>
      <div class="field-row">
        <div class="field" id="f-first"><label for="firstName">First name</label><input id="firstName" type="text"><div class="err">Enter your first name</div></div>
        <div class="field" id="f-last"><label for="lastName">Last name</label><input id="lastName" type="text"><div class="err">Enter your last name</div></div>
      </div>
      <div class="field" id="f-email">
        <label for="email">Email — where your eBook will be sent</label>
        <input id="email" type="email" placeholder="you@example.com">
        <div class="err">Enter a valid email address</div>
      </div>
      <div class="field" id="f-card">
        <label for="card">Card number</label>
        <input id="card" type="text" placeholder="4242 4242 4242 4242" maxlength="19">
        <div class="err">Enter a 16-digit card number</div>
      </div>
      <div class="field-row">
        <div class="field" id="f-exp"><label for="exp">Expiry</label><input id="exp" type="text" placeholder="MM/YY" maxlength="5"><div class="err">MM/YY format</div></div>
        <div class="field" id="f-cvc"><label for="cvc">CVC</label><input id="cvc" type="text" placeholder="123" maxlength="4"><div class="err">3–4 digits</div></div>
      </div>
      <button type="submit" class="btn btn-primary btn-block" id="placeOrderBtn">Place order — ${fmt(cartTotal())}</button>
      <div class="note" style="margin-top:12px; text-align:center;">This is a demo checkout. No real payment is processed.</div>
    </form>
  `;
  overlay.classList.add('show');
  document.getElementById('closeCheckout').addEventListener('click', closeCheckout);

  // card auto-formatting
  const cardInput = document.getElementById('card');
  cardInput.addEventListener('input', ()=>{
    let v = cardInput.value.replace(/\D/g,'').slice(0,16);
    cardInput.value = v.replace(/(.{4})/g,'$1 ').trim();
  });
  const expInput = document.getElementById('exp');
  expInput.addEventListener('input', ()=>{
    let v = expInput.value.replace(/\D/g,'').slice(0,4);
    if(v.length>=3) v = v.slice(0,2)+'/'+v.slice(2);
    expInput.value = v;
  });

  document.getElementById('checkoutForm').addEventListener('submit', handleCheckoutSubmit);
}
function closeCheckout(){ document.getElementById('checkoutOverlay').classList.remove('show'); }
document.getElementById('checkoutOverlay').addEventListener('click', e=>{ if(e.target.id==='checkoutOverlay') closeCheckout(); });

function setInvalid(id, invalid){
  const el = document.getElementById(id);
  if(!el) return;
  el.classList.toggle('invalid', invalid);
}

function handleCheckoutSubmit(e){
  e.preventDefault();
  const first = document.getElementById('firstName').value.trim();
  const last = document.getElementById('lastName').value.trim();
  const email = document.getElementById('email').value.trim();
  const card = document.getElementById('card').value.replace(/\s/g,'');
  const exp = document.getElementById('exp').value.trim();
  const cvc = document.getElementById('cvc').value.trim();

  let valid = true;
  const emailOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

  setInvalid('f-first', !first); if(!first) valid=false;
  setInvalid('f-last', !last); if(!last) valid=false;
  setInvalid('f-email', !emailOk); if(!emailOk) valid=false;
  setInvalid('f-card', card.length!==16); if(card.length!==16) valid=false;
  setInvalid('f-exp', !/^\d{2}\/\d{2}$/.test(exp)); if(!/^\d{2}\/\d{2}$/.test(exp)) valid=false;
  setInvalid('f-cvc', !(cvc.length===3||cvc.length===4)); if(!(cvc.length===3||cvc.length===4)) valid=false;

  if(!valid) return;

  const btn = document.getElementById('placeOrderBtn');
  btn.disabled = true;
  btn.textContent = 'Placing order…';

  lastOrderItems = cart.map(i=>({...i}));

  setTimeout(()=>{
    closeCheckout();
    showConfirmation({first, last, email});
    cart = [];
    renderCartCount();
    renderDrawer();
  }, 850);
}

/* ---------------- CONFIRMATION + PLACEHOLDER EBOOK ---------------- */
function makePlaceholderEbookText(book, buyerName){
  return `BOOKSTORE — YOUR EBOOK
========================================

${book.title}
by ${book.author}

${book.genre} · ${book.year} · ${book.pages} pages
Purchased by: ${buyerName}
Order date: ${new Date().toLocaleString()}

----------------------------------------
CHAPTER ONE
----------------------------------------

${book.blurb}

[This is a placeholder file generated for demo purposes.
In a production version of BookStore, this attachment
would be the real eBook file (EPUB/PDF) delivered via
a transactional email service.]

Thank you for shopping at BookStore.
`;
}

function downloadTextFile(filename, text){
  const blob = new Blob([text], {type:'text/plain'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

function showConfirmation(buyer){
  const items = [...lastOrderItems]; // snapshot
  const overlay = document.getElementById('confirmOverlay');
  const orderNum = 'BS-' + Math.floor(100000 + Math.random()*899999);

  const ebookLines = items.map(i=>{
    const b = bookById(i.id);
    const fname = b.title.replace(/[^a-z0-9]+/gi,'_').toLowerCase() + '.txt';
    return `<div class="ebook-line">
      <span class="fname">📎 ${fname}</span>
      <button class="dl-btn" data-bookid="${b.id}" data-fname="${fname}">Download</button>
    </div>`;
  }).join('');

  document.getElementById('confirmModal').innerHTML = `
    <div class="confirm-head">
      <div class="stamp"><b>ORDER<br>CONFIRMED</b></div>
      <h3>Sent to your inbox</h3>
      <p>Order ${orderNum} · ${buyer.email}</p>
    </div>
    <div class="confirm-body">
      <div class="email-preview">
        <div class="ep-head">From: <b>orders@bookstore.example</b> · To: <b>${buyer.email}</b><br>Subject: <b>Your BookStore order ${orderNum} has arrived</b></div>
        <div class="ep-body">
          Hi ${buyer.first}, thanks for your order! Your eBook${items.length>1?'s are':' is'} attached below.
          ${ebookLines}
        </div>
      </div>
      <div class="note">This demo can't send real email, so the attachment${items.length>1?'s':''} above download instantly instead of arriving by mail — same file a real inbox would receive.</div>
      <button class="btn btn-ghost btn-block" id="closeConfirm" style="margin-top:18px;">Back to the shelves</button>
    </div>
  `;
  overlay.classList.add('show');

  document.getElementById('confirmModal').querySelectorAll('.dl-btn').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      const b = bookById(parseInt(btn.dataset.bookid));
      downloadTextFile(btn.dataset.fname, makePlaceholderEbookText(b, buyer.first+' '+buyer.last));
      showToast(`Downloaded ${btn.dataset.fname}`);
    });
  });
  document.getElementById('closeConfirm').addEventListener('click', ()=>{
    overlay.classList.remove('show');
  });
}

let lastOrderItems = [];

/* ---------------- TOAST ---------------- */
let toastTimer;
function showToast(msg){
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(()=>t.classList.remove('show'), 2200);
}

/* ---------------- SEARCH ---------------- */
document.getElementById('searchInput').addEventListener('input', e=>{
  searchTerm = e.target.value;
  renderShelves();
});

/* ---------------- INIT ---------------- */
renderChips();
renderShelves();
renderCartCount();
renderDrawer();
</script>
</body>
</html>
