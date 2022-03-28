import os

def fromFile(filename):
  with open(os.path.join(os.path.dirname(__file__), 'data', filename), 'r', encoding='utf8') as f:
    return f.read()
  return
