Trendmatch is an innovative Danish [startup company](https://trendmatch.dk/) in the fashion business. In one app it connects buyers and sellers - both large and small. Their shopping experience is as easy as Swipe -> Match -> Purchase.

Product recommendation is one of the most important features of the app, with an ultimate goal of increasing the number of matches between users and products. This in turn would result in higher profits for the sellers and better clothes for the buyers.

![trendmatch_app](../static/trendmatch_app.png)

## Design & challenges

The recommender's design started around the same time as the app's backend. This made sure that the algorithm will get the needed data, and the rest of the data infrastructure will be able to provide it. This was made possible only by great collaboration between the data, backend and leadership teams of Trendmatch.

The algorithm should be able to function in real-time i.e., in sub-second time intervals, between two user swipes. To be able to get accurate recommendations, we must combine product data with information on both short and long-term user actions. Some of the challenges here arise with incomplete user data, such as unknown user gender or age. Other challenges are connected to the way data is stored and computed, so sub-second predictions are made possible. 

## Development

As of March 2019, the Trendmatch app has been functional for a few months now, collecting a substantial amount of data. Thus, the development process of the recommender is under way! 