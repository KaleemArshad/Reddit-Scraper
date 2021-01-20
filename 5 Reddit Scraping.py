# the module, by which we will scrape reddit
import praw
import pprint

# This for getting access to reddit for Scraping
reddit = praw.Reddit(
    client_id='LtXZqlldge3fEg',
    client_secret='kS4Nh6UVPI4YPLNRCm25xx-3augdjg',
    user_agent='windows:this.is.my.bot:v1 (by u/Sajawal_Chopra55)',
    username='Sajawal_Chopra55',
    password='Sawemah55'
)

# if this print true, it means that you are not authorized if false it means your are authorized
print(reddit.read_only)

# for the Detail of Posts max 10
for submission in reddit.subreddit('learnpython').hot(limit=10):
    print(submission.title)
    print(submission.score)
    print(submission.id)
    print(submission.url)
# Name of the Redditor(member) of the subreddit(group)
    redditor = submission.author
    print(redditor.name)

# For Detail of subreddit(Group)
subreddit = reddit.subreddit('learnpython')
print(subreddit.title)
print(subreddit.display_name)
print(subreddit.description)

# for printing comments of a post
for submission in reddit.subreddit('learnpython').hot(limit=1):
    # for top comments
    # submission = reddit.submission(id="39zje0")
    top_comments = list(submission.comments)
    print(top_comments)
    # for all comments
    all_comments = submission.comments.list()
    print(all_comments)

# To Determine Available Attributes of an Object
submission = reddit.submission(id="39zje0")
print(submission.title)  # to make it non-lazy
pprint.pprint(vars(submission))
