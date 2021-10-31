import hashlib
import json

# assuming list of users with the flag turned on
users = {}

for number in range(1000000):
  users['{}@gmail.com'.format(number)] = True

# print(users)

rollout_percentage = 20

def score_hash(hashed):
  num = int(hashed.hexdigest(), 16)
  # print(num, num % 100)
  return (num % 100)

def encode_value(value):
  return json.dumps(value).encode("utf-8")

def get_flag_value(key):
  if users[key]:
    hashed = hashlib.sha1(encode_value(key))  # nosec
    score = score_hash(hashed)
    return score <= rollout_percentage


# tests
total_true = 0
for user in users:
  if get_flag_value(user) == True:
    total_true += 1
print('true', total_true)