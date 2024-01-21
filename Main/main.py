import csv
import facebook

def convert_to_csv(profile):
    # Extract necessary fields from the profile JSON object
    fields = ['first_name', 'gender', 'birthday', 'email', 'profile_link', 'categories']
    likes = profile.get('likes', {}).get('data', [])  # Extract 'likes' data
    # Create a list to store all categories
    categories = []
    # Add categories to the list
    for like in likes:
        category = like.get('category', '')
        if category:
            categories.append(category)
    # Join all categories into a single string
    categories_str = ', '.join(categories)
    # Get profile link
    profile_link = profile.get('link', '')
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

def main(): 
    token = "EAAOo80pc1RABO80NOUxygZBnKY97aRBPqCvZAJTxWqEsViZBorZB8yVUZAddHliLLd62AoT2loVdkJKU6WZCG58TL6aCZA2bQf30JQZAOFvt9m9ZAouKuZAvmZBrIXEYvUtolqK6qFnXosVJZBmZBtY9CK2bhxje8fvXPtSZAOu7WXpKAzJK48cFBcyQ5wKUjencipMZA58xs86BVjT98DgjZBGEc2CIYjnFG9P49qNM3tpthI4OdfNE1XKwld2V2KN8re5dJwZDZD"
    
    graph = facebook.GraphAPI(token) 
    profile = graph.get_object('me', fields='first_name, gender, birthday, email, link, likes{category}')
    print(profile)
    convert_to_csv(profile)
    
main()