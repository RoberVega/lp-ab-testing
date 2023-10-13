import pandas as pd
import numpy as np 




def run_results(version: str)->int:
    if version=="A":
        return 1 if np.random.rand() < 0.027 else 0
    if version=="B":
        return 1 if np.random.rand() < 0.059 else 0




def get_results(data: pd.DataFrame)->pd.DataFrame:
    data["interacted"] = data["version"].apply(run_results)
    return data
