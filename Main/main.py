import csv
import facebook
import pandas as pd

def convert_to_csv(profile):
    # Get profile link
    profile_link = profile.get('link', '')
    # Extract necessary fields from the profile JSON object
    fields = ['first_name', 'gender', 'birthday', 'email', 'profile_link', 'categories']
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
            'categories': categories_str  # Include categories in the CSV output
        }
        writer.writerow(row)

def main(key): 
    token = key
    
    graph = facebook.GraphAPI(token) 
    profile = graph.get_object('me', fields='first_name, gender, birthday, email, link, likes{category}')
    file= pd.read_csv("profile_dataNewest.csv")
    if ((file['first_name'].eq(profile.get('first_name', '')).any()) & (file['email'].eq(profile.get('email', '')).any())):
        print("user already exists")
        
    else:
        convert_to_csv(profile)
        print("Successfully updated the user")
        
main("EAAOo80pc1RABO3za5pOgYek939dXlTGT8rZCOe1Bv7qZCZAtKluVa0UDex35vQprtbOBkyTVTBqMDgZBvUfYJoQ1q0xgLOAWJVltrslV4cw1Tm7WuG1a7TGjjcrZABrvReZCvKAgexdktqsA7XOlwAuYhce4Vpb1WPG7lyflCjY6fPpqtVZBkiVIeQGi1QqKzaEj3xKn7xSYoluXHrH7zsZD")