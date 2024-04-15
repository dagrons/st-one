# TODO

- ConversationalRetrievalChain
- m3e-base
- 如何实现高并发

# 离线部署

先在本地成功跑通，然后导出依赖下载pkg，打包传到内网部署

- pkgs
- dagrons.tar.gz(py310初始环境)
- one.tar.gz(源码)
- terseract, poppler(for pdf extraction)
- Qwen1.5(1.8B,7B,14B), ChatGLM3(6B), MiniCPM(2B)
- nltk\_data
- paraphrase-MiniLM-L6-v2

# 在线部署

- git clone one
- pip install -r requirements.txt
- aDrive上传llm model(Qwen1.5-0.5b-chat), embedding(m3e-base), nltk_data



# 隐藏Deploy Button和MainMenu

```python
st.markdown(r"""
<style>
   .stDeployButton{
           visibility: hidden
   }
   #MainMenu {
           visibility: hidden
   }
</style>

""", unsafe_allow_html=True)
```

# LLM APP

就是用Prompt作为功能实现，每个Prompt对应了一个函数

在传统App中，我们用代码实现功能，在LLM APP中，我们用Prompt描述输入输出即可


