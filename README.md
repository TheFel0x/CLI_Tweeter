
[![CodeFactor](https://www.codefactor.io/repository/github/thefel0x/cli_tweeter/badge/master)](https://www.codefactor.io/repository/github/thefel0x/cli_tweeter/overview/master)

# CLI_Tweeter

Using [Tweepy](https://github.com/tweepy/tweepy).

#### Features:
- custom "Twitter for..." message
- make tweets, replies and comment retweets with and without images
- save and access all your accounts easily
- simple and effective commands

## Installation

 - Download both files
 - Install Tweepy
`pip install tweepy`
(Assuming you have Python and pip already installed.)

## How to use

 - Get access to the [Twitter API](https:///developer.twitter.com/) 
 - Make a [new app](https://developer.twitter.com/en/portal/apps/new)
 - Enter your API / consumer key and secret in the [api_stuff.py](https://github.com/TheFel0x/CLI_Tweeter/blob/master/api_stuff.py)
 - Run [tweeter.py](https://github.com/TheFel0x/CLI_Tweeter/blob/master/tweeter.py) with Python
 - The program will then open your web browser and ask you for the pin that Twitter generates for you.
 - use `h` to show all available commands

## Commands

| Command | Explanation |
|--|--|
| q | Quit |
| h | Help |
| tw | Tweet |
| itw | Tweet with image |
| re | Reply (don't use this) |
| sre | Stable Reply |
| ire | Reply with image (don't use this) |
| isre | Stable reply with image |
| crt | Comment Retweet |
| icrt | Comment Retweet with image |

## Inputs
After you enter a command you will be asked for further inputs.
| Symbol | Input |
|--|--|
| `>` | What you want to tweet. Example: `>Hello world!` |
| `ID:` | The ID of the Tweet that you want to reply to. Found at the end of the Tweets URL. Example: `ID:1215831854596743168` |
| `ats:` | All the @'s of the people that you want to reply to, divided with spaces. Example: `ats:@Twitter @github` |
| `URL:` | The URL of the Tweet that you want to comment-retweet. Example: `URL:https://twitter.com/github/status/1278433248994091022` |
| `count:` | Amount of images that you want to add to a tweet. Maximum is 4. Example: `count:3` |
| `path:` | Path of the image that you want to upload. (Will be asked up to 4 times, depending on `count:`. Example: `path:/home/thefel0x/Downloads/image.png` |

## Known Bugs and To-Do

- Doesn't check if the post has <150 characters.
- Multi-Line Tweets not possible.
- Image upload doesn't support `.jpg` files and probably many other file types. `.png` is working fine.
- ~~`sre` and `isre` will replace `re` and `ire`~~ _(done)_
- needs `undo` command to delete last tweet
