"""
Data validation functions.
"""


# Example function to implement:
def validate_isbn(isbn):
    """Validate ISBN-13 format."""
    print(isbn)
    isbn = str(isbn).strip().replace('-', '')    #.replace(" ", "").replace("-", "")
#    isbn = isbn.replace('-', '')    #.replace(" ", "").replace("-", "")
    print(isbn)

    if not isbn.isdigit():
        return False
    
    return True
