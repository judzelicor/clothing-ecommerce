# Django E-commerce
This is a clothing e-commerce web application for a hypothetical brand, Oubjects. Upon entering the website, the visitor is prompted by a button to 
view and shop the lastest clothing in their collection. The front page also display their best sellers and one featured product near the bottom of the
page.

## Screenshot Previews
<img src="https://gate-of-babylon.s3.ca-central-1.amazonaws.com/oubjects-ecommerce/Screen+Shot+2022-09-28+at+11.29.53+AM.png" />

## Current Features
- It has a search function where customers are able to search for a particular clothing site-wide.
- It has a shopping cart system where customers are able to add or remove clothing items from their cart and specify the number of clothing 
they've intended to purchase which can be seen on the upper-right corner of the website on desktops and through a menu toggle when the website if viewed in a mobile device.
- It has Strip integrated to handle payments. You can go through the payment process and use a testing Stripe credit card `4242 4242 4242 4242`.
- A user authentication system where customers are able to sign up for an account and log in.
- A blogging system for admin users to post and create artciles related to clothing and their brand.
- It uses AWS S3 to store every static assets.

## Run This Project
You can run this project on your local computer for further testing and modifications.
1. Make sure you have Python 3.6+ installed on your computer. You can set it up by following instructions from their [website](https://www.python.org). I
personally prefer using [Miniconda](https://docs.conda.io/en/latest/miniconda.html) and set up an isolated environment but takes some tinkering around but
the payoff is worth the trouble.
2. Create an empty directory in your computer and open your terminal. Relocate to your newly created directory by typing in the command
```
cd <NAME_OF_YOUR_DIRECTORY>
```
3. Clone this repository by typing in the command
```
git clone https://github.com/judzelicor/clothing-ecommerce ./
```
4. Download Django by typing in the command
```
python -m pip install Django
```
5. Run the server by entering the following command in the terminal
```
python manage.py runserver
```
6. Open your desired browser and visit http://localhost:8000 or the port that your project is open which can be read right after the command that you just
ran.

### Acknowledgements
- Designed and implemented by Judz Philip Elicor.
- Images were taken from actual ecommerce websites.
- Written content were also taken from actual ecommerce websites because I lack the "creative content writer" neural faculties to do so on my own :P.
