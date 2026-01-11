import streamlit as st
import random

# --- ページ設定 ---
st.set_page_config(
    page_title="人生！運試しおみくじ",
    page_icon="🧧",
    layout="centered"
)

# --- 背景とボタンのデザイン（CSS） ---
st.markdown("""
 
    
    /* タイトルなどの文字を読みやすく白にする */
    h1, h2, h3, p, span {
        color: #ffffff !important;
    }

    /* ボタンのデザイン */
    div.stButton > button {
        background-color: #FFD700; 
        color: #000000;
        border-radius: 10px;
        border: 2px solid #DAA520;
        font-weight: bold;
        height: 3em;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #FFA500;
        color: #FFFFFF;
    }

    /* 共有用コードブロックの背景を見やすく */
    code {
        color: #fffdde !important;
        background-color: #4a1d05 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 人生！運試しおみくじ 🔥")

# --- 役に立たない助言リスト ---
useless_advices = [
    "靴下は右から履くと、右から履いたことになります。",
    "昨日の次は、だいたい今日が来ます。",
    "右に曲がれない時は、左に3回曲がれば右に行けます。",
    "雨の日に傘をささないと、だいたい濡れます。",
    "パンはパンでも、食べられるパンは普通のパンです。",
    "急いでいる時に走ると、歩くより早く着く可能性があります。",
    "てか、五条悟って誰？え？五条勝？",
    "パンが無ければ、ひじの先っちょのカサカサのところを反対の手のひらで温めて、ちょっと右斜め上を眺めながら舌を出して足首を軽く回したらいいじゃない。"
]

# --- 煽り文句リスト ---
insults = ["凶　それでいいの？w", "凶　人生、そんなに甘くないよw", "凶　出直し確定ですw"]

# --- URL共有機能 ---
query_params = st.query_params
shared_num = query_params.get("num")

def display_result(num):
    advice = useless_advices[num % len(useless_advices)]
    
    if num >= 70:
        st.error(f"出た数字: {num}")
        st.markdown(f"# {insults[num % len(insults)]}")
        st.info(f"💡 助言：\n{advice}")
    elif num == 1:
        st.balloons()
        st.success(f"出た数字: {num}")
        st.markdown("# 🌈 大吉　最高の人生 🌈")
    elif 2 <= num <= 20:
        st.info(f"出た数字: {num}")
        st.markdown("## 📈 中吉　絶好調 📈")
    else:
        st.warning(f"出た数字: {num}")
        st.markdown("## 😑 吉　平凡な人生ﾍｲﾍｲ 😑")

# --- メインロジック ---
if shared_num:
    st.write("--- 友達からの共有結果 ---")
    display_result(int(shared_num))
    if st.button("自分も占う"):
        st.query_params.clear()
        st.rerun()
else:
    if st.button("🧧 おみくじを引く"):
        num = random.randint(1, 100)
        display_result(num)
        
        st.write("---")
        st.write("🔗 この【結果URL】をDiscordに貼って友達を煽ろう！")
        
        base_url = "https://my-omikuji-app-rrjeeuxyemsppmr3oveugp.streamlit.app" 
        full_share_url = f"{base_url}/?num={num}"
        st.code(full_share_url)

