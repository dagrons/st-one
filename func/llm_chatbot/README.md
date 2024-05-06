# before day 0

## 需求分析

知识库外挂，SUPPORTED_EMB_MODEL + SUPPORTED_VECTORDB
client_agent，在浏览器中聊天时，streamlit能获用户ip吗？如果可以，就能在服务端下发指令让client_agent执行

## 技术选型

### 前端streamlit

### 后端fastapi+langchain+sqlarchemy

无状态, asyncio

streamlit + fastapi的方式，对前端只用暴露一个端口

# day0 - 页面开发

聊天页面 - llm_chatbot

助手页面 - llm_agent
> llm agent只能是特殊领域的agent，比如sql查询，表格查询，计算等，而且对小模型效果并不是很好
> 
检索页面 - retrieval

# day1 - 接口设计

/chat
/stream_chat
/agent_chat
/agent_stream_chat
/list_llm
/list_emb
/get_emb_vector
/list_kg_db
/search_kg_db

# day2 - 后端接口层

只有把后端接口定下来，才知道后端有哪些分层




