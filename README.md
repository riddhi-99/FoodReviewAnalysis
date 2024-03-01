# AMAZON  Food Review SENTIMENT Analysis
This Python program performs sentiment analysis on Amazon food reviews collected from the years 1999 to 2012. It extracts relevant data from these reviews and provides insights through graphical visualization and key term analysis.
We encounter such huge texts of documents time and again. But, before reading the documents, if we can get an overview of what the documents are about, it would make the job so much easy. For example, before watching a movie, if we can watch its trailer, it can help us decide if the movie is worth it. Similarly, we can decide if the documents are worth the effort?

Or, alternatively, if we have a bunch of documents and we can identify each document with their "topic", we can shortlist the documents based on topic of interest - without having to read through all the documents.

In Machine Learning and Natural Language Processing, Topic Models, a type of statistical model, gives us the ability to discover topics from a collection of documents.
# DATA

For the project, I used publicly available Amazon's Fine Food reveiws data. It can be accessed [here](https://drive.google.com/file/d/1yWRbzKPlvkYzhBT--_wdlnq8JdYsjRHg/view?usp=drive_link). The data contains approx. 569,000 reviews from 256,000 users.

The sample can be checked from here : ![data](https://github.com/riddhi-99/FoodReviewAnalysis/assets/72509965/b5ad445b-6367-4027-ae7b-f806bef88e5c)
# Text Normalization

Cleaning the textual data was very important to get good topics from the reviews. The process involved following steps:

* Removing HTML tags
* Correcting grammar contractions
* Lowercasing the reviews
* Removing numbers and additional white spaces
* Removing Punctuations
* Tokenization
* Remving stopwords (using a long list of words from rank.nl and domain specific words)
* Removing Whitespaces
* Lemmatizing all reviews
* # Installation Steps
* Install the required dependencies:
*     pip install wordcloud
      pip install STOPWORDS
      pip install Review
      pip install tqdm
  # Usage
  python main.py
  # Modelling
- **Data Collection**: Automatically fetches Amazon food reviews from the specified time period.
- **Sentiment Analysis**: Utilizes Natural Language Processing techniques to analyze the sentiment of each review.
- **Graphical Insights**: Generates bar graphs to visualize the distribution of ratings and their corresponding sentiment.
- **Key Term Analysis**: Identifies the most frequently occurring words associated with positive and negative reviews.
  # Results
After running the program, you'll get:

Bar graphs depicting the distribution of ratings and sentiment.
Key terms associated with positive and negative reviews.
 # Example
Here's a sample output:
![Picture1](https://github.com/riddhi-99/FoodReviewAnalysis/assets/72509965/8d25850c-8fc9-4c75-8229-59e7927c655a)
![Picture2](https://github.com/riddhi-99/FoodReviewAnalysis/assets/72509965/6c4b5456-a4f2-41b1-84a9-39493c0def1f)
 # Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow the standard GitHub flow:

Fork the repository
Create a new branch (git checkout -b feature/new-feature)
Make your changes
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature/new-feature)
Create a new Pull Request

# Conclusion
In conclusion, this Amazon Food Reviews Sentiment Analysis project provides a comprehensive solution for extracting, analyzing, and visualizing sentiment from Amazon food reviews spanning from 1999 to 2012. By leveraging Natural Language Processing techniques, it offers valuable insights into customer opinions and preferences regarding food products on Amazon.

Through the collection of relevant data, sentiment analysis, and graphical visualization, users gain a deeper understanding of customer sentiments towards various food products. The generated bar graphs illustrate the distribution of ratings and sentiment, enabling users to identify trends and patterns over time.

Moreover, the key term analysis highlights the most commonly occurring words associated with positive and negative reviews, offering actionable insights for product manufacturers and sellers to improve their offerings and customer satisfaction.

Overall, this project serves as a valuable tool for researchers, businesses, and anyone interested in understanding customer sentiments in the food domain on Amazon during the specified time period. Contributions and feedback are welcome to further enhance the functionality and usefulness of this project.






