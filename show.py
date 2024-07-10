import streamlit as st
from main import xiaohongshu_generate
import os
with st.sidebar:
    openai_key=st.text_input("请输入你的OpenAI_API密钥:",type="password")
    st.markdown("[如何获取API密钥？](https://www.baidu.com/)")
st.title("爆款小红书AI写作助手✏️")
st.divider()
subject=st.text_input("请输入您要撰写的主题:")
clicked=st.button('开始写作✍️')
if clicked:
    if openai_key=='':
        st.info("请输入OpenAI 密钥")
        st.stop()
    elif subject=='':
        st.info("请输入你想要输入的主题")
        st.stop()
    else:
        with st.spinner("AI文本正在生成中..."):
            try:
                result= xiaohongshu_generate(subject,openai_key)
            except:
                st.info(":red[请输入正确的OpenAI API密钥]")
                st.info("写作中断")
                exit()
                st.stop()
        st.success("文本已生成🙌")
        st.write('我推荐的小标题为：\n')
        for title in result.title:
            st.write(f'{title}\n')
        st.write(f'正文文本为：\n{result.context}')