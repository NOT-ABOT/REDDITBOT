###########################################################################
#       These will likely end up being dictionaries of dictionaries       #
###########################################################################
import re
url = 'http://www.google.com/?#q='
all_comment_types = [
                    depression_words, 
                    depression_responses, 
                    curious_words,
                    curous_responses,
                    relationship_words,
                    relationship_responses
]
depression_words = [
                    'I want to die',
                    'I want to kill myself',
                    'I hate life',
                    
] 
#This is what we are looking for. We will use regular expressions later
depression_response = [
                      'I\'m so sorry to hear that you\'re in pain. If you are in serious pain and need help' + ', ' + '[please visit this site](https://afsp.org/)',
                      'I understand your pain. [This link might be able to help](https://afsp.org/)'
] #This is what we are responding with. Examples here will be replaced with regular expressions
curious_words = [
                'I wonder why'
                'How does'
                'What if'
]

curious_responses = [
                    '[Here, let me help you with that](' + url + '### + ')'
]

relationship_words= []

relationship_responses = []
