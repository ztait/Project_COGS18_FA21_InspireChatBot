"""COGS 18 Project Functions."""

import string
import random
import nltk

# From A3
def remove_punctuation(input_string):
    """Removes punctuation from the input words.

    Parameters
    ----------
    input_string : str
        user input words

    Returns
    -------
    out_string : str
        resulting string with punctuation removed
    """

    out_string = ''

    # loops through each character in input
    for character in input_string:
        # if character is not in string.punctuation
        if character not in string.punctuation:
            # concatenate current character to output string
            out_string += character

    return out_string

# From A3
def prepare_text(input_string):
    """Prepare text input into list by making all characters lowercase,
        removing punctuation, and splitting words.

    Parameters
    ----------
    input_string : str
        user input words

    Returns
    -------
    out_list : list
        result of making words lowercase, removing punctuation,
        and splitting input words
    """

    out_list = []

    # make string all lowercase and assign to variable
    temp_string = input_string.lower()

    # remove punctuation from new string
    #  using remove_punctuation function previously defined
    #   and assign to variable
    temp_string = remove_punctuation(temp_string)

    # split string into words and assign to variable
    out_list = temp_string.split()

    return out_list

# From Lecture Notes 20
def get_input():
    """Ask user for an input message.

    Returns
    -------
    msg : str
        'input' as output
    out_msg : None
        None as output
    """

    msg = input('INPUT :\t')
    out_msg = None

    return msg, out_msg

# From Lecture Notes 20
def end_chat(input_list):
    """Identify if user says 'quit' in input and end chat.

    Parameters
    ----------
    input_list : list
        user input as separated words

    Returns
    -------
    output : str or None
        returned message if input includes 'quit'
        or None if if input does not include 'quit'
    chat : bool
        determines if chat is true or false to
        continue or stop chat
    """

    if "quit" in input_list:
        output = "Thank you for speaking with me today! " + \
        "Hope to see you again next time!"
        chat = False
    else:
        output = None
        chat = True

    return output, chat

# Adapted from A3
def greeting_selector(input_list, check_list, return_string):
    """Returns a message if an element from the user input
        is in the predetermined check list.

    Parameters
    ----------
    input_list : list
        user input as separated words
    check_list : list
        checked list to determine if output should be returned
    return_string : str
        output to be returned if input is in checked list

    Returns
    -------
    output : str or None
        return string input as output
        or None if input not in checked list
    """

    output = None

    # loops through input list
    for element in input_list:
        if element in check_list:
            output = return_string
            break

    return output

def result_counter(input_list, running_total):
    """Produces a running sum that keeps count of how many times a
        user inputs 'true' that will determine quote selection.

    Parameters
    ----------
    input_list : list
        user input as separated words checked for 'true'
    running_total : int
        running sum determined by user input

    Returns
    -------
    running_total : int
        updated running sum
    """

    # loops through input list
    for item in input_list:
        # checks if item is 'true'
        if item == "true":
            # adds 1 to running total
            running_total += 1
        else:
            # adds 0 to running total
            #  if item not 'true'
            running_total += 0

    return running_total

# Adapted from A3
def question_selector(input_list, check_list, return_list):
    """Identifies if user's input is included in the check list
        and if the return list has a length that is not 0,
         then removes the first index from return_list if so.

    Parameters
    ----------
    input_list : list
        user input as separated words
    check_list : list
        check to determine if question output should be produced
    return_list : list
        list of questions used for indexing

    Returns
    -------
    output : string or None
        question selected or None if input not in checked list
    """

    output = None

    # loops through input list
    for element in input_list:
        # checks if element from input is in check list 
        #  and if the return list doesn't have a length of 0
        if element in check_list and len(return_list) != 0:
            # returns first index of return list
            output = return_list[0]
            # removes first index from return list
            return_list.remove(return_list[0])
        else:
            output = None

        return output

# Adapted from A3, but mainly my own code
def quote_selector(input_list, check_list, input_integer, return_list):
    """Selects a quote to output based on the input, running sum,
        and if that input matches the intended input.

    Parameters
    ----------
    input_list : list
        user input as separated words
    check_list : list
        predetermined and used to check the input before selecting output
    input_integer : int
        running sum that determines output selected
    return_list : list
        list used to select output

    Returns
    -------
    output_quote : str or None
        quote selected based on input and running sum
        or None if input not in checked list
    """

    output_quote = None

    # loops through input list
    for element in input_list:
        # checks if element from input is in check list
        if element in check_list:
            # checks if running sum is equal to 0
            if input_integer == 0:
                output_quote = return_list[0]
            elif 1 <= input_integer < 4:
                output_quote = return_list[1]
            elif 4 <= input_integer < 7:
                output_quote = return_list[2]
            elif 7 <= input_integer < 10:
                output_quote = return_list[3]
            elif input_integer == 10:
                output_quote = return_list[4]
            else:
                output_quote = None

    return output_quote

def quote_feed(input_list, return_positive, return_negative):
    """Checks if input is equal to 'yes' or 'no'
        and returns output based on that.

    Parameters
    ----------
    input_list : list
        user input as separated words
    return_positive : str
        positive output if input is 'yes'
    return_negative : str
        negative output if input is 'no'

    Returns
    -------
    output : str or None
        positive or negative output selected
        or None if input not in input list
    """

    output = None

    # loops through input list
    for item in input_list:
        if item == "yes":
            output = return_positive
            break
        if item == "no":
            output = return_negative
            break

    return output

# adapted from Lecture Notes 20 and A3, but mainly my own code
def inspire_chat_bot(result_total = 0):
    """Chatbot that takes users input, turns it into a list,
         and uses that to determine output using functions previously defined.

    Parameters
    ----------
    result_total : int, optional
        running sum, default = 0
    """

    greeting_input = ["hi",
                      "hello",
                      "hey",
                      "there",
                      "sup",
                      "good",
                      "morning"
                      "afternoon",
                      "evening",
                      "yo"]
    greeting_name_input = ["name"]

    greeting_output = "Hello there beautiful person!\n\
    My name is Happyella and I am so excited to be chatting with you today.\n\
    Who do I have the pleasure of speaking with? " + \
    "Please type the word 'name' and your name after it."
    greeting_name_output = "Wow! What a beautiful name you have.\n\
    I am so excited and honored to meet you today.\n\
    I hope you are having a wonderful day," + \
    "and if you are not I hope I can make it better for you.\n\
    \r\n\r\nToday, I am going to ask you a series of statements" + \
    "about your personality and who you are.\n\
    I encourage you to relax and answer these questions honestly, as yourself.\n\
    \r\n\r\nYou will answer each statement with EITHER 'true' or 'false' " + \
    "indicating whether you think the statement is" + \
    "True in describing you or False in describing you.\n\
    \r\nAfter 10 statements, I will give you your own personalized inspirational quote.\
    \r\n\r\nIf at any point you want to stop talking to me, please type 'quit' to exit.\
    \r\n\r\nAre you ready? Please type 'ready' to start!"

    personality_question_input_list = ["ready", "true", "false"]

    personality_question_1 = "I consider myself to have introverted qualities: " + \
    "Sometimes, I prefer to be alone and in my own company."
    personality_question_2 = "I consider myself to have extroverted qualities: " + \
    "Sometimes, I prefer to be surrounded by others in a social setting."
    personality_question_3 = "I strive to make a difference in the community " + \
    "for both myself and others. " + \
    "I want to make the world a better place through my actions and passions."
    personality_question_4 = "I like to be creative and unique. " + \
    "I prioritize expressing myself day-to-day in at least one way."
    personality_question_5 = "I value helping others rather than putting my own needs first."
    personality_question_6 = "I prefer to set goals and plan " + \
    "rather than being spontaneous most of the time."
    personality_question_7 = "I prefer to take the lead on group projects " + \
    "and generally when working with others."
    personality_question_8 = "I am not afraid of the unknown " + \
    "and I am always ready for an adventure."
    personality_question_9 = "I try to see the positive in situations, " + \
    "so when something unexpected happens I try to make the best out of it."
    personality_question_10 = "I am open with my emotions. " + \
    "I am both able to identify with what I am feeling and able to communicate that to others."

    results_directions = "Now selecting your very own personalized quote...\r\n\r\n\
    Calculating...\r\n\r\n\
    Please type 'quote' to see your quote!"

    personality_question_list = [personality_question_1,
                                 personality_question_2,
                                 personality_question_3,
                                 personality_question_4,
                                 personality_question_5,
                                 personality_question_6,
                                 personality_question_7,
                                 personality_question_8,
                                 personality_question_9,
                                 personality_question_10,
                                 results_directions]

    quote_input = ["quote"]

    quote_feedback = "Did you like the personalized quote we selected for you? " + \
    "Please type 'yes' for yes and 'no' for no."
    quote_options = ["Take a deep breath and clear your mind. " + \
                     "Know that you matter, and you will become your best self with time." + \
                     "Never stop trying, this is only the beginning.\r\n\r\n" + quote_feedback,
                     "Never. Stop. Trying. You are valued, do not forget that! " + \
                     "You are so important in this world, " + \
                     "continue pushing forward" + \
                     "and know that you will achieve great things.\r\n\r\n" + quote_feedback,
                     "Stop, look in the mirror, and smile. " + \
                     "This is you in all your beauty, " + \
                     "you are truly where you are meant to be" + \
                     "and do not forget that!\r\n\r\n" + quote_feedback,
                     "As you continue to grow and find who you are, " + \
                     "know that everything will be okay and that life is a journey. " + \
                     "Continue to be yourself " + \
                     "and take comfort in who you are.\r\n\r\n" + quote_feedback,
                     "You are such a bright light and you never fail to light up the room! " + \
                     "Keep being you in all your glory and never give up. " + \
                     "You are going to change the world.\r\n\r\n" + quote_feedback]

    positive_quote_feedback = "Wonderful! Please make sure to rate us 5 stars. " + \
    "See you next time!\r\n\r\n\
    Please type 'quit' to exit."
    negative_quote_feedback = "Oh no! We are so sorry to hear that. \n\
    Feel free to try talking to me again to get a different quote! " + \
    "See you next time!\r\n\r\n\
    Please type 'quit' to exit."

    unknown = ["I don't understand! Please follow the instructions and try again.",
               "Sorry! What? Please follow the instructions and try again."]

    chat = True

    while chat:

        # get input message from the user
        msg, out_msg = get_input()

        # check for an end msg
        out_msg, chat = end_chat(msg)

        # prepare user's input to be processed by the chatbot
        msg = prepare_text(msg)

        # calculates a running sum that identifies if the user inputs 'true' or 'false'
        result_total = result_counter(msg, result_total)

        # specify what to return
        if not out_msg:

            # initialize to collect a list of possible outputs
            outs = []

            # check if the input looks like a greeting, add a greeting output if so
            outs.append(greeting_selector(msg,
                                          greeting_input,
                                          greeting_output))

            # check if the input looks like a greeting name, add a greeting name output if so
            outs.append(greeting_selector(msg,
                                          greeting_name_input,
                                          greeting_name_output))

            # check if input looks like ready for questions
            #  or an answer to a question, add a question output if so
            outs.append(question_selector(msg,
                                          personality_question_input_list,
                                          personality_question_list))

            # check if input looks like ready for quote, add a quote output if so
            outs.append(quote_selector(msg,
                                       quote_input,
                                       result_total,
                                       quote_options))

            # check if input looks like ready for feedback , add feedback output if so
            outs.append(quote_feed(msg,
                                   positive_quote_feedback,
                                   negative_quote_feedback))

            #  might have appended None in some cases, meaning don't have a reply
            #   to deal with this, going to randomly select
            #    an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(unknown)

        print('OUTPUT:', out_msg)