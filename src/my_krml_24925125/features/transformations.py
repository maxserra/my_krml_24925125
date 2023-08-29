from typing import List
import pandas as pd

from sklearn.preprocessing import StandardScaler, OneHotEncoder


def scale_and_encode(data: pd.DataFrame,  # only features, no target needed here
                     scaler = None,
                     encoder = None,
                     ignore_cols: List[str] = None,
                     return_transformers: bool = True) -> pd.DataFrame:

    temp_data = data.copy()

    if ignore_cols is not None:
        ignore_data = temp_data[ignore_cols]
        temp_data = temp_data.drop(ignore_cols, axis=1)
    
    numeric_cols = list(temp_data.select_dtypes("number").columns)
    categorical_cols = list(set(temp_data.columns) - set(numeric_cols))

    scaler = scaler if scaler is not None else StandardScaler()
    encoder = encoder if encoder is not None else OneHotEncoder(
        drop="first",
        sparse_output=False,
        dtype=int,
        handle_unknown="infrequent_if_exist"
    )

    out_data = encoder.fit_transform(temp_data[categorical_cols])
    out_data = pd.DataFrame(out_data, columns=encoder.get_feature_names_out())
    out_data[numeric_cols] = scaler.fit_transform(temp_data[numeric_cols])

    if ignore_cols is not None:
        out_data[ignore_cols] = ignore_data
    
    if return_transformers:
        return out_data, scaler, encoder
    else:
        return out_data