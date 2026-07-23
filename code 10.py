import pandas as pd

df = pd.DataFrame({
    "Prompt": ["Tree", "Bird"],
    "Images": [80, 95]
})
df.to_csv("genai_data.csv", index=False)