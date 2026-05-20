import requests
from datetime import datetime, timedelta

username = 'torvalds'  # Linus Torvalds (creator of Linux)

# Get user info
user_api_url = f'https://api.github.com/users/{username}'

try:
    # Fetch user info
    response = requests.get(user_api_url)
    response.raise_for_status()
    user_data = response.json()
    
    print(f"Name: {user_data.get('name', 'N/A')}")
    print(f"Location: {user_data.get('location', 'N/A')}")
    print(f"Public Repos: {user_data.get('public_repos', 'N/A')}")
    print()
    
    # Fetch contributions from the last year
    # Calculate date from one year ago
    one_year_ago = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    
    # Search for commits in the last year
    search_url = f'https://api.github.com/search/commits?q=author:{username}+committer-date:>{one_year_ago}&per_page=1'
    
    response = requests.get(search_url)
    response.raise_for_status()
    search_data = response.json()
    
    total_contributions = search_data.get('total_count', 0)
    print(f"Commits in the last year: {total_contributions}")
    
except requests.exceptions.RequestException as error:
    print(f"Error fetching data: {error}")
