import re


def safe_password(text):
    if len(text)<8:
        return False
    if not re.search('[0-9]', text):
        return False
    if not re.search('[A-Z]', text):
        return False
    if not re.search('[a-z]', text):
        return False
    if not re.search('[^a-zA-Z0-9]', text):
        return False
    return True

if __name__ == "__main__":
    assert safe_password('A12a$567') == True
 

