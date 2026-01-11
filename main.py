import streamlit as st
import random

# アプリのタイトル
st.title("🔥 煽り全開！運試しおみくじ 🔥")

# 煽り文句のリスト
insults = [
    "ドンマイw", 
    "え、本気？w", 
    "逆にすごw", 
    "明日から本気出そうかw", 
    "お疲れ様でした（笑）"
]

# 友達が押すボタン
if st.button("おみくじを引く"):
    # 1/3の確率で煽りモード
    if random.randint(1, 3) == 1:
        message = random.choice(insults)
        st.error(f"【悲報】{message}")
    else:
        # 通常のおみくじ
        num = random.randint(1, 100)
        if num == 1:
            st.balloons() # 演出：風船を飛ばす
            st.success(f"数字: {num} ✨超大吉✨")
        elif 2 <= num <= 20:
            st.info(f"数字: {num} 🌸大吉🌸")
        else:
            st.write(f"数字: {num} 結果: 普通")
