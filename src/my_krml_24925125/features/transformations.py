from typing import List
import pandas as pd

from sklearn.preprocessing import StandardScaler, OneHotEncoder


def scale_and_encode(data: pd.DataFrame,  # only features, no target needed here
                     scaler = None,
                     encoder = None,
                     ignore_cols: List[str] = None,
                     return_transformers: bool = True):

    temp_data = data.copy()

    if ignore_cols is not None:
        ignore_data = temp_data[ignore_cols]
        temp_data = temp_data.drop(ignore_cols, axis=1)
    
    numeric_cols = list(temp_data.select_dtypes("number").columns)
    categorical_cols = list(set(temp_data.columns) - set(numeric_cols))

    if scaler is None:
        temp_scaler = StandardScaler()
        temp_scaler.fit(temp_data[numeric_cols])
    else:
        temp_scaler = scaler

    if encoder is None:
        temp_encoder = OneHotEncoder(drop="first",
                                     sparse_output=False,
                                     dtype=int,
                                     handle_unknown="infrequent_if_exist")
        temp_encoder.fit(temp_data[categorical_cols])
    else:
        temp_encoder = encoder

    out_data = temp_encoder.transform(temp_data[categorical_cols])
    out_data = pd.DataFrame(out_data, columns=temp_encoder.get_feature_names_out())
    out_data[numeric_cols] = temp_scaler.transform(temp_data[numeric_cols])

    if ignore_cols is not None:
        out_data[ignore_cols] = ignore_data
    
    if return_transformers:
        return out_data, temp_scaler, temp_encoder
    else:
        return out_data