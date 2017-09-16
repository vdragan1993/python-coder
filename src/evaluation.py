import ast
from nltk.translate import bleu_score


def code_compiles(code):
    """
    Check if given Python code compiles
    :param code: Python source code as string
    :return: True or False
    """
    try:
        ast.parse(code)
    except SyntaxError:
        return False
    return True


def calculate_bleu(original, translated):
    """
    Calculates BLEU score for translated code
    :param source: original source code string
    :param translated: translated source code string
    :return: BLEU score
    """
    hypothesis = list(translated)
    reference = list(original)
    return bleu_score.sentence_bleu([reference], hypothesis)
