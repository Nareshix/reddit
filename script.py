import praw
from termcolor import colored



reddit = praw.Reddit(
    client_id="RwJpvGeakXSR0dbHQ3WchQ",
    client_secret="nXLnw5QM1M1xNBRhD1vRJu-EBA8T5g",
    user_agent="Character_Glass_7568 ",
)


sgexam = reddit.subreddit('sgexams')

#Dict is used to remopve duplicate posts when sorting (hot,new,top)
posts = {}

print('')

def sort_by(option):
    for submission in option:
        
        #to remove the pinned post of r/sgexam
        if submission.url == 'https://www.reddit.com/r/SGExams/comments/147guo1/a_levels_update_to_the_holy_grail_mark_6/':
            continue

        # slice flair to remove unncessary emoji
        index = submission.link_flair_text.find(':')
        if submission.link_flair_text[:index-1] in ['A Levels', 'Junior Colleges','University','Scholarships']:
            posts[submission.title] = submission.url

sort_by(sgexam.hot(limit=10))
sort_by(sgexam.new(limit=10))
sort_by(sgexam.top(limit=10,time_filter='day'))

for title,link in posts.items():
    print(colored(title,'light_green') + '\n' + colored(link,'light_blue') + '\n') 
