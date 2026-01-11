import streamlit as st
import random
st.set_page_config(
    page_title="人生！運試しおみくじ",
    page_icon="🧧",
    layout="centered"
)
st.title("🔥 人生！運試しおみくじ 🔥")

# --- 【プロの小技】ボタンを金色にする魔法（CSS） ---
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #FFD700; /* 金色 */
        color: #000000;           /* 文字は黒で読みやすく */
        border-radius: 10px;      /* 角を少し丸く */
        border: 2px solid #DAA520; /* 縁取り */
        font-weight: bold;        /* 太字 */
        height: 3em;
        width: 100%;              /* 横幅いっぱい */
    }
    div.stButton > button:hover {
        background-color: #FFA500; /* カーソルを乗せたらオレンジっぽく光る */
        color: #FFFFFF;
    }
    </style>
    """, unsafe_allow_html=True)

useless_advices = [
    "靴下は右から履くと、右から履いたことになります。",
    "昨日の次は、だいたい今日が来ます。",
    "右に曲がれない時は、左に3回曲がれば右に行けます。", # ここにカンマを忘れずに！
    "雨の日に傘をささないと、だいたい濡れます。", # 新しく追加
    "パンはパンでも、食べられるパンは普通のパンです。", # 新しく追加
    "急いでいる時に走ると、歩くより早く着く可能性があります。", # どんどん増やしてOK！
    "てか、五条悟って誰？え？五条勝？",
    "パンが無ければ、ひじの先っちょのカサカサのところを反対の手のひらで温めて、ちょっと右斜め上を眺めながら舌を出して足首を軽く回したらいいじゃない。"
]
insults = ["それでいいの？w", "人生、そんなに甘くないよw", "出直し確定ですw"]

query_params = st.query_params
shared_num = query_params.get("num")

def display_result(num):
    advice = useless_advices[num % len(useless_advices)]
    if num >= 70:
        st.error(f"出た数字: {num}")
        st.markdown(f"# {insults[num % len(insults)]}")
    elif num == 1:
        st.balloons()
        st.success(f"出た数字: {num}")
        st.markdown("# 🌈 最高の人生 🌈")
    elif 2 <= num <= 20:
        st.info(f"出た数字: {num}")
        st.markdown("## 📈 絶好調 📈")
    else:
        st.warning(f"出た数字: {num}")
        st.markdown("## 😑 平凡な人生ﾍｲﾍｲ 😑")
    
    st.info(f"💡 助言：\n{advice}")

if shared_num:
    st.write("--- 友達からの共有結果 ---")
    display_result(int(shared_num))
    if st.button("自分も占う"):
        st.query_params.clear()
        st.rerun()
else:
    # 【変更】ボタンの文字を「おみくじを引く」に変更
    if st.button("🧧 おみくじを引く"):
        num = random.randint(1, 100)
        display_result(num)
        
        st.write("---")
        st.write("🔗 この【結果URL】をDiscordに貼って友達を煽ろう！")
        
        base_url = "https://my-omikuji-app-rrjeeuxyemsppmr3oveugp.streamlit.app" 
        full_share_url = f"{base_url}/?num={num}"
        
        st.code(full_share_url)






