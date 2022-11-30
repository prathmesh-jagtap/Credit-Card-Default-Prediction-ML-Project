# CREDICT CARD DEFAULT PREDICTION

> Predicts weather the credit card holder is DEFAULT or not.

![Issues](https://img.shields.io/github/issues/prathmesh-jagtap/Credit-Card-Default-Prediction-ML-Project)
![Pull Requests](https://img.shields.io/github/issues-pr/prathmesh-jagtap/Credit-Card-Default-Prediction-ML-Project)
![Forks](https://img.shields.io/github/forks/prathmesh-jagtap/Credit-Card-Default-Prediction-ML-Project)
![Stars](https://img.shields.io/github/stars/prathmesh-jagtap/Credit-Card-Default-Prediction-ML-Project)
[![License](https://img.shields.io/github/license/prathmesh-jagtap/Credit-Card-Default-Prediction-ML-Project)](https://github.com/prathmesh-jagtap/Credit-Card-Default-Prediction-ML-Project/blob/master/LICENSE)

# Aim of the Project

#### > To predict whether a credit card customer is a defaulter, using numerical and Categorical Data.

#### > Apply ML and DL Models to predict the severity and probability of the Credit Card Defaulter.

#### > Create a Wonderful UI for this project using Front End Languages and Frameworks (Like Bootstrap, HTML/CSS, JavaScript).

#### > Create the Backend using Flask Framework.

#### > Deploy on Cloud and make this wonderful project available to public

## Table of Content

- [Project Description](#about-project)
- [Languages/Framework Used](#tech-stack)
- [Project Setup](#project-setup)
- [How to use](#installation)
- [CI/CD](#deployment)
- [Demo](#demo)
- [Notebook](#notebok)

## About Project:

Financial threats are displaying a trend about the credit risk of commercial banks as the incredible improvement in the financial industry has arisen. In this way, one of the
biggest threats faces by commercial banks is the risk prediction of credit clients. The goal is to predict the probability of credit default based on credit card owner's characteristics and payment history.

For building the project I have used “Default of Credit Card Clients” dataset
released under the public liscense of Creative Commons and available on the Kaggle website.
This dataset contains information on default payments, demographic factors, credit data, history of payment,
and bill statements of credit card clients from April 2005 to September 2005. This dataset contains
30000 observations of 25 variables from a bank (and also a cash and credit card issuer); where each
observation corresponds to a particular credit card client. Among the total 30000 observations, 6636 observations (22.1%)
are cardholders with default payment.

The data is prepossessed, validate and scaled. I have trained with Random forest Classifier, and Gaussain Naive Bayes algorithms.
To provide an easy-to-use interface to users. I have developed a website that will take the data and display the output with accuracy and time taken to predict.
For the evalution or accuracy of our model I have used **F1 Score**. F1 Score is the weighted average of Precision and Recall.
Therefore, this score takes both false positives and false negatives into account. Intuitively it is not as easy to understand as accuracy,
but F1 is usually more useful than accuracy, especially if you have an uneven class distribution.

## Tech Stack

**Client:** HTML, CSS, JavaScript, Boootstrap.

**Server:** Python, Flask, Pandas, Numpy, Sklearn.

**Deployment:** Heroku.

## Project Setup

1. Environment Variables

> To run this project, you will need to add the following environment variables:

```
conda create -p venv python -y
```

```
conda activate venv
```

```
pip install -r requirements.txt
```

2. run the app.py as python app.py
3. Web Application will be hosted at 127.0.0.1:5000
4. Enter the URL in the browser Application will be hosted.
5. Enter the details of the credit card owner for prediction.

## Installation

> Steps to follow :scroll:

### 0. Star The Repo :star2:

Star the repo by pressing the topmost-right button to start your wonderful journey.

### 1. Fork it :fork_and_knife:

### 2. Clone it :busts_in_silhouette:

`NOTE: commands are to be executed on Linux, Mac, and Windows`

Cloning a repository.

> Run the cammond in Git or CMD

```bash
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git
```

> This makes a local copy of the repository in your machine.

Once you have cloned the repository in Github, move to that folder first using change directory command on Linux, Mac, and Windows

```bash
# This will change directory to a folder
$ cd YOUR-REPOSITORY-NAME
```

Move to this folder for all other commands.

### 3. Set it up :arrow_up:

Run the following commands to see that _your local copy_ has a reference to _your forked remote repository_ in Github :octocat:

```sh
$ git remote -v
origin  https://github.com/Your_Username/YOUR-REPOSITORY-NAME.git (fetch)
origin  https://github.com/Your_Username/YOUR-REPOSITORY-NAME.git (push)
```

Now, let's add a reference to the original [Credit-Card-Default-Prediction-ML-Project](https://github.com/prathmesh-jagtap/Credit-Card-Default-Prediction-ML-Project) repository using

```sh
$ git remote add upstream https://github.com/prathmesh-jagtap/Credit-Card-Default-Prediction-ML-Project.git
```

> This adds a new remote named **_upstream_**.

See the changes using

```sh
$ git remote -v
origin    https://github.com/Your_Username/Credit-Card-Default-Prediction-ML-Project.git (fetch)
origin    https://github.com/Your_Username/Credit-Card-Default-Prediction-ML-Project.git (push)
upstream  https://github.com/Remote_Username/Credit-Card-Default-Prediction-ML-Project.git (fetch)
upstream  https://github.com/Remote_Username/Credit-Card-Default-Prediction-ML-Project.git (push)
```

`In your case, you will see`

```sh
$ git remote -V
origin    https://github.com/Your_Username/Credit-Card-Default-Prediction-ML-Project.git (fetch)
origin    https://github.com/Your_Username/Credit-Card-Default-Prediction-ML-Project.git (push)
upstream  https://github.com/manan-bedi2908/Credit-Card-Default-Prediction-ML-Project.git (fetch)
upstream  https://github.com/manan-bedi2908/Credit-Card-Default-Prediction-ML-Project.git (push)
```

### 4. Sync it :recycle:

Always keep your local copy of the repository updated with the original repository.
Before making any changes and/or in an appropriate interval, run the following commands _carefully_ to update your local repository.

```sh
# Fetch all remote repositories and delete any deleted remote branches
$ git fetch --all --prune

# Switch to `New_Pipeline` branch
$ git checkout New_pipeline

# Reset local `main` branch to match the `upstream` repository's `main` branch
$ git reset --hard upstream/main

# Push changes to your forked `Breast-Cancer-Predictor` repo
$ git push -u origin New_pipeline
```

### 5. Ready Steady Go... :turtle: :rabbit2:

Once you have completed these steps, you are ready to start contributing to the project and creating [pull requests](https://github.com/prathmesh-jagtap/Credit-Card-Default-Prediction-ML-Project/pulls).

### 6. Checkout to a new branch :bangbang:

Whenever you are going to contribute. Please create a separate branch using command and keep your `main` branch clean (i.e. synced with remote branch).

```sh
# It will create a new branch with name Branch_Name and switch to branch Folder_Name
$ git checkout -b New_pipeline
```

Create a separate branch for contribution and try to use the same name of the branch as of folder.

To switch to the desired branch

```sh
# To switch from one folder to other
$ git checkout New_pipeline
```

To add the changes to the branch. Use

```sh
# To add all files to branch Folder_Name
$ git add .
```

Type in a message relevant for the code reviewer using

```sh
# This message get associated with all files you have changed
$ git commit -m '<message>'
```

Now, Push your awesome work to your remote repository using

```sh
# To push your work to your remote repository
$ git push -u origin New_pipeline
```

(Kindly push all the changes to the "New_pipeline", not main branch)
Finally, go to your repository in the browser and click on `compare and pull requests`.
Then add a title and description to your pull request that explains your precious effort.

---

## Deployment

To deploy this project or heroku we need 3 information

1. HEROKU_EMAIL = <jagtaprathmesh19@gmail.com>
2. HEROKU_API_KEY = < Locatied in settings of your heroku account >
3. HEROKU_APP_NAME = < Name of your heroku app >

Build Docker Image

```bash
docker build -t <image_name>:<tagname> .
```

> Note: Image name for docker must be lowercas

To list out docker images

```bash
docker images
```

Run docker image

```bash
docker run -p 5000:5000 -e PORT=5000 187e678ae51c
```

To stop docker conatiner

```bash
docker stop <container_id>
```

## Demo

---

<div align="center">
<h4>Application UI</h4>
</div>

![Application UI](https://github.com/prathmesh-jagtap/Credit-Card-Default-Prediction-ML-Project/blob/main/Documents/gif.gif)

[Try Now](https://creditcard-defaults-prediction.herokuapp.com/)

## Related

Here are some related projects

[Housing Price Prediction](https://github.com/prathmesh-jagtap/Housing-Price-Prediction-ML-Project)

## Authors

- [About me](https://github.com/prathmesh-jagtap)

## Feedback

If you have any feedback, please reach out to us at [Feedback](https://github.com/prathmesh-jagtap/Credit-Card-Default-Prediction-ML-Project/issues/new/choose)

## Notebok

<button><a target="_blank" href="https://colab.research.google.com/drive/1Cb9WRRHQiv2cRq41syHkyP3iInFNgSMu?usp=sharing"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />Run in Google Colab</a></button>

## Thnaks for Reading :pray:
