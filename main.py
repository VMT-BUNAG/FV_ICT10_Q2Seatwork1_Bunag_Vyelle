from pyscript import document, display

# List of ICT club members
members = ["Nuggets Zu", "Prince Joshtin", "Kuya Nimo", "Vyelle Bunag"]

# Verifying the candidate's name
def check_name(e):
    first = document.getElementById("first").value
    last = document.getElementById("last").value

    fullname = (first + " " + last).title()
    result = fullname in members

    messages = {
        True: "Congratulations " + fullname + "! You are now part of the ICT Club.",
        False: "Sorry " + fullname + ", your name is not on the list."
    }

    display(messages[result], target="output")

# Clearing the input fields
def clear_name(e):
    document.getElementById("first").value = ""
    document.getElementById("last").value = ""
    document.getElementById("output").innerHTML = ""