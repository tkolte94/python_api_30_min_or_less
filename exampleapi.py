# Everything that starts with a # is considered a comment and is not an actual part of the code that get executed

# This is an import statement. It allows you to use the module you've just loaded in your application
from fastapi import FastAPI

# This defines our application.  "app" is what we'll use to set up everything else
app = FastAPI()

# Let's start setting up the routes!
@app.get("/")
def index():
	return {'possible routes': {
			"/test": "use with GET, returns a test string",
			"/sayhi/{name}": "use with GET, returns hello with your argument",
			"/": "This message!"
	}}

@app.get("/test")
def test():
	return {"message": "This is a test"}

@app.get("/sayhi/{name}")
def sayhi(name):
	hi_message = "Hi " + name + "!"
	return {"message": hi_message}
