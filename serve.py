from flashtext.keyword import KeywordProcessor
import pickle

# Funtion that takes loads in our pickeled word processor
# and defines a function for using it. This makes it easy
# to do these steps together when serving our model.
def get_keywords_api():
    
    # read in pickled word processor. You could also load in
    # other models as this step.
    with open("word_processor.pkl", "rb") as file:
        keyword_processor = pickle.load(file)
    
    # Function to apply our modle & extract keywords from a 
    # provided bit of text
    def keywords_api(text): 
        keywords_found = keyword_processor.extract_keywords(text, span_info=True)      
        return keywords_found
    
    # return the function
    return keywords_api
