# robo-advisor

## Robo Advisor Project 
If you are interested in researching and evaluating stocks to retrieve information such as: latest closing price, most recent high, and low price. In addition, this Python application will reccommened to you whether now is a good time buy or sell a selected stock. 

## Installation Requirements
Anaconda 3.7 + 
Python 3.7 + 
Pip 




## Installation

Use the GitHub.com online interface to create a new remote project repository called something like "robo-advisor". When prompted by the GitHub.com online interface, let's get in the habit of adding a "README.md" file and a Python-flavored ".gitignore" file (and also optionally a "LICENSE") during the repo creation process. After this process is complete, you should be able to view the repo on GitHub.com at an address like https://github.com/YOUR_USERNAME/robo-advisor.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

cd ~/Desktop/robo-advisor

If you haven't done so yet, use anaconda to create and activate a new virtual environment. A suggestion would be to call it "stocks-env":

    conda create -n stocks-env python=3.8
    conda activate stocks-env

From inside the virtual environment, install package dependicies:

    pip install -r requirements.txt


Before using or developing this application, take amoment to obtain an AlphaVantage API Key ()

After obtaining an API Key, create a new file in this repository called ".env", and update the contents of the ".env" file to specify your real API Key: 

    ALPHAVANTAGE_API_KEY="abc123"


## Usage


From inside the virtual environment, run the code using the command below:

    python app/robo_advisor.py 

To start, enter a valid stock ticker when requested to do so. If successful, you will be presented with an abundance of data (latest closing price, most recent high, and low price) to evaluate the stock. In addition, this Python application will reccommened to you whether now is a good time buy or sell a selected stock. This decision will be based on whether or not the stock's latest closing price is more than or less than 15% above its recent low.  If unsuccesful with typing in a valid stock ticker, you will be asked to start the process over. Enjoy! 




