import re
from collections import defaultdict
import pkg_resources


AR_CMUDICT_DICT = 'data/haraka_moshakal.dic'
AR_CMUDICT_PHONES = 'data/haraka.phone'


def _string(resource_name):
    string = pkg_resources.resource_string(__name__, resource_name)
    return string


def _stream(resource_name):
    stream = pkg_resources.resource_stream(__name__, resource_name)
    return stream

def _entries(stream):
    entries = []
    for line in stream:
        parts = line.decode('utf-8').strip().split()
        thing = re.sub(r'\(\d+\)$', '', parts[0])
        entries.append((thing, parts[1:]))
    return entries


def dict():
    """
    Compatibility with NLTK.
    Returns the ar_cmudict lexicon as a dictionary, whose keys are
    lowercase words and whose values are lists of pronunciations.
    """
    default = defaultdict(list)
    for key, value in entries():
        default[key].append(value)
    return default


def dict_stream():
    """Return a readable file-like object of the ar_cmudict.dict file."""
    stream = _stream(AR_CMUDICT_DICT)
    return stream


def dict_string():
    """Return the contents of ar_cmudict.dict as a string."""
    string = _string(AR_CMUDICT_DICT)
    return string



def phones():
    phones = []
    for line in phones_stream():
        parts = line.decode('utf-8').strip().split()
        phones.append((parts[0], parts[1:]))
    return phones


def phones_stream():
    """Return a readable file-like object of the ar_cmudict.phones file."""
    s = _stream(AR_CMUDICT_PHONES)
    return s


def phones_string():
    """Return the contents of ar_cmudict.phones as a string."""
    string = _string(AR_CMUDICT_PHONES)
    return string


def entries():
    """
    Returns the ar_cmudict lexicon as a list of entries
    containing (word, transcriptions) tuples.
    """
    entries = _entries(dict_stream())
    return entries



def words():
    """
    Compatibility with NLTK.
    Returns a list of all words defined in the ar_cmudict lexicon.
    """
    return [word.lower() for (word, _) in entries()]
