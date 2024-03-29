import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response = False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=None):
        if required_words is None:
            required_words = []
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Response ---------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    # ... (existing code)

    # Additional Responses -----------------------------------------

    # Greeting responses
    response('Hi there!', ['hi', 'hello', 'hey', 'greetings'], single_response=True)
    response('Greetings!', ['greetings', 'salutations', 'hello'], single_response=True)

    # Farewell responses
    response('Farewell!', ['goodbye', 'bye', 'see', 'you', 'later'], single_response=True)
    response('Take care!', ['take', 'care'], single_response=True)

    # Responses about the bot
    response('I am a chatbot!', ['what', 'are', 'you'], required_words=['what', 'you', 'are'])

    # Responses to gratitude
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('No problem!', ['no', 'problem'], single_response=True)

    # Responses to compliments
    response('Thank you!', ['you', 'are', 'awesome'], required_words=['you', 'are', 'awesome'])
    response('I appreciate it!', ['nice', 'work'], required_words=['nice', 'work'])

    # Custom longer responses
    response('Sure! Here\'s some advice: ' + long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response('I don\'t eat, but I can help you find great recipes!', ['what', 'you', 'eat'],
             required_words=['you', 'eat'])

    # ... (existing code)

    # Additional Responses -----------------------------------------

    # Responses to questions about the bot's capabilities
    response('I can assist with various queries. Try asking me about programming or general knowledge!',
             ['what', 'can', 'you', 'do'], required_words=['what', 'can', 'you', 'do'])
    response('I\'m here to chat and provide information. Ask me anything!',
             ['who', 'are', 'you'], required_words=['who', 'are', 'you'])

    # Responses to expressions of curiosity
    response('Curiosity is a great trait! Feel free to ask me anything you want to know.',
             ['curious', 'tell', 'me'], required_words=['curious', 'tell', 'me'])

    # Responses to expressions of frustration
    response('I understand, sometimes things can be frustrating. How can I assist you?',
             ['frustrating', 'help'], required_words=['frustrating', 'help'])


    # Responses to expressions of excitement
    response('That sounds exciting! Tell me more about it.',
             ['excited', 'amazing', 'awesome'], required_words=['excited', 'amazing', 'awesome'])

    # Responses to weather-related queries
    response('I don\'t have real-time weather information, but I can help you find weather forecasts online.',
             ['weather', 'today'], required_words=['weather', 'today'])

    # Responses to time-related queries
    response('I don\'t have the current time, but I can help you with various tasks. What do you need assistance with?',
             ['what', 'time', 'is', 'it'], required_words=['what', 'time', 'is', 'it'])

    # ... (existing code)

    # Responses to health-related queries ---------------------------------

    # General health advice
    response(
        'I am not a doctor, but I can provide general health tips. For personalized advice, please consult a healthcare professional.',
        ['health', 'advice'], required_words=['health', 'advice'])

    # Encouragement to seek professional help

    # Mental health support
    response(
        'Taking care of your mental health is crucial. If you need someone to talk to, consider reaching out to a mental health professional.',
        ['mental', 'health', 'support'], required_words=['mental', 'health', 'support'])

    # Fitness motivation
    response(
        'Regular exercise is beneficial for overall health. Find an activity you enjoy, and remember to consult a fitness expert if needed.',
        ['exercise', 'fitness'], required_words=['exercise', 'fitness'])

    # Nutrition advice
    response(
        'Maintaining a balanced diet is important. Include a variety of fruits, vegetables, and whole grains for a healthy lifestyle.',
        ['nutrition', 'diet'], required_words=['nutrition', 'diet'])

    # Encouragement for self-care
    response(
        'Remember to prioritize self-care. Whether it\'s getting enough sleep or taking breaks, taking care of yourself is essential.',
        ['self-care', 'well-being'], required_words=['self-care', 'well-being'])

    # ... (existing code)

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

while True:
    print('Bot: ' + get_response(input('You: ')))
