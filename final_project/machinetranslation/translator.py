from deep_translator import MyMemoryTranslator


def english_to_french(englishtext):
    '''This function translates the input to French'''

    frenchtext = MyMemoryTranslator(source = 'english', target = 'french').translate(englishtext)
    return frenchtext


def french_to_english(frenchtext):
    '''This function translates the input to English'''

    englishtext = MyMemoryTranslator(source = 'french', target = 'english').translate(frenchtext)
    return englishtext