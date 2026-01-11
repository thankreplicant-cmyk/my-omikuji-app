import streamlit as st
import random

# --- 設定 ---
st.title("🔥 人生！運試しおみくじ 🔥")

useless_advices = [
    "靴下は右から履くと、右から履いたことになります。",
    "昨日の次は、だいたい今日が来ます。",
    "右に曲がれない時は、左に3回曲がれば右に行けます。"
]
insults = ["その決断でいいの？w", "人生、そんなに甘くないよw", "出直し確定ですw"]

# --- URLからデータを読み取る (クエリパラメータ) ---
query_params = st.query_params
shared_num = query_params.get("num") # URLに ?num=XX があれば取得

# --- 表示用関数 (共通化) ---
def display_result(num):
    advice = useless_advices[num % len(useless_advices)] # 数字から固定のアドバイスを導く
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
        st.markdown("## 😑 平凡な人生 😑")
    
    st.info(f"💡 助言：\n{advice}")
    return advice

# --- メイン処理 ---
if shared_num:
    # 共有URLから来た場合
    st.write("--- 友達からの共有結果 ---")
    display_result(int(shared_num))
    if st.button("自分も占う"):
        st.query_params.clear() # URLを綺麗にしてリロード
        st.rerun()
else:
    # 普通に占う場合
    if st.button("運命の決断を下す"):
        num = random.randint(1, 100)
        display_result(num)
        
        # 共有用URLの作成
        # 例: https://your-app.streamlit.app/?num=42
        st.write("---")
        st.write("🔗 この結果を友達にシェアする")
        share_url = f"https://{st.get_option('server.address')}/?num={num}" # 本来は手動でURLを足すのが確実
        st.code(f"今のURLの末尾にこれを足して送ってね： ?num={num}")
