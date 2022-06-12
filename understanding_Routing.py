from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def greetings():
    return "Dojo!"

@app.route('/say/<varName>')
def printNames (varName):
    print("In the print name function")
    return "Hi " + varName

@app.route('/repeat/<myNum>/<myvar>')
def repeat (myNum,myvar):
    print("In the repeat function")
    myInt = int(myNum)
    arr = []
    for x in range(0,myInt): 
        arr.append(myvar)
    return f"Hello: {arr}" 
    

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

