# Url Shortening Service
Given a url, generate a short url and store the hash value.
[ URL ] -> [ Hash Func ]-> [ Hash Value ] -> [ User_id + Hash Value ] -> [ Short Url ] -> [ DB [ Key -> Url ]  ]


# Hashing
Hashing is the process of generating a key and value pair from a piece of data.The key is the hash value obtained from a hash function. This key is related to its value in a dictionary for easier read and write.

## Hash Function
Hash function is a pure function (produces the same output with the same input always) which produces a key known as the hash **value**

# Short Url Form
`domain/uhh-uhh-uhh-uhh`
- domain - shorturl.com
- u - Segmented user_id (uuuu)
- h - Segmented hash of main url (hhhhhhhhhh)

# User id
Each User will have a unique id that will contribute in generating the short url.
- Random values from capital to lower case, and numbers from 0 to 9 make up the user_id
- When an id is created, it is compared to the database to check for existing one.

