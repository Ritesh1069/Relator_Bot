import pandas as pd

def filter_ds(target_user_name, df):
    user_row = df[df['first_name'] == target_user_name]
    if not user_row.empty:
        target_categories = set(user_row['categories'].iloc[0].split(',')) 
        
        # loc_pref = input("Do you want to filter users by location (y/n): ")
        loc_pref = "y"
        if loc_pref == 'y':
            # target_location1 = input('Enter location ("Mumbai,Maharashtra","Pune,Maharashtra","Nashik,Maharashtra","Thane,Maharashtra","Navi Mumbai,Maharashtra"): ')
            target_location1 = "Mumbai,Maharashtra"
        # age_pref = input('Do you want to filter users by age (y/n): ')
        age_pref = "y"
        if age_pref == 'y':
            # target_age_range1 = input('Enter age range ("13-17","18-20","21+"): ')
            target_age_range1 = "21+"
        # gender_pref = input('Do you want to filter users by gender (y/n): ')
        gender_pref = "y"
        if gender_pref == 'y':
            # target_gender1 = input('Enter Gender (male/female): ')
            target_gender1 = "male"
            
        if loc_pref == 'y' and age_pref == 'n' and gender_pref == 'n': 
            mask = (df['location'] == target_location1)
            filtered_df = df.loc[mask].copy()
        
        elif loc_pref == 'n' and age_pref == 'y' and gender_pref == 'n': 
            mask = (df['age_range'] == target_age_range1)    
            filtered_df = df.loc[mask].copy()
            
        elif loc_pref == 'n' and age_pref == 'n' and gender_pref == 'y':
            mask = (df['gender'] == target_gender1) 
            filtered_df = df.loc[mask].copy()
        
        elif loc_pref == 'y' and age_pref == 'y' and gender_pref == 'n': 
            mask = (df['location'] == target_location1) & (df['age_range'] == target_age_range1)
            filtered_df = df.loc[mask].copy()
        
        elif loc_pref == 'n' and age_pref == 'y' and gender_pref == 'y': 
            mask = (df['age_range'] == target_age_range1) & (df['gender'] == target_gender1)
            filtered_df = df.loc[mask].copy()
            
        elif loc_pref == 'y' and age_pref == 'n' and gender_pref == 'y': 
            mask = (df['location'] == target_location1) & (df['gender'] == target_gender1)
            filtered_df = df.loc[mask].copy()
            
        elif loc_pref == 'y' and age_pref == 'y' and gender_pref == 'y': 
            mask = (df['location'] == target_location1) & (df['age_range'] == target_age_range1) & (df['gender'] == target_gender1)
            filtered_df = df.loc[mask].copy()
            
        elif loc_pref == 'n' and age_pref == 'n' and gender_pref == 'n': 
            filtered_df = df.copy()
        
        print(len(filtered_df))
        if len(filtered_df) > 130:
            filtered_df.loc[:, 'total_categories_count'] = filtered_df['categories'].apply(lambda x: len(x.split(',')))
            # Count the number of matching categories for each user
            filtered_df.loc[:, 'similar_categories_count'] = filtered_df['categories'].apply(lambda x: len(target_categories.intersection(set(x.split(',')))))
            filtered_df.loc[:, 'total_to_similar_ratio'] = filtered_df['total_categories_count']/filtered_df['similar_categories_count']
            filtered_df = filtered_df.sort_values(by='total_to_similar_ratio', ascending=True).head(130)
        
        filtered_df = pd.concat([filtered_df, user_row], ignore_index=True)
        return filtered_df
    else:
        print("Target user not found in the dataset.")
        return None

if __name__=="__main__":
    df = pd.read_csv("R:/Git/Relator_Bot/test datasets/1000_location.csv")
    user = input("enter name: ")
    print(filter_ds(user,df))