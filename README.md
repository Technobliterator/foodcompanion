# foodcompanion
Django-based web application (assisted by Bootstrap and Vue.js for frontend) for querying and filtering food items obtained from scraped database.

Project is hosted at https://glacial-oasis-82218.herokuapp.com/.

How to test the app:

1. Under the “Product” search, type “olives” and press enter. The first result should be: “blood mary olives”
2. Click on “blood mary olives” and it will open the store webpage for that product
3. Click on the “back arrow” and it will go back to 
4. Under the “Ingredients” search, type “olives” and press enter. The first result should be: “Sugar Fr Oats Orange & Choc Chip Cookies, 8 oz
5. Under the “Maximum calories” search, type “120” and press enter. The first result should be: “01 Espresso Blend Coffee, 12 oz”
6. Press “Clear filters”. It should be reset.
7. Under the “Product” search type “red pepper” and press enter. The first result should be: “12inch uncured pepperoni pizza”
8. Press “Clear filters”. It should be reset.
9. Enter “Search”, search “chicken”. The first result should be: “Aidells All Natural Teriyaki & Pineapple Chicken Meatballs” from “Kroger”
10. Select “United Kingdom” from the list of countries. The result should now be “Tesco 4 Southern Fried Chicken”.
11. Press “Clear filters” again to reset.
12. Select “Canada” from the list of countries. The first result should be: “Alpen No Added Sugar Muesli Cereal - Case of 12 - 14 oz.”
13. Press “Clear filters” again to reset.
14. Select “Whole Foods” from the list of stores. The first result should be: “01 Espresso Blend Coffee, 12 oz”
15. Press “Clear filters” again.
16. Press “glutenfree”. The first result should be: “0% Blueberry Skyr Yogurt”
17. Press “Clear filters” again.
18. Press “vegan”. The first result should be: “01 Espresso Blend Coffee, 12 oz”
19. Press “vegetarian”. The results should now include products with the “vegetarian” certificate, “vegan” unselected. The first of these should be “01 Espresso Blend Coffee, 12 oz”
20. Press “halal”. As above; “vegetarian” should be unselected, and products should include ones with the “halal” certificate. The first of these should be “0% Blueberry Skyr Yogurt, 5.3 oz”.
21. Press “kosher”. As above; “vegetarian” should be unselected, and products should include ones with the “halal” certificate. The first of these should be “0% Blueberry Skyr Yogurt, 5.3 oz”.
22. Press the “login” button at the top right, and then follow the link to “register”.
23. Register an account with an acceptable username and password. It should return to the front page.
24. Press “login” with the new username and password. When logging in, it should return to the front page with “login” at the top-right replaced by the username and “logout”.
