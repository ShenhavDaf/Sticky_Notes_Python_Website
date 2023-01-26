from flask import Blueprint, request, render_template, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, User
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note_text')

        if note:
            new_note = Note(text = note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='succsess')
        else: flash('Note is too short. Try again', category='error')

    return render_template('home.html', user = current_user)


@views.route('delete-note', methods=['POST'])
def deleteNote():
    note = json.loads(request.data)
    noteId = note['note_id']
    note = Note.query.get(noteId)

    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

