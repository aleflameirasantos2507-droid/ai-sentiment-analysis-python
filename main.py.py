from textblob import TextBlob
from deep_translator import GoogleTranslator


def analyze_polarity(text):
    translated_text = GoogleTranslator(source='auto', target='en').translate(text)
    analysis = TextBlob(translated_text)
    return analysis.sentiment.polarity


def analyze_input(prompt):
    positive = []
    negative = []
    neutral = []

    while True:
        text = input(prompt)

        if text.lower().strip() == 'exit':
            total = len(positive) + len(negative) + len(neutral)

            try:
                print('=' * 30 + ' FINAL REPORT ' + '=' * 30)
                print(f"--> Positive sentences: {len(positive)} [{(len(positive) / total) * 100:.2f}%]")
                print(f"--> Negative sentences: {len(negative)} [{(len(negative) / total) * 100:.2f}%]")
                print(f"--> Neutral sentences: {len(neutral)} [{(len(neutral) / total) * 100:.2f}%]")
            except ZeroDivisionError:
                return "No sentences were entered."

            return '=' * 30 + ' PROGRAM FINISHED ' + '=' * 30

        score = analyze_polarity(text)

        if score > 0:
            print(f"SENTIMENT: Positive [score: {score:.2f}]")
            positive.append('positive')

        elif score < 0:
            print(f"SENTIMENT: Negative [score: {score:.2f}]")
            negative.append('negative')

        else:
            print(f"SENTIMENT: Neutral [score: {score:.2f}]")
            neutral.append('neutral')


def analyze_file(prompt):
    file_name = input(prompt)

    positive = []
    negative = []
    neutral = []

    try:
        with open(file_name, 'r') as file:
            for line in file:
                sentence = line.strip()

                if sentence == '':
                    continue

                score = analyze_polarity(sentence)

                if score > 0:
                    positive.append('positive')
                    result = 'Positive'

                elif score < 0:
                    negative.append('negative')
                    result = 'Negative'

                else:
                    neutral.append('neutral')
                    result = 'Neutral'

                print(f'Sentence: "{sentence}" → Sentiment: {result} [score: {score:.2f}]')

    except FileNotFoundError:
        print("File not found.")

    total = len(positive) + len(negative) + len(neutral)

    try:
        print('=' * 30 + ' FINAL REPORT ' + '=' * 30)
        print(f"--> Positive sentences: {len(positive)} [{(len(positive) / total) * 100:.2f}%]")
        print(f"--> Negative sentences: {len(negative)} [{(len(negative) / total) * 100:.2f}%]")
        print(f"--> Neutral sentences: {len(neutral)} [{(len(neutral) / total) * 100:.2f}%]")
    except ZeroDivisionError:
        print("No sentences were analyzed.")


print('=' * 20 + ' SENTIMENT ANALYZER ' + '=' * 20)

option = input("Choose an option:\n[1] Enter sentences\n[2] Analyze file\n")

while True:
    if option == '1':
        result = analyze_input("Enter a sentence (type 'exit' to finish): ")
        print(result)
        break

    elif option == '2':
        analyze_file("Enter the file name to analyze: ")
        break

    else:
        option = input("Enter a valid option: ")