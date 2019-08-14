import numpy as np
import pandas as pd
import os
import time
import pyttsx3
import newspaper

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("rate", 150)

df = pd.read_csv(r"C:\Users\Mahe\Dropbox (Who cares)\GRE\Margesh_Dictionary.csv", encoding="ISO-8859-1")
data = np.array(df[['Word', 'Definition', 'Example', 'Comfort', 'Synonyms']])
df.head()
name = data[:, 0]
defs = data[:, 1]
examples = data[:, 2]
comfort = data[:, 3]
max_comfort = np.amax(comfort)
synonyms = data[:, 4]
Is_right_flag = False

session_correct_counter = 0
session_wrong_counter = 0
voice_mode_on = False


def question_mark_voice():
    IsRight = False
    global session_correct_counter
    global session_wrong_counter
    global voice_mode_on
    global Is_right_flag
    global engine

    while (1):
        l = np.random.randint(0, len(name) - 1)
        correct_comfort = comfort[l]

        if (np.random.randint(0, round(max_comfort) + 2) - correct_comfort > 0):
            continue
        else:
            break

    correct_name = name[l]
    correct_def = defs[l]
    correct_example = examples[l]
    correct_synonyms = synonyms[l]
    options = np.array([correct_def])

    voice_rand_id = np.random.randint(0, len(voices) - 1)
    engine.setProperty('voice', voices[voice_rand_id].id)  # changes the voice
    engine.say(correct_name)
    engine.runAndWait()

    while (IsRight == False):
        print("Enter 10 to toggle voice mode. Enter 20 to view the word list.")
        print("Enter 30 to repeat the word.")
        answer_in = input("Enter the spelling - ")
        try:
            if (int(answer_in) == 10):
                if (voice_mode_on):
                    voice_mode_on = False
                    break
                else:
                    voice_mode_on = True

            if (int(answer_in) == 30):
                engine.say(correct_name)
                engine.runAndWait()

            elif (int(answer_in) == 20):
                print(df[['Word', 'Definition', 'Comfort']].to_string())

            elif (int(answer_in) == 0):
                break

        except:
            if (answer_in.lower() == correct_name.lower()):
                df.at[l, 'Comfort'] = df.at[l, 'Comfort'] + 0.25
                print("\nBingo")
                print("\nName", name[l])
                print("\nDefinition", defs[l])
                print("\nSynonyms - ", correct_synonyms)
                session_correct_counter = session_correct_counter + 1
                # print("Correct Answers - ", session_correct_counter)
                # print("Wrong answer - ", session_wrong_counter)
                options = []
                IsRight = True
                Is_right_flag = True
            else:
                print("Try Again?")
                df.at[l, 'Comfort'] = df.at[l, 'Comfort'] - 0.5
                session_wrong_counter = session_wrong_counter + 1

    IsRight = False
    try:
        return int(answer_in), correct_name
    except:
        return answer_in, correct_name


def question_mark_name():
    IsRight = False
    global session_correct_counter
    global session_wrong_counter
    global voice_mode_on
    global Is_right_flag

    while (1):
        l = np.random.randint(0, len(name) - 1)
        correct_comfort = comfort[l]

        if (np.random.randint(0, round(max_comfort) + 2) - correct_comfort > 0):
            continue
        else:
            break

    correct_name = name[l]
    correct_def = defs[l]
    correct_example = examples[l]
    correct_synonyms = synonyms[l]
    options = np.array([correct_def])

    while (len(options) < 5):
        opt = np.random.randint(0, len(name) - 1)
        if opt == l:
            opt = np.random.randint(0, len(name) - 1)
        options = np.append(options, defs[opt])
        #   print(options)
        np.random.shuffle(options)
    #   print(options)
    while (IsRight == False):
        print(correct_name)
        print("Options - ")
        opt_ctr = 1
        for option in options:
            print(str(opt_ctr) + ")", option)
            opt_ctr = opt_ctr + 1
        print("Enter 10 to toggle voice mode. Enter 20 to view the word list.")
        while (1):
            try:
                answer_in = int(input("Enter the option number or enter 0 to quit : "))
                break
            except:
                print("Please retry with proper input.")

        if (answer_in == 10):
            if (voice_mode_on):
                voice_mode_on = False
            else:
                voice_mode_on = True
        elif (answer_in == 20):
            print(df[['Word', 'Definition', 'Comfort']].to_string())

        elif (answer_in == 0):
            break

        elif (str(options[answer_in - 1]) == correct_def):
            df.at[l, 'Comfort'] = df.at[l, 'Comfort'] + 0.25
            print("\nBingo")
            print("\nSynonyms - ", correct_synonyms)
            session_correct_counter = session_correct_counter + 1
            # print("Correct Answers - ", session_correct_counter)
            # print("Wrong answer - ", session_wrong_counter)
            options = []
            IsRight = True
            Is_right_flag = True

        else:
            if (answer_in < 6 and answer_in > 0):
                print("Try Again?")
                df.at[l, 'Comfort'] = df.at[l, 'Comfort'] - 0.5
                session_wrong_counter = session_wrong_counter + 1
            else:
                print("Invalid input.")

    IsRight = False
    return answer_in, correct_name


def question_mark_def():
    IsRight = False
    global session_correct_counter
    global session_wrong_counter
    global voice_mode_on
    global Is_right_flag

    while (1):
        l = np.random.randint(0, len(name) - 1)
        correct_comfort = comfort[l]

        if (np.random.randint(0, round(max_comfort) + 2) - correct_comfort > 0):
            break
        else:
            continue

    correct_name = name[l]
    correct_def = defs[l]
    correct_example = examples[l]

    correct_synonyms = synonyms[l]
    options = np.array([correct_name])

    # for i in range(0,4):
    while (len(options) < 5):
        opt = np.random.randint(0, len(name) - 1)
        if opt == l:
            opt = np.random.randint(0, len(name) - 1)
        options = np.append(options, name[opt])
        np.random.shuffle(options)
    #   print(options)
    while (IsRight == False):
        print(correct_def)
        print("Options - ")
        opt_ctr = 1
        for option in options:
            print(str(opt_ctr) + ")", option)
            opt_ctr = opt_ctr + 1
        print("Enter 10 to toggle voice mode. Enter 20 to view the word list.")
        while (1):
            try:
                answer_in = int(input("Enter the option number or enter 0 to quit : "))
                break
            except:
                print("Please retry with proper input.")

        if (answer_in == 10):
            if (voice_mode_on):
                voice_mode_on = False
            else:
                voice_mode_on = True
        elif (answer_in == 20):
            print(df[['Word', 'Definition', 'Comfort']].to_string())

        elif (answer_in == 0):
            break

        elif (str(options[answer_in - 1]) == correct_name):
            df.at[l, 'Comfort'] = df.at[l, 'Comfort'] + 0.25
            print("\nBingo")
            print("\nSynonyms - ", correct_synonyms)
            session_correct_counter = session_correct_counter + 1
            # print("Correct Answers - ", session_correct_counter)
            # print("Wrong answer - ", session_wrong_counter)
            options = []
            IsRight = True
            Is_right_flag = True

        else:
            if (answer_in < 6 and answer_in > 0):
                print("Try Again?")
                df.at[l, 'Comfort'] = df.at[l, 'Comfort'] - 0.5
                session_wrong_counter = session_wrong_counter + 1

    IsRight = False
    return answer_in, correct_name


while (1):
    question_type = np.random.randint(0, 150)
    if (question_type > 125 and voice_mode_on == True):
        answer = question_mark_voice()
    elif (question_type > 75):
        answer = question_mark_name()
    else:
        answer = question_mark_def()

    df.to_csv(r"C:\Users\Mahe\Dropbox (Who cares)\GRE\Margesh_Dictionary.csv", index=False)
    ##  clear_output()
    if (voice_mode_on == True and answer[0] != 0):
        voice_rand_id = np.random.randint(0, len(voices) - 1)
        engine.setProperty('voice', voices[voice_rand_id].id)  # changes the voice
        engine.say(answer[1])
        engine.runAndWait()
    if (Is_right_flag == True and voice_mode_on == False):
        input("\n \n Enter anything to continue")
        Is_right_flag = False

    os.system('cls')
    time.sleep(0.7)

    if (answer[0] == 0):
        print("Correct Answers - ", session_correct_counter)
        print("Wrong answer - ", session_wrong_counter)
        break



