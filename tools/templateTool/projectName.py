# Util function to give filenames a consistent name
def projectName(title, author, ff='ove'):
    return "{}-{}.{}".format(
        author.replace(' ','_'),
        title.replace(' ','_'),
        ff
    )
