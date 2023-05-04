import csv
import json
import os
from datetime import datetime
from typing import List, Tuple


class Note:
    def __init__(self, note_id: int, title: str, body: str, created_at: datetime, updated_at: datetime):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_at = created_at
        self.updated_at = updated_at


class NotesManager:
    def __init__(self, filename: str):
        self.filename = filename
        self.notes = []
        self.load_notes()

    def load_notes(self) -> None:
        """Load notes from the file"""
        if not os.path.isfile(self.filename):
            return

        with open(self.filename, 'r') as file:
            if self.filename.endswith('.json'):
                self.notes = [Note(**note) for note in json.load(file)]
            elif self.filename.endswith('.csv'):
                reader = csv.reader(file, delimiter=';')
                next(reader, None)  # skip the header row
                self.notes = [Note(*row) for row in reader]

    def save_notes(self) -> None:
        """Save notes to the file"""
        if self.filename.endswith('.json'):
            data = [note.__dict__ for note in self.notes]
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=4)
        elif self.filename.endswith('.csv'):
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(['note_id', 'title', 'body', 'created_at', 'updated_at'])
                for note in self.notes:
                    writer.writerow([note.note_id, note.title, note.body, note.created_at, note.updated_at])

    def get_notes(self, from_date: datetime = None, to_date: datetime = None) -> List[Note]:
        """Get notes from the list by date range"""
        if from_date and to_date:
            return [note for note in self.notes if from_date <= note.created_at <= to_date]
        elif from_date:
            return [note for note in self.notes if note.created_at >= from_date]
        elif to_date:
            return [note for note in self.notes if note.created_at <= to_date]
        else:
            return self.notes

    def add_note(self, title: str, body: str) -> Note:
        """Add a new note to the list"""
        note_id = self.get_next_id()
        now = datetime.now()
        note = Note(note_id, title, body, now, now)
        self.notes.append(note)
        return note

    def edit_note(self, note_id: int, title: str, body: str) -> bool:
        """Edit an existing note"""
        for note in self.notes:
            if note.note_id == note_id:
                note.title = title
                note.body = body
                note.updated_at = datetime.now()
                return True
        return False

    def delete_note(self, note_id: int) -> bool:
        """Delete an existing note"""
        for note in self.notes:
            if note.note_id == note_id:
                self.notes.remove(note)
                return True
        return False

    def get_next_id(self) -> int:
        """Get the next note ID"""
        if self.notes:
            return self.notes[-1].note_id + 1
        else:
            return 1
