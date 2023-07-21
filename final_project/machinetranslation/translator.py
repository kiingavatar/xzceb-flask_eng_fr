"""
This python file is define to translator using libray deep_translator and mymemorytransalator
"""

from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    """
    This function is convert english text to french text
    """
    #write the code here
    frenchText = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    """
    This function is used convert french text to english text
    """
    #write the code here
    englishText = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(frenchText)
    return englishText

