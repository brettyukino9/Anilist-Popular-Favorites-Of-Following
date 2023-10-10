import csv
import json
import os
import webbrowser
from pip._vendor import requests
import sys
# arg 1 = username

username = sys.argv[1]
queryOld = '''
query($name:String){User(name:$name){id}}
'''

# Define our query variables and values that will be used in the query request
variablesOld = {
    'name': username
}

url = 'https://graphql.anilist.co'

# Make the HTTP Api request
response = requests.post(url, json={'query': queryOld, 'variables': variablesOld}).json()
userId = response['data']['User']['id']

map = {}
query = '''
query ($userId: Int!) {
  a1: Page(page: 1) {
    following(userId: $userId, sort: ID) {
      ...stuff
    }
  }
  a2: Page(page: 2) {
    following(userId: $userId, sort: ID) {
      ...stuff
    }
  }
  a3: Page(page: 3) {
    following(userId: $userId, sort: ID) {
      ...stuff
    }
  }
  a4: Page(page: 4) {
    following(userId: $userId, sort: ID) {
      ...stuff
    }
  }
  a5: Page(page: 5) {
    following(userId: $userId, sort: ID) {
      ...stuff
    }
  }
  a6: Page(page: 6) {
    following(userId: $userId, sort: ID) {
      ...stuff
    }
  }
  a7: Page(page: 7) {
    following(userId: $userId, sort: ID) {
      ...stuff
    }
  }
  a8: Page(page: 8) {
    following(userId: $userId, sort: ID) {
      ...stuff
    }
  }
  a9: Page(page: 9) {
    following(userId: $userId, sort: ID) {
      ...stuff
    }
  }
  a10: Page(page: 10) {
    following(userId: $userId, sort: ID) {
      ...stuff
    }
  }
  User(id: $userId) {
    ...stuff
  }
}

fragment stuff on User {
  name
  favourites {
    characters1: characters(page: 1) {
      nodes {
        name {
          full
        }
      }
    }
    characters2: characters(page: 2) {
      nodes {
        name {
          full
        }
      }
    }
    characters3: characters(page: 3) {
      nodes {
        name {
          full
        }
      }
    }
    characters4: characters(page: 4) {
      nodes {
        name {
          full
        }
      }
    }
  }
}


'''

# Define our query variables and values that will be used in the query request
variables = {
    'userId': userId
}

# Make the HTTP Api request
response = requests.post(url, json={'query': query, 'variables': variables}).json()
print(response)

for x in range(1, 11) :
    for user in response['data']['a'+str(x)]['following'] :
        for y in range(1,5) :
            for i in user['favourites']['characters'+str(y)]['nodes']:
                char = i['name']['full']
                if(char in map) :
                    map[char] = map[char] + 1
                else :
                    map[char] = 1


res = {key: val for key, val in sorted(map.items(), key = lambda ele: ele[1], reverse = True)}
[print(key,':',value) for key, value in res.items()]
with open('Results/'+username+' results.txt', 'w', encoding='utf8') as f:
    for key, value in res.items() :
        f.write(key+' : '+str(value)+"\n")
