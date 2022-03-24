

def preprocessor(data):
    # helper function preprocesses data for machine learning modeling
    # it first removes string columns
    # then use preprocessor function from sci-kit learn
    # and lastly return pre-processed dataframe
    data.drop(['Country or region', 'name'], axis = 1) 
    preprocessed_data = preprocess.transform(data) 
    return preprocessed_data 