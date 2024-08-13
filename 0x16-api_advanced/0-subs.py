import requests

def number_of_subscribers(subreddit):
    # Define the API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set the headers with a custom User-Agent to avoid rate limiting
    headers = {"User-Agent": "subreddit-subscriber-counter/0.1"}

    try:
        # Make the GET request
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the status code indicates success (200 OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract and return the number of subscribers
            return data['data']['subscribers']

        # If the subreddit is invalid, return 0
        elif response.status_code == 404:
            return 0
        # Handle other HTTP errors or unexpected status codes
        else:
            return 0

    except requests.RequestException:
        # Handle any request errors
        return 0

# Example usage:
# print(number_of_subscribers("python"))  # Should return the number of subscribers for r/python
# print(number_of_subscribers("nonexistentsubreddit"))  # Should return 0
