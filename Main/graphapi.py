import csv
import facebook
import pandas as pd
#un updated
def convert_to_csv(profile):
    # Get profile link
    profile_link = profile.get('link', '')
    # Extract necessary fields from the profile JSON object
    fields = ['first_name', 'gender', 'birthday', 'age_range', 'location', 'email', 'profile_link', 'categories']
    likes = profile.get('likes', {}).get('data', [])  # Extract 'likes' data
    # Create a list to store all categories
    categories = []
    # Add categories to the list
    for like in likes:
        category = like.get('category', '')
        if category not in categories:
            categories.append(category)
    # Join all categories into a single string
    categories_str = ','.join(categories)
   
    # Read existing CSV file if exists
    try:
        existing_data = pd.read_csv("profile_dataNewest.csv")
    except FileNotFoundError:
        existing_data = pd.DataFrame(columns=fields)

    # Check if the user already exists
    user_exists = existing_data[(existing_data['first_name'] == profile.get('first_name', '')) & 
                                (existing_data['email'] == profile.get('email', ''))].index
    # If user exists, update their details
    if not user_exists.empty:
        # existing_data.loc[user_exists] = {
        #     'first_name': profile.get('first_name', ''),
        #     'gender': profile.get('gender', ''),
        #     'birthday': profile.get('birthday', ''),
        #     'email': profile.get('email', ''),
        #     'profile_link': profile_link,
        #     'categories': categories_str,
        #     'age_range': (str(profile.get('age_range', {}).get('min', '')) + "-" + str(profile.get('age_range', {}).get('max', ''))),
        #     'location': profile.get('location', {}).get('name', '')
        # }
        existing_data.loc[user_exists, ['gender', 'birthday', 'age_range', 'location', 'categories']] = [
            profile.get('gender', ''),
            str(profile.get('birthday', '')),
            str(str(profile.get('age_range', {}).get('min', '')) + "-" + str(profile.get('age_range', {}).get('max', ''))),
            profile.get('location', {}).get('name', ''),
            categories_str
        ]
        print("Existing user details updated successfully")
    else:
        # Append new user's details to existing data
        new_row = {
            'first_name': profile.get('first_name', ''),
            'gender': profile.get('gender', ''),
            'birthday': str(profile.get('birthday', '')),
            'age_range': str(str(profile.get('age_range', {}).get('min', '')) + "-" + str(profile.get('age_range', {}).get('max', ''))),
            'location': profile.get('location', {}).get('name', ''),
            'email': profile.get('email', ''),
            'profile_link': profile_link,
            'categories': categories_str
            
        }
        existing_data = existing_data._append(new_row, ignore_index=True)
        print("New user details updated successfully")
        
    # Write data to CSV file
    existing_data.to_csv('profile_dataNewest.csv', index=False, encoding='utf-8')

def main(key): 
    token = key
    
    graph = facebook.GraphAPI(token) 
    profile = graph.get_object('me', fields='first_name, gender, birthday, age_range, location, email, link, likes{category}')
    convert_to_csv(profile)

main("EAAOo80pc1RABO5uPZA7xVZBeJAbDDjFZBkAZBp5M2YZBdGLKkCbJe2dOZAEVK14YlgpbkWy1obGSnMfFMjwI9jgsUrjyQbY0JR0q0kTZBYobsCulmbVPbsQSydwzLHYLqnKZAnon6LztZB76BVeuWPG08nZC9QZCDCgYD25UR4FI86h2cgVpFmfXfDVqzH4ZCZBjvZCPNduvYNvsh03pEZB6nqNadZBJcVODBTshjZBJ6vhC9IRAXc4so0EIMKZCgZCpuK0QIhuewZDZD")
