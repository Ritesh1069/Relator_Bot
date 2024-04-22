import csv
import facebook
import pandas as pd

def convert_to_csv(profile):
    # Get profile link
    profile_link = profile.get('link', '')
    # Extract necessary fields from the profile JSON object
    fields = ['first_name', 'gender', 'birthday', 'email', 'profile_link', 'categories','age_range','location']
    likes = profile.get('likes', {}).get('data', [])  # Extract 'likes' data
    # Create a list to store all categories
    categories = []
    # Add categories to the list
    for like in likes:
        category = like.get('category', '')
        if category not in categories:
            categories.append(category)
        else:
            pass
    # Join all categories into a single string
    categories_str = ','.join(categories)
   
    #checking elements
    set1 = set(categories)
    if category not in set1:
        set1 += (category,)
    else:
        pass
    # Write data to a CSV file
    with open('profile_dataNewest.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        
        row = {
            'first_name': profile.get('first_name', ''),
            'gender': profile.get('gender', ''),
            'birthday': profile.get('birthday', ''),
            'email': profile.get('email', ''),
            'profile_link': profile_link,
            'categories': categories_str,# Include categories in the CSV output
            'age_range': (str(profile.get('age_range', '').get('min', [])) + "-"+ str(profile.get('age_range', '').get('max', []))),
            'location': profile.get('location', '').get('name', [])
        }
        writer.writerow(row)

def main(key): 
    token = key
    
    graph = facebook.GraphAPI(token) 
    profile = graph.get_object('me', fields='first_name, gender, birthday, email, link, likes{category}, age_range, location')
    file= pd.read_csv("profile_dataNewest.csv")
    if ((file['first_name'].eq(profile.get('first_name', '')).any()) & (file['email'].eq(profile.get('email', '')).any())):
        print("user already exists")
        
    else:
        convert_to_csv(profile)
        print("Successfully updated the user")
        
main("EAAOo80pc1RABO5uPZA7xVZBeJAbDDjFZBkAZBp5M2YZBdGLKkCbJe2dOZAEVK14YlgpbkWy1obGSnMfFMjwI9jgsUrjyQbY0JR0q0kTZBYobsCulmbVPbsQSydwzLHYLqnKZAnon6LztZB76BVeuWPG08nZC9QZCDCgYD25UR4FI86h2cgVpFmfXfDVqzH4ZCZBjvZCPNduvYNvsh03pEZB6nqNadZBJcVODBTshjZBJ6vhC9IRAXc4so0EIMKZCgZCpuK0QIhuewZDZD")