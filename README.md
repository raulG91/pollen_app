# Pollen App
![GitHub License](https://img.shields.io/github/license/raulG91/pollen_app)
![GitHub forks](https://img.shields.io/github/forks/raulG91/pollen_app)
![GitHub Repo stars](https://img.shields.io/github/stars/raulG91/pollen_app)


## Description

The aim of this project was to create an app to continue my learning about [Reflex](https://reflex.dev/). The idea was to create a simple application to check pollen values in my region: Andalucia (South of Spain). This app was created because the official website that I normally use to check pollen values is a very old website and it is not possible to use in mobile because it is not reposible. So I took this oppotunity to play around with Reflex to create something useful. 

Since I don't have access to the offical data, this project uses [Google API](https://developers.google.com/maps/documentation/pollen/overview). That API will return pollen result for the city selected on the screen and will show the results in a table. It is a simple design but useful.

The application contains a file called `andalucia.json`, that file contains for each province all the towns and for each town two attributes are stored: latitude and longitude. Those 2 attributes will be used to retrieve the information from Google Pollen API.

## Installation

To use the application, you will need to have an access token from Google to authenticate again the API.

-   Instructions about how to get the API key follow the guide provided by [Google](https://developers.google.com/maps/documentation/pollen/cloud-setup).

Once you have the API Token you need to set it in your environment. Create an environment variable called `token="Your access token"`. 

After following previous steps you will be able to launch the application just executing `reflex run`.