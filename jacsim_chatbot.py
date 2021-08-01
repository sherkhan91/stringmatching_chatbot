import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import sys
import json
from nltk.corpus import wordnet


# return synonym 
def check_synonyms(word):
    synList = []
    syns = wordnet.synsets(word)
    # for syn in wordnet.synsets(word):
    #     for l in syn.lemmas():
    #         synList.append(l.name())
    return set(syns)

#PRE PROCESSING-
def pre_process(my_str):
    # define punctuation
    punctuations = string.punctuation
    # remove punctuation from the string
    no_punct = ""
    for char in my_str:
        if char not in punctuations:
            no_punct = no_punct + char
    # removing stop words
    text_tokens = word_tokenize(no_punct)
    # print(text_tokens)
    all_stop_words = stopwords.words('english')
    text_without_sw = []
    for word in text_tokens:
        if word not in all_stop_words:
            text_without_sw.append(word)
    lemmatized = []
    lemmatizer = WordNetLemmatizer()
    for word in text_without_sw:
        lemma = lemmatizer.lemmatize(word)
        lemmatized.append(lemma)

    return lemmatized

#jaccard similarity
def jaccard_similarity(s1, s2):
    return len(s1.intersection(s2)) / len(s1.union(s2))

#read the questions
def questions():
    question_list=[]
    # questions
    d1 = 'how many legs a chair has?'
    d2 = 'by which material a chair made?'
    d3 = 'can you please show me a chair how it looks like?'
    question_list.append(d1)
    question_list.append(d2)
    question_list.append(d3)
    return question_list

#answers are here
def answers():
    answer_list=[]
    #Answers
    a1='Normally a chair has 4 legs'
    a2='a chair is made of many materials like plastic,wood,fiber or even iron'
    a3='yes sure, pleae click the link below to see a chair\n https://www.google.com/search?q=chair+pic&sxsrf=ALeKk02uzUFS2I0MYWw8pmfKSoMH8isDPQ:1601620591806&tbm=isch&source=iu&ictx=1&fir=Q0EnJDixgu7fOM%252C3efLBuczeeaJNM%252C_&vet=1&usg=AI4_-kRRBAOl_iAeC2Zo2Cz9jVyvzRSpZg&sa=X&ved=2ahUKEwil1cHTpZXsAhWSTcAKHXzpBvAQ9QF6BAgKEFk#imgrc=Q0EnJDixgu7fOM'

    answer_list.append(a1)
    answer_list.append(a2)
    answer_list.append(a3)
    return answer_list

#global variable
stored_score=0


#final similarity check is being done here
def check_similarity(asked_question):
    similarity_score_among_questions_list=[]
    all_questions = questions()
    all_answers = answers()
    s1 = pre_process(asked_question)
    for i in range(len(all_questions)):
        s2 = pre_process(all_questions[i])
        s1 = set(s1)
        s2 = set(s2)
        a = jaccard_similarity(s1, s2)
        a=(int(round(a * 100)))
        similarity_score_among_questions_list.append(a)
        # print(similarity_score_among_questions_list)
        # stored_score += int(round(a * 100))
        # stored_score = stored_score / len(question_list)
    confidence_level= int(max(similarity_score_among_questions_list))
    indexx=similarity_score_among_questions_list.index(confidence_level)
    # print("final",confidence_level,"\n found similar with question# ",indexx)
    #
    # print("Most similar Question is: ",question_list[indexx],"                    with the         confidence of",confidence_level)
    # print("Most similar Answer is:          ",answer_list[indexx])
    #
    returnList = []
    if confidence_level > 30:
        returnList.append("Most Similar Question: "+all_questions[indexx])
        returnList.append("Confidence Level: "+str(confidence_level))
        returnList.append("Answer: "+all_answers[indexx])
    else:
        returnList.append("Sorry the question is n")



    result_json = json.dumps(returnList)
    print(result_json)
    return result_json


#Main testing function
#------------
#user_question= sys.argv[1]
user_question = input("Please ask a question:  ")
# user_question = "how many legs a chair has"
check_similarity(user_question)

