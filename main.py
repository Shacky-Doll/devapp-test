import streamlit as st
import numpy as np
import pandas as pd
import time

st.title("Streamlit 超入門")

st.write("DataFrame")

df = pd.DataFrame({
    "1列目" : [1, 2, 3,4 ],
    "2列目" : [10, 20, 30, 40]
})

st.table(df.style.highlight_min(axis = 0))

'''
# 章
## 節
### 項

```python
import pandas
```
'''

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns = ["a", "b", "c"]
)

st.line_chart(df2)


df3 = pd.DataFrame(
    np.random.rand(100, 2) / 50 + [35.69, 139.7],
    columns = ["lat", "lon"]
)

st.map(df3)


from PIL import Image

st.write("DisplayImage")


option = st.selectbox(
    "あなたの好きな数字を教えてください",
    list(range(1, 11))
)
"あなたの好きな数字は",option, "です。"



st.write("Interactive Widgets")

text = st.text_input("あなたの趣味を教えてください")
"あなたの趣味は", text, "です。"


condition = st.slider("あなたの調子は？", 0, 100, 50)
"あなたのコンディションは", condition, "です。"


left_column, right_column = st.columns(2)
butten = left_column.button("右カラムに文字を表示")
if butten:
    right_column.write("ここは右カラム")


expander = st.expander("問い合わせ")
expander.write("問い合わせ内容を書く")


st.write("プログレスバーの表示")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i + 1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Done!!"