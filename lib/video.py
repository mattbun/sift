import lib
from lib import utils
from lib import attempt
import re

#
# Attempt to find information about a video
#
def process(conf, full_path):
    
    file_name = utils.getFileName(full_path)
    extension = utils.getExtension(full_path)
    containing_directory = utils.getContainingDirectory(full_path)

    tv_info = getTVInfo(full_path, file_name, containing_directory)
    movie_info = getMovieInfo(file_name, full_path)

    tv_info['extension'] = extension
    movie_info['extension'] = extension
    tv_info['original_name'] = file_name
    movie_info['original_name'] = file_name

    if (isTV(tv_info, full_path)):
        return utils.assemble(conf['tv_format'], tv_info)
    else:
        return utils.assemble(conf['movie_format'], movie_info)


def getTVInfo(full_path, file_name, containing_directory):
    
    # These arrays will hold all of the attempts, we'll tally them up later
    show_name_attempts = []
    season_attempts = []
    episode_number_attempts = []
    episode_name_attempts = []
    year_attempts = []
    
    # Now we'll populate those arrays
    # Look for sNNeNN names
    o = re.search('(.*)\s*[\.-]*\s*[sS](\d+)[\s\.-]*[eE](\d+)[\s\.-]*(.*)',file_name)
    if o is not None:
        season_attempts.append(attempt.makeAttempt(o.group(2), 80))
        episode_number_attempts.append(attempt.makeAttempt(o.group(3), 80))
        if o.group(1) != '':
            show_name_attempts.append(attempt.makeAttempt(o.group(1), 80))
        if o.group(4) != '':
            episode_name_attempts.append(attempt.makeAttempt(o.group(4), 80))

    # Look for NNxNN names
    o = re.search('(.*)(\d+)[xX-](\d+)(.*)',file_name) #TODO add more of these
    if o is not None:
        season_attempts.append(attempt.makeAttempt(o.group(2), 70))
        episode_number_attempts.append(attempt.makeAttempt(o.group(3), 70))
        if o.group(1) != '':
            show_name_attempts.append(attempt.makeAttempt(o.group(1), 70))
        if o.group(4) != '':
            episode_name_attempts.append(attempt.makeAttempt(o.group(4), 70))

    # Look for episode numbers that follow the letter E
    o = re.search('[eE](\d+)',file_name)
    if o is not None:
        episode_number_attempts.append(attempt.makeAttempt(o.group(1), 60))

    # Look for episode numbers that follow the word "episode"
    o = re.search('[eE]pisode(\d+)',file_name)
    if o is not None:
        episode_number_attempts.append(attempt.makeAttempt(o.group(1), 65))

    # look for episode numbers that are just the number and no season number
    # These get less certain as it finds more digits since they could contain 
    # season numbers or actually be years
    #TODO add more checks for numbers that arent at the beginning of the string and decide whether or not these should be included at all
    o = re.search('^(\d{1,2})',file_name)
    if o is not None:
        episode_number_attempts.append(attempt.makeAttempt(o.group(1),30))
    
    o = re.search('^(\d{3})',file_name)
    if o is not None:
        episode_number_attempts.append(attempt.makeAttempt(o.group(1),20))

    o = re.search('^(\d{4})',file_name)
    if o is not None:
        episode_number_attempts.append(attempt.makeAttempt(o.group(1),10))

    #look for season numbers that follow the letter S
    o = re.search('[sS](\d+)',full_path)
    if o is not None:
        season_attempts.append(attempt.makeAttempt(o.group(1),50))

    #look for season numbers that follow the word "Season"
    o = re.search('[Ss][Ee][Aa][Ss][Oo][Nn]\s*(\d+)',full_path)
    if o is not None:
        season_attempts.append(attempt.makeAttempt(o.group(1),7))

    #TODO Check that the year is valid
    # Look for four digit numbers that could be years
    o = re.search('(\d{4})', full_path) 
    if (o is not None and utils.isValidYear(o.group(1))):
        year_attempts.append(attempt.makeAttempt(o.group(1), 10))

    # Look for four digit numbers *in parentheses* that could be years
    o = re.search('[\(\[](\d{4})[\(\[]', full_path) #TODO add brackets, parentheses
    if (o is not None and utils.isValidYear(o.group(1))):
        year_attempts.append(attempt.makeAttempt(o.group(1), 50))
    
    # Tally up the votes
    show_name = attempt.getMostCertain(show_name_attempts)
    season = attempt.getMostCertain(season_attempts)
    episode_number = attempt.getMostCertain(episode_number_attempts)
    episode_name = attempt.getMostCertain(episode_name_attempts)
    year = attempt.getMostCertain(year_attempts)
    
    # Clean up the names
    show_name.result = utils.cleanString(show_name.result)
    episode_name.result = utils.cleanString(episode_name.result)

    #print("Show Name: %s" % show_name.result)
    #print("Season: %s" % season.result)
    #print("Episode #: %s" % episode_number.result)
    #print("Episode Name: %s" % episode_name.result)
    
    data = {'show_name' : show_name.result,
            'season_number' : season.result,
            'episode_number' : episode_number.result,
            'episode_name' : episode_name.result}

    return data;

def getMovieInfo(file_name, full_path):
    
    title_attempts = []
    year_attempts = []
    
    # Try to remove year from title if it exists.
    o = re.search('(.*)\s*\(\d{4}\)', file_name)
    if (o is not None):
        title_attempts.append(attempt.makeAttempt(o.group(1), 20))
    
    # Or just give up...
    title_attempts.append(attempt.makeAttempt(file_name, 10))


    # Look for four digit numbers that could be years
    o = re.search('(\d{4})', full_path) 
    if (o is not None and utils.isValidYear(o.group(1))):
        year_attempts.append(attempt.makeAttempt(o.group(1), 10))

    # Look for four digit numbers *in parentheses* that could be years
    o = re.search('[\(\[](\d{4})[\(\[]', full_path) #TODO add brackets, parentheses
    if (o is not None and utils.isValidYear(o.group(1))):
        year_attempts.append(attempt.makeAttempt(o.group(1), 50))


    year = attempt.getMostCertain(year_attempts)
    title = attempt.getMostCertain(title_attempts)

    title.result = utils.cleanString(title.result)

    data = {'title' : title.result,
            'year' : year.result}

    return data

def isTV(tv_info, full_path):
    
    if (tv_info['season_number'] is None or tv_info['season_number'] is ''):
        return 0
    else:
        return 1
