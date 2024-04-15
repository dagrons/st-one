# TODO

- ConversationalRetrievalChain
- m3e-base
- 如何实现高并发

# 离线部署清单

先在本地成功跑通，然后导出依赖下载pkg，打包传到内网部署

- one.tar.gz
- nltk\_data.tar.gz
- m3e-base.tar.gz
- llm-models
- dagrons.tar.gz(py310初始环境)
- pkgs.tar.gz

# 在线部署清单

导入到aDrive，再通过aDrive下载到在线环境，更新最频繁的代码可以通过github更新

- one.tar.gz
- nltk.tar.gz
- m3e-base.tar.gz
- llm models


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


