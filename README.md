# search-engine

* Python3 is a pre-requisite
============================

* Run "pip3 install -r requirements.txt" when inside the django project
    to install the required dependencies
* Run "python3 manage.py makemigrations"
* Run "python3 manage.py migrate"
( This will apply the migrations )

* Run "python3 manage.py runserver 8000" to up the local server
* Hit this api (GET): http://127.0.0.1:8000/preprocess to preprocess and
  create all the data required for querying (takes about 1 min to pre-populate)

* In SAMPLE APIs (listed below):
    1) API will preprocess and pre-populate all the data required for querying
    2) API will take a list of queries and k, and return a list of k matching results 
       {id:"string", author:"string", summary:"string", query:"string"} for each query

Model Definitions (search_app/models.py):
-----------------

BOOK:
    [Fields]        = count_words, book_id (PK)
    [Sample Values]: 23 , 1

WORD:
    [Fields]        = w (DB index)
    [Sample Values]: "problems"
    
FREQ:
    [Fields]        = count, book, word
    [Sample Values]:  3, book(obj), word(obj)
    

FREQ <- Many-to-Many Relation with -> BOOK

FREQ <- Many-to-Many Relation with -> WORD


SAMPLE APIs :
-------------

1) REQUEST (GET):  http://127.0.0.1:8000/preprocess
   RESPONSE: { "result": "success" }

2) REQUEST (POST):  http://127.0.0.1:8000/process_queries
   PAYLOAD : {  "queries" : ["is your problems", "achieve take book"], 
	            "k": 3 }
	            
   RESPONSE: {
    "result": [
        [
            {
                "id": 0,
                "summary": "The Book in Three Sentences: Practicing meditation and mindfulness will make you at least 10 percent happier. Being mindful doesn’t change the problems in your life, but mindfulness does help you respond to your problems rather than react to them. Mindfulness helps you realize that striving for success is fine as long as you accept that the outcome is outside your control.",
                "author": {
                    "author": "Dan Harris"
                },
                "query": "is your problems"
            },
            {
                "id": 48,
                "summary": "The Book in Three Sentences: Finding something important and meaningful in your life is the most productive use of your time and energy. This is true because every life has problems associated with it and finding meaning in your life will help you sustain the effort needed to overcome the particular problems you face. Thus, we can say that the key to living a good life is not giving a fuck about more things, but rather, giving a fuck only about the things that align with your personal values.",
                "author": {
                    "author": "Mark Manson"
                },
                "query": "is your problems"
            },
            {
                "id": 7,
                "summary": "The Book in Three Sentences: Everything in life is an invention. If you choose to look at your life in a new way, then suddenly your problems fade away. One of the best ways to do this is to focus on the possibilities surrounding you in any situation rather than slipping into the default mode of measuring and comparing your life to others.",
                "author": {
                    "author": "Rosamund Zander and Benjamin Zander"
                },
                "query": "is your problems"
            }
        ],
        [
            {
                "id": 1,
                "summary": "The Book in Three Sentences: The 10X Rule says that 1) you should set targets for yourself that are 10X greater than what you believe you can achieve and 2) you should take actions that are 10X greater than what you believe are necessary to achieve your goals. The biggest mistake most people make in life is not setting goals high enough. Taking massive action is the only way to fulfill your true potential.",
                "author": {
                    "author": "Grant Cardone"
                },
                "query": "achieve take book"
            },
            {
                "id": 39,
                "summary": "The Book in Three Sentences: Before you pay your expenses, take your profit first. Run your business based on what you can afford to do today, not what you hope to be able to afford someday. When profit comes first, it is the focus, and it is never forgotten.",
                "author": {
                    "author": "Mike Michalowicz"
                },
                "query": "achieve take book"
            },
            {
                "id": 20,
                "summary": "The Book in Three Sentences: Many of our behaviors are driven by our desire to achieve a particular level of status relative to those around us. People are continually raising and lowering their status in conversation through body language and words. Say yes to more and stop blocking the opportunities that come your way.",
                "author": {
                    "author": "Keith Johnstone"
                },
                "query": "achieve take book"
            }
        ]
    ]
}


REFERENCE:
----------
http://www.tfidf.com/

** Relevance of match is calculated based on summation of calculated tf-idf value for each book id


P.S. - Have written basic unit tests with mock (First ever implementation of mocking). Wanted to 
       keep total development time to maximum of 4-5 hours.
