# ObserverPattern-WebGame
A project to practice Observer Pattern, Flask, HTML, JavaScript, Postgres, MongoDB, Redis and ideally Docker.
What I'm trying to build here is a small version of a browser game similar to Grepolis, Travian, etc.

# 22.04.2024:
**What am I trying to achieve(Intent):**
- Create template for in-game event/news system.
- Create subscription system to allow users to subscribe to in-game events/news system.
- Create a function to unsubscribe from in-game events/news system.

# 21.04.2024:
**What am I trying to achieve(Intent):**
- Create a system that will allow user to build units or upgrade buildings without the user feeling or seeing that the page was reloaded in the background.
- Update user's resources data in MongoDB collection when building units or upgrading buildings, according to cost.
- Add notification system for when the unit is created.
- Code will need some clean up/refactoring once done with the other tasks.
 
**Currently:**
- Learning JavaScript and HTML
- Trying out: Threading, Multiprocessing and Asyncio to get the task running in the background without preventing the user from using the game.

**Added:**
- Process for creating clubs. Using threading; For now functions are inside "player_profile.py". This will need to be changed.
- Resources are updated according to how many clubs are made. This will need to have some safety code so that in case when MongoDB is down, etc. the code should not charge user for clubs.
- Added simple notification system using notifypy - This could have been changed so that the user receives a text message or an email, if the need be.
- Refactoring of unit production.
