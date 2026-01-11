import streamlit as st
import random

st.title("🔥 人生！運試しおみくじ 🔥")

useless_advices = [
    "靴下は右から履くと、右から履いたことになります。",
    "昨日の次は、だいたい今日が来ます。",
    "右に曲がれない時は、左に3回曲がれば右に行けます。"
]
insults = ["その決断でいいの？w", "人生、そんなに甘くないよw", "出直し確定ですw"]

# URLからデータを読み取る
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
        st.markdown("## 😑 平凡な人生 😑")
    
    st.info(f"💡 助言：\n{advice}")

if shared_num:
    st.write("--- 友達からの共有結果 ---")
    display_result(int(shared_num))
    if st.button("自分も占う"):
        st.query_params.clear()
        st.rerun()
else:
    if st.button("運命の決断を下す"):
        num = random.randint(1, 100)
        display_result(num)
        
        st.write("---")
        st.write("🔗 この【結果URL】をDiscordに貼って友達を煽ろう！")
        
        # 【ここを改善！】今のURLを自動で取得して、末尾に数字をくっつける
        # GitHubのPagesやStreamlit CloudのURLを想定しています
        base_url = "https://your-app-name.streamlit.app" # ← ここを自分のアプリのURLに書き換えてください
        full_share_url = f"{base_url}/?num={num}"
        
        st.code(full_share_url) # これで完成したURLがコピー可能な状態で表示されます！
