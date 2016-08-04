###########################################################################
#       These will likely end up being dictionaries of dictionaries       #
###########################################################################
import re

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
                    'I hate life'
                    
] #This is what we are looking for. We will use regular expressions
depression_response = [
                      'Depression can hurt. If you need someone to talk to someone ' + 'I\'m here for you'
                      ] #This is what we are responding with. Examples here will be replaced with regular expressions
curious_words = [
                'I wonder'
                'How does'
                'What if'
]

curious_responses = [
                    'Here, let me help you with that'
]

relationship_words= []

relationship_responses = []
