INSERT INTO user(username, password)--Insert test user into database
  VALUES(
    ('test', 'password'),
    ('test2', 'password2')
  )

INSERT INTO answers (question, answer)-- Test user has progress of one question in the answers tb
  VALUES(
    ('test question ', 'test answer'),
    ('another question', 'another anwser')
  )

INSERT INTO stats (name, points)-- Has stat values as well
  VALUES(
    ('test Swiftness', 10),
    ('test Strength', 10),
    ('test Luck', 5 ),
    ('test Intelligence', 5),
    (' test Charisma', 5)

  )

INSERT INTO items (name, amount)
  VALUES(
    ('test Rifle', 1),
    ('test Gernade', 3),
    ('test Rations', 9)
  )
