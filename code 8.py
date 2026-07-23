import pandas as pd

df = pd.DataFrame({
    "Images": [100, 120, 90, 150]
})
print(df["Images"].mean())