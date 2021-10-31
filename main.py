import hashlib
from utils import score_hash, encode_value

# assuming list of users with the flag turned on
users = {}
for number in range(1000000):
  users['{}@gmail.com'.format(number)] = True

rollout_percentage = 20

def get_flag_value(key):
  if users[key]:
    hashed = hashlib.sha1(encode_value(key))  # nosec
    score = score_hash(hashed)
    return score <= rollout_percentage

# tests
if __name__ == '__main__':
  total_true = 0
  for user in users:
    if get_flag_value(user) == True:
      total_true += 1
  print('true', total_true)