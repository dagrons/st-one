# TODO

- 如何实现高并发

# 离线部署清单

- pkgs
- dagrons.tar.gz(py310初始环境)
- one.tar.gz(源码)
- terseract, poppler(for pdf extraction)
- Qwen1.5(1.8B,7B,14B), ChatGLM3(6B), MiniCPM(2B)
- nltk\_data
- paraphrase-MiniLM-L6-v2


## 隐藏Deploy Button和MainMenu

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

""", unsafe_allow_html=True

)
```
