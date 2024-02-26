# Store standard routes for user navigation

# Importing note
from .models import Note
# Importing db
from . import db
# A blueprint has urls defined, it is a way to separate app, views can be defined in multiple files, 
# render_template renders the html templates,
# request works with HTTP request,
# flash flashes a message,
# redirect is used to redirect to an url_for,
# jsonify jsonifies
from flask import Blueprint, render_template, request, flash, jsonify
# Importing flask login_user, login_required, logout_user, current_user
from flask_login import login_required, current_user
# Import json
import json


# Define the views blueprint (views = blueprint name)
views = Blueprint("views", __name__)

# Main page: /
# @ -> Decorator
@views.route("/", methods=["GET", "POST"])
# Makes so you cannot get to the home page if not logged in
@login_required
def home():
    # Checks the method on the request
    if request.method == "POST":
        # Gets the note on request form
        note = request.form.get("note")

        # Checks if length of the note is lesser than 1
        if len(note) < 1:
            # Flash error message
            flash("Note is too short", category="error")
        else:
            # Receives note data for the user
            new_note = Note(data=note, user_id=current_user.id)
            # Adds new_note to the database
            db.session.add(new_note)
            # Commits the addition
            db.session.commit()
            # Flash success message
            flash("Note Added!", category="success")

    # Renders the template, can pass variables and therefore values
    return render_template("home.html", user=current_user)

# Creating endpoint to delete the note
@views.route("/delete-note", methods=["POST"])
def delete_note():
    # Getting data from javascript json.stringify, loading as an python dictionary
    note = json.loads(request.data)
    # Access the id attribute
    noteId = note["noteId"]
    # Look for the note that has this id
    note = Note.query.get(noteId)
    # If the note exists
    if note:
        # If the note belongs to the logged in user
        if note.user_id == current_user.id:
            # Method to delete parameter passed from database
            db.session.delete(note)
            # Commits the deletion
            db.session.commit()
    # Returns an empty response
    return jsonify({})
