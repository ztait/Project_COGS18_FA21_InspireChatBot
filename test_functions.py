"""COGS 18 Project Test Functions."""

# Imports
from functions import end_chat, greeting_selector, result_counter, question_selector, quote_selector, quote_feed

def test_end_chat():
    """Test end_chat function."""
    assert callable(end_chat)
    assert isinstance(end_chat(["quit"])[0], str)
    assert isinstance(end_chat(["quit"])[1], bool)
    assert end_chat(["quit"])[0] == "Thank you for speaking with me today! " + \
    "Hope to see you again next time!"
    assert end_chat(["quit"])[1] is False
    assert end_chat(["hi"])[0] is None
    assert end_chat(["hi"])[1] is True

def test_greeting_selector():
    """Test greeting_selector function."""
    assert callable(greeting_selector)
    assert isinstance(greeting_selector(["hi"],
                                        ["hi", "hello", "good morning"],
                                        "Welcome! Hi!"), str)
    assert greeting_selector(["hi"],
                             ["hi", "hello", "good morning"],
                             "Welcome! Hi!") == "Welcome! Hi!"
    assert greeting_selector(["hello"],
                             ["hi", "hello", "good morning"],
                             "Welcome! Hi!") == "Welcome! Hi!"
    assert greeting_selector(["bye"],
                             ["hi", "hello", "good morning"],
                             "Welcome! Hi!") is None

def test_result_counter():
    """Test result_counter function."""
    assert callable(result_counter)
    assert isinstance(result_counter(["True"], 0), int)
    assert result_counter(["false"], 1) == 1
    assert result_counter(["true"], 3) == 4
    assert result_counter(["hi"], 4) == 4
    assert result_counter(["truetrue"], 0) == 0

def test_question_selector():
    """Test question_selector function."""
    assert callable(question_selector)
    assert isinstance(question_selector(["true"],
                                        ["ready", "true"],
                                        ["How are you?",
                                         "Are you okay?"]), str)
    assert question_selector(["true"],
                             ["ready", "true"],
                             ["How are you?",
                              "Are you okay?"]) == "How are you?"
    assert question_selector(["true"],
                             ["ready", "true"],
                             []) is None
    assert question_selector(["hi"],
                             ["ready", "true"],
                             ["How are you?",
                              "Are you okay?"]) is None

def test_quote_selector():
    """Test quote_selector function."""
    assert callable(quote_selector)
    assert isinstance(quote_selector(["hi"],
                                     ["hi", "bye"],
                                     3,
                                     ["Hello World!",
                                      "Happy Day",
                                      "Happy Happy!"]), str)
    assert quote_selector(["quote"],
                          ["quote"],
                          0,
                          ["Great 1!",
                           "Great 2!",
                           "Great 3!",
                           "Great 4!",
                           "Great 5!"]) == "Great 1!"
    assert quote_selector(["quote"],
                          ["quote"],
                          5,
                          ["Great 1!",
                           "Great 2!",
                           "Great 3!",
                           "Great 4!",
                           "Great 5!"]) == "Great 3!"
    assert quote_selector(["quote"],
                          ["quote"], 7,
                          ["Great 1!",
                           "Great 2!",
                           "Great 3!",
                           "Great 4!",
                           "Great 5!"]) == "Great 4!"
    assert quote_selector(["quote"],
                          ["quote"],
                          10,
                          ["Great 1!",
                           "Great 2!",
                           "Great 3!",
                           "Great 4!",
                           "Great 5!"]) == "Great 5!"
    assert quote_selector(["hi"],
                          ["quote"],
                          10,
                          ["Great 1!",
                           "Great 2!",
                           "Great 3!",
                           "Great 4!",
                           "Great 5!"]) is None

def test_quote_feed():
    """Test quote_feed function."""
    assert callable(quote_feed)
    assert isinstance(quote_feed(["yes"],
                                 "Good Job!",
                                 "Bad Job!"), str)
    assert quote_feed(["yes"],
                      "Good Job!",
                      "Bad Job!") == "Good Job!"
    assert quote_feed(["no"],
                      "Good Job!",
                      "Bad Job!") == "Bad Job!"
    assert quote_feed(["hi"],
                      "Good Job!",
                      "Bad Job!") is None