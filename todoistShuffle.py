#
# Source: https://github.com/djnicholson/todoist-shuffle
#
# Requires todoist-python:
# $ sudo pip install todoist-python
# See https://developer.todoist.com/index.html?python for documentation
#

import todoist
import random

##
# BEGIN: Customization
##

# Insert your own API key (the "API token" on the "Account" tab of Todoist Settings) in
# a copy of this file saved somewhere that you will not git commit:
apiKey = 'INSERTKEYHERE'

# The query to use when finding items to shuffle. This query finds all items with 
# the 'shuffle' label:
queryForItemsToShuffle = '@shuffle'

# The date range to shuffle within. Items will be randomly placed over the subsequent 
# 90 days (starting from now):
windowSizeInDays = 90;

##
# END: Customization
##

api = todoist.api.TodoistAPI(apiKey)

shufflableItems = api.query([queryForItemsToShuffle])[0]["data"]

for item in shufflableItems:
    hoursFromNow = random.randint(1, windowSizeInDays * 24)
    newDueDate = '' + str(hoursFromNow) + ' hours'

    print('Item being shuffled:')
    print(' ' + item["content"])
    print(' - Old due date: ' + str(item["due_date"]))
    print(' - New due date: ' + newDueDate)

    itemProxy = api.items.get_by_id(item["id"])
    itemProxy.update(date_string=newDueDate,date_lang='en',due_date_utc=None)

api.commit()
