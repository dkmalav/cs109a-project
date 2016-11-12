import os
import requests
import time
import json
from datetime import datetime, timedelta


class NYTArticlesApi(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'

    def get_articles(self, start_date, end_date, page):
        start_date_str = start_date.strftime('%Y%m%d')
        end_date_str = end_date.strftime('%Y%m%d')

        params = {
            'api-key': self.api_key,
            'fq': "section_name:Business",
            'begin_date': start_date_str,
            'end_date': end_date_str,
            'fl': "lead_paragraph",
            'sort': "newest",
            'page': page
        }
        r = requests.get(self.url, params=params)

        if r.status_code == 200:
            response = json.loads(r.text)
            docs = response['response']['docs']
            return [item['lead_paragraph'] for item in docs]

        print "Error: api response: ", r.status_code, "Message :", r.text
        return None

    def fetch_articles(self, start_date, end_date, data_dir):
        cur_date = start_date
        while cur_date >= end_date:
            print 'Processing ', cur_date, '...'
            articles = []
            # get 2 pages for each day, i.e. 20 articles
            for page in range(2):
                articles_page = self.get_articles(cur_date, cur_date, page)
                if articles_page:
                    articles += articles_page
                else:
                    print "No data for page {0}.".format(page)
                    time.sleep(1)
                    break
                time.sleep(1)

            if len(articles) > 0:
                file_name = data_dir + cur_date.strftime('%Y%m%d') + '.txt'
                with open(file_name, 'wb',) as f:
                    for text in articles:
                        if text:
                            f.write(text.encode('utf-8').strip() + '\n')

            else:
                print "Error fetching articles for {0}.".format(cur_date)
                file_name = data_dir + "last_date.txt"
                with open(file_name, 'wb',) as f:
                    f.write(cur_date.strftime('%Y%m%d'))
                return

            cur_date -= timedelta(days=1)


if __name__ == '__main__':
    # set parameters for search

    # Dinesh
    api_key = '20fac7ba36c4447296126ff877e77b38'
    # api_key = 'ba51676673ec44259d27c5a5114b75cd'
    start_date = datetime(year=1995, month=12, day=31).date()
    end_date = datetime(year=1986, month=1, day=1).date()
    # start_date = datetime(year=2013, month=05, day=11).date()
    # end_date = datetime(year=2011, month=1, day=1).date()
    data_dir = '/Volumes/Transcend/work/Harvard/CSCEI109a/project/data/'

    # # Maja
    # api_key = '??????'
    # start_date = datetime(year=2010, month=12, day=31).date()
    # end_date = datetime(year=2006, month=1, day=1).date()
    # data_dir = '/Volumes/Transcend/work/Harvard/CSCEI109a/project/data2/'
    #
    # # Naveen
    # api_key = '?????'
    # start_date = datetime(year=2005, month=12, day=31).date()
    # end_date = datetime(year=2001, month=1, day=1).date()
    # data_dir = '/Volumes/Transcend/work/Harvard/CSCEI109a/project/data2/'
    #
    # # Naveen
    # api_key = '????'
    # start_date = datetime(year=2000, month=12, day=31).date()
    # end_date = datetime(year=1996, month=1, day=1).date()
    # data_dir = '/Volumes/Transcend/work/Harvard/CSCEI109a/project/data2/'


    file_name = data_dir + "last_date.txt"
    if os.path.exists(file_name):
        with open(file_name, 'rb') as f:
            last_date_str = f.readline()
            start_date = datetime.strptime(last_date_str, '%Y%m%d').date()

    # start_date = datetime(year=1992, month=7, day=31).date()

    # create NYT articles API wrapper and fetch data
    api = NYTArticlesApi(api_key)
    api.fetch_articles(start_date, end_date, data_dir)


# Dinesh - 2011-01-01-current
# Maja - 2001-01-01 - 2010-12-31
# Naveen - 1991-01-01 - 2000-12-31
# Uday - 1981-01-01 - 1900-12-31
