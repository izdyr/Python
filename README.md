<p align=center>
  <img height="150" weight="150" src="https://i.ibb.co/ZfdyMC7/output-onlinegiftools.gif">
</p>


# Hello    <img height="35" weight="70" src="https://i.ibb.co/NmcCZrz/Picture2.png">

In this section, I have put my small projects.
Many of these projects can be found on the internet, but I have written them in my own way

I hope they were helpful.

## 🧮 Python Calculator Project

This Python calculator project is designed to effortlessly handle your basic arithmetic operations. 🧮 By utilizing symbols such as '+', '-', 'x' (or '*'), and '/' (or '÷'), users can input mathematical expressions and receive quick and accurate results. ➗ The program parses the input, extracts the numbers and the operation, and performs the calculation. 🔄 With error handling in place, it ensures a smooth user experience. 🛠️ Explore the world of Python programming with this handy calculator! 🌐
> **Input:**
```console
foo@bar:~$ python calculator.py What do you want to solve? 3+3

```
>

> **Output:**
```console
foo@bar:~$ python calculator.py 3+3=6

```
>
>

<a href="https://github.com/izadyarjalalipour/Python/tree/main/Calculator">
  <img src="https://i.ibb.co/mcWLd7z/button-source-code.png" alt="GitHub" height="55" width="200">
</a>


## 📧 Python Email Sender

This Python script simplifies email sending through the smtplib library and the SMTP protocol. 📧 It begins by configuring the SMTP server, setting up email content, and creating both plain text and HTML message bodies. ⚙️ The process involves connecting to the server, initiating a secure connection, logging in, and ultimately sending the email from the sender to the recipient. 🔒 Upon successful transmission, the script gracefully closes the SMTP connection and prints a confirmation message. 🎉 Customize sender and recipient addresses, adjust content, and streamline your communication workflow effortlessly with this Python email sender script. 🚀
> **Input:**
```console
foo@bar:~$ python email_sender.py Type your password and press enter: ********

```
>

> **Output:**
```console
foo@bar:~$  Email sent successfully!

```
>
>

<a href="https://github.com/izadyarjalalipour/Python/tree/main/Email%20sender">
  <img src="https://i.ibb.co/mcWLd7z/button-source-code.png" alt="GitHub" height="55" width="200">
</a>

## 🛡️ Password Manager

This Python script acts as a secure and user-friendly password manager. 🐍🔐 It utilizes the Fernet encryption library, symbolized by a robust lock, to safeguard stored passwords. 🔒 Users can effortlessly manage their credentials by adding new passwords or retrieving existing ones. ➕🔍 With key generation, password encryption, and an intuitive menu interface, it empowers users to navigate the password management landscape securely. 🛡️ Take command of your digital security and embark on a journey into Python programming with this reliable password manager! 🗝️
> **Library:**
```console
foo@bar:~$ pip install cryptography

```
>
> **Input:**
```console
foo@bar:~$ python password_manager.py
Password Manager
1. Retrieve password
2. Add new password
3. Exit

```
>

> **Output (Choice):**
```python
if choice == "1":
            service = input("Enter the service name: ")
            retrieve_password(service)
        elif choice == "2":
            new_password()
        elif choice == "3":
            break
```
>
>

<a href="https://github.com/izadyarjalalipour/Python/tree/main/Password%20Manager"> 
  <img src="https://i.ibb.co/mcWLd7z/button-source-code.png" alt="GitHub" height="55" width="200">
</a>

## 🔑 Password Generator

This Python script functions as a password generator with a user-friendly interface. 🐍🔐 Users can choose between running the password generator or exiting the program. 🔄🚪 The generator employs a combination of letters, digits, and punctuation for creating secure passwords. ➡️🔢🔠 It provides an intuitive menu, allowing users to interact easily. 🛠️👨‍💻 Take control of your password creation with this Python tool!

> **Input:**
```console
foo@bar:~$ python password_generator

```
>

> **Output (Choice):**
```python
     1. run the password generator
     2. Exit
```
>
>

<a href="https://github.com/izadyarjalalipour/Python/blob/main/Password%20generator/">
  <img src="https://i.ibb.co/mcWLd7z/button-source-code.png" alt="GitHub" height="55" width="200">
</a>

## 🤳🏻 QRCode Generator

This Python code generates a QR code using the `qrcode` library. 🐍 You provide a website URL as input, and the code creates a QR code with specified effects such as box size and border. The QR code is then saved as an image, in this case as "qrcode.png".📷

> **Input:**
```console
foo@bar:~$ python qrcode_generator.py

```
>

> **Output:**
```console
foo@bar:~$ Enter URL: [user_input_here]
```
>
>

<a href="https://github.com/izadyarjalalipour/Python/tree/main/QR%20code%20generator/">
  <img src="https://i.ibb.co/mcWLd7z/button-source-code.png" alt="GitHub" height="55" width="200">
</a>


## 📖 Story Generator

This Python script creates a randomly generated story scenario. 📚🎲 It features characters, settings, and plots, and combines them to form a unique narrative snippet. 🐍 Here's a breakdown:

Characters:

A list of fictional character names is defined, and one character is randomly chosen from this list.
Settings:

Various settings are provided, such as a forest, beach, city, etc. One setting is randomly selected.
Plots:

Different plot ideas are given, like searching for a lost artifact, solving a mystery, etc. A plot is randomly chosen.
Story Generation:

Using the selected character, setting, and plot, a sentence is constructed to describe a scenario. The characters "found themselves" in a specific setting, and engaged in a particular plot. The emotional state of the character is also randomly determined, with options like "excited," "scared," etc.

> **Input:**
```console
foo@bar:~$ python story_generator.py

```
>

> **Output:**
```console
foo@bar:~$ Charlie found themselves in a forest, escaping from danger. They were excited!
```
>
>

<a href="https://github.com/izadyarjalalipour/Python/tree/main/Story%20generator/">
  <img src="https://i.ibb.co/mcWLd7z/button-source-code.png" alt="GitHub" height="55" width="200">
</a>

## ☁️ Weather App

This Python script utilizes the OpenWeather API to provide current weather information for a specified city and country. 🌍🌦️ The code prompts the user to input the city name and country code, then requests the OpenWeather API to fetch real-time weather data. The temperature in degrees Celsius and a brief description of the weather (e.g., cloudy, sunny) are then extracted from the API response and presented to the user. ☀️🌧️ If the API request is unsuccessful, the script informs the user that weather information cannot be retrieved.

> **Input:**
```console
foo@bar:~$ python weather.py
Enter city name: Paris
Enter country code: FR
```
>

> **Output:**
```console
foo@bar:~$ The temperature is 20 degrees Celsius, and the weather is partly cloudy.
```
>
>

<a href="https://github.com/izadyarjalalipour/Python/tree/main/Weather%20App">
  <img src="https://i.ibb.co/mcWLd7z/button-source-code.png" alt="GitHub" height="55" width="200">
</a>

## ▶️ Youtube Video Downloader

This Python script utilizes the `pytube` library to download YouTube videos. 🎥🔽 The user is prompted to input the YouTube video URL. The script then creates an instance of the `YouTube` class, extracts the first available video stream, and proceeds to download the video. The progress is displayed to the user, and upon completion, a success message is printed. 🚀

> **Input:**
```console
foo@bar:~$ python pytube.py
Please type the YouTube video URL: https://www.youtube.com/watch?v=example_video_id
```
>

> **Output:**
```console
foo@bar:~$
Downloading video...
Video downloaded successfully!
```
>
>

<a href="https://github.com/izadyarjalalipour/Python/tree/main/YouTube%20video%20downloader">
  <img src="https://i.ibb.co/mcWLd7z/button-source-code.png" alt="GitHub" height="55" width="200">
</a>

# 👨‍💻 Creator
<a href="https://github.com/izadyarjalalipour">
  <img src="https://i.ibb.co/8PXrptR/izadyar.png" alt="GitHub" height="55" width="55">Izadyar Jalalipour
</a>

# 📜 Lisence

*Copyright (c) 2023 Izadyar Jalalipour*
