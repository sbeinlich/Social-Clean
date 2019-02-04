"""Clean up all social media."""
import twitter

def main():
    username = input("Which user? ")
    twitter.tweetbot.clean_tweets(username)
    
if __name__ == "__main__":
    main()