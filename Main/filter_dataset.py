# import pandas as pd

# def filter_ds(target_user_name, df):
#     user_row = df[df['first_name'] == target_user_name]
#     if not user_row.empty:
#         target_location = user_row['location'].iloc[0]
#         target_age_range = user_row['age_range'].iloc[0]
#         filtered_df = df[(df['location'] == target_location) & (df['age_range'] == target_age_range)]
#         if len(filtered_df) > 500:
#             filtered_df['categories_count'] = filtered_df['categories'].apply(lambda x: len(x.split(',')))
#             filtered_df = filtered_df.sort_values(by='categories_count', ascending=False)
#             filtered_df = filtered_df.head(500)
#         return(filtered_df)
#     else:
#         print("Target user not found in the dataset.")

import pandas as pd

def filter_ds(target_user_name, df, gend):
    user_row = df[df['first_name'] == target_user_name]
    if not user_row.empty:
        target_location = user_row['location'].iloc[0]
        target_age_range = user_row['age_range'].iloc[0]
        target_gender1 = gend 

        # Filter the DataFrame with single indexing to avoid chained indexing
        mask = (df['location'] == target_location) & (df['age_range'] == target_age_range) & (df['gender'] == target_gender1)
        filtered_df = df.loc[mask].copy()  # Make a copy to avoid SettingWithCopyWarning

        print(len(filtered_df))
        if len(filtered_df) > 100:
            # Use .loc for assignment to avoid SettingWithCopyWarning
            filtered_df.loc[:, 'categories_count'] = filtered_df['categories'].apply(lambda x: len(x.split(',')))
            filtered_df = filtered_df.sort_values(by='categories_count', ascending=False).head(100)
        
        filtered_df = pd.concat([filtered_df, user_row], ignore_index=True)
        return filtered_df
    else:
        print("Target user not found in the dataset.")
        return None
