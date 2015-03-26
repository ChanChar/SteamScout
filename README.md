# 002-pyp-demoday-g1
Charlie's angels  
[Initial Overview Sheet](https://docs.google.com/document/d/1qt_IZOc579Qe8HO5wrb--vzrk4acdOavfqp7vlH7crw/edit)  
[Basic Wireframes](https://docs.google.com/presentation/d/1vJZhuTA-SrLgKG1RMaPhud2BZqDFzHbbWi4EKOhzvHE/edit#slide=id.p)  


## Purpose
Steam sales are a daily occurance but there are way too many games to keep track of. Use SteamScout to alert you
when a game that you're interested in drops down to the price you set. 

### Required

+ Set up email notifications and integrate with some type of scheduling system. 
+ Paginate games library, currently causes significant lag. SQL alchemy has something built in for pagination
+ set up the gamesDB to automatically refresh every 24 hours. - Cron Job
+ Fix flashes - Working on it right now


### Optional

+ Improve Settings page. - Improved it to look better.
+ Add percentage threshold option for preferences
+ Change Preferences so that once an email goes out with that preference, 
either delete the preference or mark it so that it doesn't get sent out again in the next report. 
+ Color divs in preferences so that users can see how close their set price is to the current price. 
+ Implement Flask blueprints
+ validate each integer in the amount threshold form
+ make the individual games look pretty - Improved it, but it could be better..
+ see if theres a way to include game cover art, trailers, etc in the individual game page
+ Change generic variables to be more specific. Ex. form should should be login_form
+ Add to the settings page when no preferences are set. 
+ Add a default currency on games page
+ Add button/link to the settings page which link to game search ''Add New Scout''
+ Convert game games to links to games steam store page. (available in the API)


### Completed:
- configure a way for steamscout to email users. - Flask-Mail
- Update button in user's settings page.
- set up user preferences
- Set up email account validations
- format price data. Currently "$4.99" displays as "499" - changed format_prices to make it easier
- Ideally, figure a way to only put games into the gamesDB. 
    - if not 2, protect the site from apps that dont have a price_info section.
- build way to search through games library - Basic Functionality
- Changes amount format, list view on settings 
- Improve Navbar in base (log out column adding problems)
- Split components into separate files. App.py is too big for one file.