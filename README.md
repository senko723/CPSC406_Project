# Probability predictor AI
# By: Peter Senko

## Instructions
### To run predictors
    python3 predictor.py
### To run blockchain and API
    python3 blockchain.py
    python3 API.py

## Introduction
Betting is something that many people do every single day. However, there are some drawbacks that are encountered when people are betting such as security and other issues regarding currency. Blockchain are something that can both offer more security and allow for users to use multiple different types, along with funding being able to more readily available. This projects goal was then to create an environment where people could results of the current data that they have on bets and then be able to communicate those results to another person. Allowing for a more peer to peer take on betting rather than just inputting bets into a online site and then coming back when the bet has concluded.

## Literature Review
When doing some background research on how I was going to exactly implement blockchain into my betting AI. I though I should first make the basis on the data that my betting predictors would be able to produce. For this I used some of my current knowledge from previous classes like CPSC 390 Artificial Intelligence and some background research in other algorithms that take data an use it provide an answer of accuracy. The algorithm I had to do some research in was neural networks(https://realpython.com/python-ai-neural-network/) from this I was able to get a better understanding on how it truly works and how I could the data acquired from this to receive results that were actually useful. The other algorithm that I did some research on was SVM or Support Vector Machines(https://www.datacamp.com/tutorial/svm-classification-scikit-learn-python).

## Documentation
The project consists of of mostly python code. The code is divided between the predictors, blockchain, and the parser/scraper which is all in the code folder. The data structures and algorithms that are used are 4 predictors(baseline, naive bayes, neural nets, and svm) that each find a accuracy based off the data from the parser and scraper.The data that is being scraped through is from Basketball Reference](https://basketball-reference.com). The data is first stored in a data-frame then is converted to json files. The work was solely done by Peter Senko.

## What works and what does not
The project runs all the predictors correctly. The aspect between the blockchain and being able to relay the calculations from the predictor to people that also currently on the blockchain. However, users can still send transactions but have to update the code with the transactions that they wish to place. The next step from here would be to enhance the API to be able to truly exchange information from peer to peer and to be able to send transaction without having to alter the code in anyway each time.
