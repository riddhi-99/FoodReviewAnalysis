import os
import numpy as np
from Utility.review import Review
from Utility.reviewsentimentscore import ReviewSentimentScore
from datetime import datetime
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from pprint import pprint
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tqdm import tqdm
import time

#start_time = time.time()

analyzer = SentimentIntensityAnalyzer()

current_working_directory = os.getcwd() 
current_working_directory = current_working_directory + "\\data\\foods.txt"
text = ''

for i in tqdm (range (101), 
               desc="Loading…", 
               ascii=False, ncols=75):
    time.sleep(0.01)     


with open(current_working_directory) as f:
    text = f.read()   
print("Processing food data...")
reviews = text.split('\n\n')
ListReview = []
for review in reviews:
    lines = review.split('\n')
    score = 0
    summary = ""
    text = ""
    year = 0
    for line in lines:
        if line.__contains__("review/score:"):
            score = line.replace("review/score:","")
        elif line.__contains__("review/summary:"):
            summary = line.replace("review/summary:","")  
        elif line.__contains__("review/text:"):
            text = line.replace("review/text:","")
        elif line.__contains__("review/time:"):
            time = line.replace("review/time:","")
            year = datetime.fromtimestamp(int(time)).year  

    ListReview.append(Review(score,summary,text,year)) 
ListSentimentScore = []
insight_dict = {} ##
for review in ListReview:
    rating = review.score
    year = review.year
    
    Score = analyzer.polarity_scores(review.summary)
    summaryScore = Score["compound"]
    Score = analyzer.polarity_scores(review.text)
    textScore = Score["compound"]
    ListSentimentScore.append(ReviewSentimentScore(rating,summaryScore,textScore,year))

##############
distinct_year = set([review.year for review in ListSentimentScore])
for dyear in distinct_year:
    s_score = [review.summaryScore for review in ListSentimentScore if review.year == dyear]
    s_score_positive = [review.summaryScore for review in ListSentimentScore if review.year == dyear and review.summaryScore >0.5]
    s_score_negetive = [review.summaryScore for review in ListSentimentScore if review.year == dyear and review.summaryScore < -0.5]
    s_score_nutral = [review.summaryScore for review in ListSentimentScore if review.year == dyear and review.summaryScore > -0.5 and review.summaryScore < 0.5]
    s_score_avg = sum(s_score)/len(s_score)
    s_score_max = max(s_score)
    s_score_min = min(s_score)

    t_score = [review.textScore for review in ListSentimentScore if review.year == dyear]
    t_score_positive = [review.textScore for review in ListSentimentScore if review.year == dyear and review.textScore >0.5]
    t_score_negetive = [review.textScore for review in ListSentimentScore if review.year == dyear and review.textScore < -0.5]
    t_score_nutral = [review.textScore for review in ListSentimentScore if review.year == dyear and review.textScore > -0.5 and review.textScore < 0.5]
    t_score_avg = sum(t_score)/len(t_score)
    t_score_max = max(t_score)
    t_score_min = min(t_score)

    ratings = [review.rating for review in ListSentimentScore if review.year == dyear]
    ratings_dict = {}
    for r in ratings:
        if r in ratings_dict:
            ratings_dict[r] += 1
        else:
            ratings_dict[r] = 1

    insight_dict[dyear] = {"ratings": ratings_dict,
                           "summary_score_positive_count" : len(s_score_positive),
                           "summary_score_negetive_count" : len(s_score_negetive),
                           "summary_score_nutral_count" : len(s_score_nutral),
                           "summary_score_max": s_score_max,
                            "summary_score_min": s_score_min,
                            "summary_score_avg": s_score_avg,
                            "text_score_positive_count" : len(t_score_positive),
                            "text_score_negetive_count" : len(t_score_negetive),
                            "text_score_nutral_count" : len(t_score_nutral),
                            "text_score_max": t_score_max,
                            "text_score_min": t_score_min,
                            "text_score_avg": t_score_avg}


def barGrapPlot(xAxis, yAxis_s,yAxis_t, title):
    X_axis = np.arange(len(xAxis)) 
    plt.bar(X_axis - 0.2,yAxis_s,0.4,label = "Title")
    plt.bar(X_axis + 0.2,yAxis_t,0.4,label = "Review")
    plt.xticks(X_axis, xAxis) 
    plt.title(title)
    plt.legend()
    plt.show()

#end_time = time.time()
#elapsed_time = start_time - end_time
#2print(elapsed_time.strftime('%H:%M:%S'))
print("Complete.")
option = input("Choose Option:\n1.Words based on rating\n2.Insight based on year\n")    
if(option == "1"):
    rating = input("Ente rating between 1 to 5:\n")
    stopwords = set(STOPWORDS)
    stopwords.update(["Amazon", "Product", "br"])
    all_rating_1 = " ".join([review.text for review in ListReview if review.score== " "+rating+".0"])
    wordcloud_rating_1 = WordCloud(stopwords=stopwords, background_color="white").generate(all_rating_1)
    plt.imshow(wordcloud_rating_1, interpolation='bilinear')
    plt.axis("off")
    plt.show()
elif(option == "2"):
    year = int(input("Ente year between 1999 to 2012:\n"))
    xAxis  = ["Positive","Negetive", "Nutral"]
    yAxis_s = [insight_dict[year]["summary_score_positive_count"],insight_dict[year]["summary_score_negetive_count"],insight_dict[year]["summary_score_nutral_count"]]
    yAxis_t = [insight_dict[year]["text_score_positive_count"],insight_dict[year]["text_score_negetive_count"],insight_dict[year]["text_score_nutral_count"]]
    barGrapPlot(xAxis,yAxis_s,yAxis_t,year)
else:
    print("Please choose a correct option.")


###################