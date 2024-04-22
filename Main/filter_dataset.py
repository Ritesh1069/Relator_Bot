import pandas as pd

def filter_ds(target_user_name, df):
    user_row = df[df['first_name'] == target_user_name]
    if not user_row.empty:
        target_location = user_row['location'].iloc[0]
        target_age_range = user_row['age_range'].iloc[0]
        filtered_df = df[(df['location'] == target_location) & (df['age_range'] == target_age_range)]
        if len(filtered_df) > 500:
            filtered_df['categories_count'] = filtered_df['categories'].apply(lambda x: len(x.split(',')))
            filtered_df = filtered_df.sort_values(by='categories_count', ascending=False)
            filtered_df = filtered_df.head(500)
        return(filtered_df)
    else:
        print("Target user not found in the dataset.")
