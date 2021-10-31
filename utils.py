import json

def score_hash(hashed):
  num = int(hashed.hexdigest(), 16)
  # print(num, num % 100)
  return num % 100

def encode_value(value):
  return json.dumps(value).encode("utf-8")