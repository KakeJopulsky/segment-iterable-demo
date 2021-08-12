## WIP of a working demo of a Segment<>Iterable integration.

### To Run
1. Create a virtual environment and install all dependencies
1. `flask run`
1. Navigate to `127.0.0.1:5000` and login
    1. If you are a new user, a profile will be created in Segment and Iterable for your user

Users logged in are identified with a Segment `identify` call, and subsequently identified in Iterable.
