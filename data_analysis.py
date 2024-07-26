from collections import Counter
import pandas as pd

syn_df = pd.read_csv("top_400k.csv")
NUM_CLASSES = 5

top_five = Counter(syn_df["modularity_class"]).most_common(NUM_CLASSES)

for mc, count in top_five:
    print(f"Modularity Class {mc}, Count: {count}")