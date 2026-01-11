def display_result(num):
    advice = useless_advices[num % len(useless_advices)]
    
    if num >= 70:
        # 煽りのとき
        st.error(f"出た数字: {num}")
        st.markdown(f"# {insults[num % len(insults)]}")
        # 💡 ここに助言を移動！煽りの時だけ表示されるようになります
        st.info(f"💡 助言：\n{advice}")
        
    elif num == 1:
        st.balloons()
        st.success(f"出た数字: {num}")
        st.markdown("# 🌈 最高の人生 🌈")
        # ここから下の st.info は消しました
        
    elif 2 <= num <= 20:
        st.info(f"出た数字: {num}")
        st.markdown("## 📈 絶好調 📈")
        
    else:
        st.warning(f"出た数字: {num}")
        st.markdown("## 😑 平凡な人生ﾍｲﾍｲ 😑")
