# data types for Drill
from pyscript import display, document


#Variable
footer = {'Enriquez | 10-Topaz'} #single quotation marks to be placed in the footer

# Footer for bottom
display(footer, target="bottom")

# Final form
def studentform(e): #creating functions in python
    document.getElementById("profile").innerHTML = "" #clearing the output field

    Address = document.getElementById("address").value.strip()
    Age = document.getElementById("age").value.strip()
    Name = document.getElementById("name").value.strip()
    Email = document.getElementById("email").value.strip()


    # Validating if they completed the input field
    if not Name or not Email or not Age or not Address:
        display("Please fill out personal details before checkout", target="profile")
        return

    # Displays
    display(f"Name: {Name}", target="Name")
    display(f"Email: {Email}", target="Email")
    display(f"Age: {Age}", target="Age")
    display(f"Address: {Address}", target="Address") #Extra input field
    

    # Multiline display
    display(
    f"""Hello, {Name}!
    Your student\'s address is {Address}
    your student age is {Age}.
    Your email, {Email}, will be confirmed shortly. Remember, \" Education is the most powerful weapon which you can use to change the world.\" - Nelson Mandela""",
    target="profile"
)

    




  

