import os
from datetime import  datetime, timedelta
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import pos_tag

def load_data(data_dir, start_date, end_date):
    data = {}
    cur_date = start_date
    while cur_date >= end_date:
        print 'Loading ', cur_date, '...'
        file_name = data_dir + cur_date.strftime('%Y%m%d') + '.txt'
        if os.path.exists(file_name):
            with open(file_name, 'rb',) as f:
                articles = f.readlines()
            data[cur_date] = " ".join(articles)

        cur_date -= timedelta(days=1)

    return data


if __name__ == '__main__':
    print "Running sentiment analysis..."
    start_date = datetime(year=2016, month=10, day=31).date()
    end_date = datetime(year=2016, month=10, day=31).date()
    data_dir = '/Volumes/Transcend/work/Harvard/CSCEI109a/project/data/'

    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()

    data = load_data(data_dir, start_date, end_date)
    for date, text in data.iteritems():
        word_tokens = word_tokenize(text)
        filtered_tokens = [w for w in word_tokens if not w in stop_words]
        stemmed_tokens = [w.lower() for w in word_tokens if not w in stop_words]
        print pos_tag(stemmed_tokens)
        # print word_tokens
        # print filtered_tokens
        # print stemmed_tokens