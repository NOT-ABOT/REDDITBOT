###########################################################################
#       These will likely end up being dictionaries of dictionaries       #
###########################################################################
import re
url = 'http://www.google.com/?#q='
all_comment_types = [
                    depression_words, 
                    curious_words,
                    relationship_words,
]
all_comment_responses = [
                      depressiong_responses,
                      curious_responses,
                      relationship_responses
]

depression_words = [
                    'I want to die',
                    'I want to kill myself',
                    'I hate life',
                    'I\'m having suicidal thoughts'
                    'I don\'t have a reason to live'
                    'I hate myself'
                    'I am a failure'
                    'I don\'t deserve to live'
                    'I can\'t do this anymore'
                    
] 
#This is what we are looking for. We will use regular expressions later
depression_response = [
                      'I\'m so sorry to hear that you\'re in pain. If you are in serious pain and need help' + ', ' + '[please visit this site](https://afsp.org/)',
                      'I understand your pain. [This site might be able to help](https://afsp.org/)'
] #This is what we are responding with. Examples here will be replaced with regular expressions
curious_words = [
                'I wonder why'
                'How does',
                'What if',
                'When did'
]

curious_responses = [
                    '[Here, let me help you with that](' + url + comment + ')'
]

relationship_words= [
                    'How do I get a *friend*'
]

relationship_responses = [
                      'The most common way is to ask the person out'
  
  
]
