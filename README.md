### 离线部署清单

先在本地成功跑通，然后导出依赖下载pkg，打包传到内网部署

- one.tar.gz
- nltk\_data.tar.gz
- m3e-base.tar.gz
- llm-models
- dagrons.tar.gz(py310初始环境)
- pkgs.tar.gz

### 在线部署清单

导入到aDrive，再通过aDrive下载到在线环境，更新最频繁的代码可以通过github更新

- one.tar.gz
- nltk.tar.gz
- m3e-base.tar.gz
- llm models


### 隐藏Deploy Button和MainMenu

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

### pyvista环境(wsl)

```bash
apt install -y libglu1 \
libxcursor-dev \
libxft2 \
libxinerama1 \
libfltk1.3-dev \ 
libfreetype6-dev  \
libgl1-mesa-dev \
libocct-foundation-dev \
libocct-data-exchange-dev 

ln -s ln -s /usr/lib/x86_64-linux-gnu/swrast_dri.so /usr/lib/dri/swrast_dri.so

conda install -c conda-forge gcc=12.1.0
```
