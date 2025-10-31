import streamlit as st

# ----------------- CONFIG -----------------
st.set_page_config(
    page_title="Târgul de Cai Măgura - Blue Christmas 2025",
    page_icon="🐎",
    layout="wide"
)

# ----------------- STIL ALBASTRU -----------------
st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #0d1b2a 0%, #000814 100%);
    color: #e0f7fa;
    font-family: 'Poppins', sans-serif;
}
h1, h2, h3 {
    color: #64b5f6;
    text-shadow: 0 0 20px #00bcd4;
}
.block {
    background-color: rgba(255,255,255,0.08);
    padding: 1.5rem;
    border-radius: 15px;
    box-shadow: 0 0 25px rgba(0,188,212,0.3);
    backdrop-filter: blur(6px);
}
a {
    color: #82e9de;
    text-decoration: none;
}
hr {
    border: 1px solid #64b5f6;
}
.snow {
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background-image: url('https://cdn.pixabay.com/photo/2017/12/27/15/30/snow-3041659_960_720.png');
  background-repeat: repeat;
  background-size: contain;
  opacity: 0.25;
  animation: snow 60s linear infinite;
  z-index: -1;
}
@keyframes snow {
  0% {background-position: 0 0;}
  100% {background-position: 500px 1000px;}
}
.lights {
  position: fixed;
  top: 0; left: 0;
  width: 100%; text-align: center;
  font-size: 24px;
  animation: pulse 2s infinite alternate;
  z-index: 1;
}
@keyframes pulse {
  0%,100% {opacity: 1;}
  50% {opacity: 0.6;}
}
.lights span {
  margin: 0 5px;
  color: #03a9f4;
  text-shadow: 0 0 15px #80deea;
}
.buy-button {
  display: inline-block;
  background: linear-gradient(45deg, #0288d1, #00acc1);
  color: white;
  font-size: 20px;
  font-weight: bold;
  padding: 15px 40px;
  border-radius: 40px;
  text-decoration: none;
  transition: all 0.3s ease;
  box-shadow: 0 0 20px #00bcd4;
}
.buy-button:hover {
  transform: scale(1.1);
  box-shadow: 0 0 40px #82e9de;
}
</style>

<div class="lights">
  <span>💡</span><span>❄️</span><span>⭐</span><span>💙</span><span>✨</span><span>❄️</span>
</div>

<div class="snow"></div>
""", unsafe_allow_html=True)

# ----------------- FUNDAL MUZICAL -----------------
st.markdown("""
<audio autoplay loop>
  <source src="https://www.dropbox.com/scl/fi/8pmy1hvz52tzc1p/Marut-Margaritar.mp3?rlkey=xyz123abc&raw=1" type="audio/mpeg">
</audio>
""", unsafe_allow_html=True)

# ----------------- HEADER -----------------
st.title("💙🐎 TÂRGUL DE CAI MĂGURA – BLUE CHRISTMAS EDITION ❄️")
st.subheader("Crăciunul prinde viață la poalele Măgurii – în tonuri de gheață și lumină!")
st.markdown("---")

# ----------------- DESPRE EVENIMENT -----------------
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    <div class='block'>
    <p style='font-size:18px;'>
    🐴 <b>Târgul de Cai Măgura</b> devine în acest an un spectacol al iernii albastre!  
    Luminile reci se împletesc cu sunetul potcoavelor, mirosul de vin fiert și colindele din zare.  
    <br><br>
    Fie că vii pentru parade, muzică sau doar pentru atmosfera feerică, te așteptăm să sărbătorim împreună Crăciunul 2025!
    </p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("https://cdn.pixabay.com/photo/2018/01/24/18/43/horse-3103440_960_720.jpg",
             caption="Cai în zăpadă la Măgura – ediția albastră", use_container_width=True)

st.markdown("---")

# ----------------- DETALII -----------------
st.header("📅 Detalii de desfășurare")
c1, c2, c3 = st.columns(3)
c1.metric("🗓️ Start", "15 decembrie 2025")
c2.metric("🎁 Final", "17 decembrie 2025")
c3.metric("📍 Locație", "Măgura, jud. Buzău")

st.markdown("---")

# ----------------- LINEUP -----------------
st.header("🎶 Line-up Special")
st.markdown("""
<div style='display:flex; gap:2rem; flex-wrap:wrap; justify-content:center;'>
  <div class='block' style='flex:1; min-width:250px;'>
    <h3>🌹 Maria Lătărețu</h3>
    <p>Colinde autentice, nostalgie și emoție pură românească.</p>
  </div>
  <div class='block' style='flex:1; min-width:250px;'>
    <h3>🥁 Frații Țambal</h3>
    <p>Sunetul tradiției, reinterpretat în note moderne de iarnă.</p>
  </div>
  <div class='block' style='flex:1; min-width:250px;'>
    <h3>🔥 Vali Vijelie</h3>
    <p>Petrecere albastră – dans, energie și bucurie în noaptea de Crăciun!</p>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ----------------- PROGRAM -----------------
st.header("🕯️ Programul complet")
colA, colB = st.columns(2)
with colA:
    st.markdown("""
    <div class='block'>
    <h3>🎅 Vineri – 15 Decembrie</h3>
    <ul>
      <li>10:00 – Parada cailor îmbrăcați de Crăciun</li>
      <li>14:00 – Concurs „Cel mai frumos cal” 🐎</li>
      <li>18:00 – Colinde cu <b>Maria Lătărețu</b></li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
with colB:
    st.markdown("""
    <div class='block'>
    <h3>🎁 Sâmbătă – 16 Decembrie</h3>
    <ul>
      <li>11:00 – Târg de produse tradiționale</li>
      <li>15:00 – Frații Țambal în concert</li>
      <li>20:00 – Vali Vijelie Live Show 💃</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class='block' style='margin-top:1rem;'>
<h3>🌟 Duminică – 17 Decembrie</h3>
<ul>
  <li>12:00 – Premierea participanților</li>
  <li>17:00 – Concert final și foc de artificii albastre 🎆</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ----------------- BUTON BILET -----------------
st.header("🎟️ Rezervă-ți locul la Blue Christmas!")
st.markdown("""
<div style='text-align:center; margin-top:20px;'>
  <a href='https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1' target='_blank' class='buy-button'>
    💙 CUMPĂRĂ BILET ACUM 💙
  </a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ----------------- CONTACT -----------------
st.header("📞 Informații & Contact")
colC, colD = st.columns([1,2])
with colC:
    st.image("https://cdn.pixabay.com/photo/2017/03/02/05/17/horse-2111351_960_720.jpg",
             caption="Măgura iarna – liniște și eleganță", use_container_width=True)
with colD:
    st.markdown("""
    <div class='block'>
    <p>📧 <b>Email:</b> targuldecaimaguraofficial@gmail.com<br>
    📱 <b>Telefon:</b> 0723 902 160<br>
    💬 <b>Instagram:</b> <a href='https://www.instagram.com/targuldecaimagura'>/targuldecaimagura</a></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;'>💙❄️ Crăciun albastru fericit de la Târgul de Cai Măgura! 🐎✨</h2>", unsafe_allow_html=True)
st.snow()

# ---- SCRIPT AUDIO ----
st.markdown("""
<script>
var audio = null;
function toggleMusic() {
    if (!audio) {
        audio = new Audio("https://www.dropbox.com/s/abc123xyz/Marut-Margaritar.mp3?raw=1");
        audio.loop = true;
        audio.volume = 0.7;
    }
    if (audio.paused) {
        audio.play();
        alert("🎶 Muzica a pornit: Mărut Mărgăritar");
    } else {
        audio.pause();
        alert("🔇 Muzica a fost oprită");
    }
}
</script>

<div style="text-align:center;">
    <button onclick="toggleMusic()">🔊 Pornește / Oprește Muzica</button>
</div>
""", unsafe_allow_html=True)