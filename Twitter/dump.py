#!/usr/bin/env python3
# OSINT/Twitter/dump.py

# dump.py
#  Dump a Twitter user's Follwers and Following
#  Uses Twint to scrape directly and bypass the rate limit 


# Imports
import twint
import sys
import argparse
import signal


def ctrl_c(sig, frame):
    print("\n{} chose to quit via CTRL+C!".format(os.environ['USER']))
    sys.exit(0)


def following(c, username):
    c.Output = "{}/following".format(username)
    twint.run.Following(c)


def followers(c, username):
    c.Output = "{}/followers".format(username)
    twint.run.Followers(c)


def main():
    
    parser = argparse.ArgumentParser(description="Get a list of Twitter users Followers and Following")
    parser.add_argument("-t", "--target", action='store', dest='username', required=True,  
                        help="Targets Twitter username")
    parser.add_argument("--following", action='store_true',
                        help="Get list of users target follows")
    parser.add_argument("--followers", action='store_true',
                        help="Get list of targtes followers")
    args = parser.parse_args()

    signal.signal(signal.SIGINT, ctrl_c)
    
    username = args.username
    c = twint.Config()
    c.Username = username
    c.User_full = True
    
    if args.following:
        following(c, username)
    elif args.followers:
        followers(c, username)
    else:
        parser.print_help()

    exit(0)

if __name__== "__main__":
    main()
