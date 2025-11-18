import hashlib

# Document dirty checking - collision would just trigger unnecessary save
class DocumentEditor:
    def __init__(self, content):
        self.content = content
        self.saved_hash = hashlib.sha256(content.encode()).hexdigest()

    def is_dirty(self):
        current_hash = hashlib.sha256(self.content.encode()).hexdigest()
        return current_hash != self.saved_hash

    def save(self):
        # Save document to disk
        self.saved_hash = hashlib.sha256(self.content.encode()).hexdigest()
        return "Document saved"


# Usage
editor = DocumentEditor("Initial content")
print(editor.is_dirty())  # False

editor.content = "Modified content"
print(editor.is_dirty())  # True - triggers save prompt

editor.save()
print(editor.is_dirty())  # False again