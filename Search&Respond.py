###########################################################################
#       These will likely end up being dictionaries of dictionaries       #
###########################################################################
import re

depression_words = [
                    'I want to die',
                    'I want to kill myself',
                    'I hate life'
                    
] #This is what we are looking for. We will use regular expressions
depression_response = [
                      'Depression can hurt. If you need someone to talk to...'
                      ] #This is what we are responding with. Examples here will be replaced with regular expressions
