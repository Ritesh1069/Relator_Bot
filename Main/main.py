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
    token = "EAAOo80pc1RABO1wF8BIwAQi9V7kPm5SojuPuFSGcsZCPSnaUbdNrPtjL0ikgIxYclUjpZBZA7vniqkfBrxLUOQirYtULBcxe4sHOZC71Tknsl0tsduw3SEQZBC5XVL40nQypLeo9KfCO1BvGf3YXn5LVWcy7IWTRaeuAKvdI5mPTVb9PM1ZATyqfvn9t7Xjyuijv43A8OGEUJB9i7JXVxnKTNFWL5SFVrvZAuoZBZBIBV2XZCV5ErWamNM2R5SFjRLKMAZD"
    
    graph = facebook.GraphAPI(token) 
    profile = graph.get_object('me', fields='first_name, gender, birthday, email, link, likes{category}')
    print(profile)
    convert_to_csv(profile)
    
main()