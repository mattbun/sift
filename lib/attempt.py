#
# An attempt contains a result and a certainty that the result is correct. 
# This awkwardly named class is meant to give higher priority to certain ways 
# of getting metadata. For example, when trying to get a track name, Id3 tags 
# are given MUCH higher priority than the filename itself.
#
class attempt:
    certainty = 0
    result = ""
    def __init__(self, r = "", c = 0):
        self.certainty = c
        self.result = r

    def __str__(self):
        return '%s, %s' % (self.certainty, self.result)


def getMostCertain(attempts):
    best = attempt("", 0);

    for a in attempts:
        if int(a.certainty) > best.certainty:
            best = a

    return best


# This is just a convenience method that returns an attempt with certainty 0 is
# the result string is empty or otherwise, it returns an attempt with the 
# max_certainty
def makeAttempt(result, max_certainty):
    if result is None or result == "":
        return attempt(0,"")
    else:
        return attempt(result, max_certainty)
