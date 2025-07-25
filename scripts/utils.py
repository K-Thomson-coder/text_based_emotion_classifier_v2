# save and load file
import pickle 

def save_file(fname, obj, mode='wb') :
    with open(fname, mode) as f :
        pickle.dump(obj, f)

def load_file(fname, mode='rb') :
    with open(fname, mode) as f :
        return pickle.load(f)

# clean text input for training model
def _remove_punctuation_(string) :
    punctuation = r"""!@#$%^&*()-=_+[]\{}|;':",./<>?"""
    for i in punctuation :
        string = string.replace(i, "")
    return string

def _remove_numbers_(string) :
    nums = "0123456789"
    for i in nums :
        string = string.replace(i, "")
    return string

def clean(string) : 
    tmp = string.lower()
    tmp = _remove_numbers_(tmp)
    tmp = _remove_punctuation_(tmp)
    return tmp