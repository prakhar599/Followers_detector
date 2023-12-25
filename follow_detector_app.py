import tweepy

# Add your Twitter API credentials
consumer_key = "IVcdXS7UTxkILShjFTnNuOSED"
consumer_secret = "M9QUrVRFwZtp7l8RWVN0zGc0RwocjWjFMdnNOP5EMzQpqjJaM4"
access_token = "1709172747287601152-3GUVDRwUr2n19Ol8IfapxULkuE3Dux"
access_token_secret = "UnZCUeIylebCoutweDUabUQRCjcjXH5Z6EQBeBAj7gZKU"

# Set up Tweepy authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def get_followers():
    # Get your followers
    followers = set(api.get_followers(screen_name="PrakharPar13", count=200).ids())
    return followers

def get_following():
    # Get accounts you are following
    following = set(api.friends(screen_name="PrakharPar13", count=200).ids())
    return following

def find_non_followers():
    followers = get_followers()
    following = get_following()
    
    # Find accounts not following you back
    non_followers = following - followers
    
    return non_followers

def main():
    non_followers = find_non_followers()
    
    print("Accounts not following you back:")
    for user_id in non_followers:
        user = api.get_user(user_id)
        print(f"{user.screen_name} (ID: {user.id})")

if __name__ == "__main__":
    main()

