# Project 1

Web Programming with Python and JavaScript

## Decisions I made, not specified in spec
- API average_score will be "N/A" if review_count == 0

## Todo-list:

### Backend
- split search into multiple pages (Using SQL LIMIT and OFFSET, perhaps), since I don't want ajax at this point (or maybe that's a good option, who knows!)

### Frontend
- use bootstrap for nicer form validation messages
- use js to ensure more careful deletion (like typing in username to confirm)

### Done:
- login
- logout
- user registration
- change password
- redirect back to prev page on:
    - login
    - register
    - logout
- delete account
    - should reviews be deleted? No
- search
    - use bootstrap cards for each result book
    - do case insensitive search
    - enable search category and remember selection; now using url;
- select a random book if user clicks "BAD" button
    - https://www.postgresql.org/docs/current/sql-select.html#SQL-FROM 
    - https://stackoverflow.com/questions/8674718/best-way-to-select-random-rows-postgresql 
    - TABLESAMPLE SYSTEM
- book detail page
- book reviews
    - ability to add/modify reviews
- calculate ratings
- make api
- add footer


### Be careful about (Which I spent hours debugging):
- Commit! Commit! Commit! Commit everytime modifying database (INSERT, UPDATE, DELETE)
- Update Bootstrap! (So dropdown-menu-right and custom_forms work!)
- DO NOT use outdated approach to make footer stick to bottom. [Use this](https://getbootstrap.com/docs/4.3/examples/sticky-footer/).

### Problems that still exist:
- Needs Improvements:
    - Search category selection 
        - Keep search selection area expanded if the user has done so
        - Use cookies to remember selection

- Styling:
    - How to get the search icon to be inside of the search box?
    - Underline link on hover doesn't work for header links