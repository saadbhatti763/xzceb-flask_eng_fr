from deep_translator import MyMemoryTranslator


def englishtofrench(englishtext):
    '''This function translates the input to French'''

    frenchtext = MyMemoryTranslator(source = 'english', target = 'french').translate(englishtext)
    return frenchtext


def frenchtoenglish(frenchtext):
    '''This function translates the input to English'''

    englishtext = MyMemoryTranslator(source = 'french', target = 'english').translate(frenchtext)
    return englishtext