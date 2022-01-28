### Tagging Service
Create a microservice which allots tags to different entities

Use case:
Multiple entities exist in the system - Users, Products, Plans, Quizzes etc.
A centralized tagging microservice will assign any number of "tags" to instances of different entities.
Eg: 

STEP 1
When a user with user_id "johndoe_12312312acxasc" carries out a purchase of electronics - the order service tells tagging microservice to tag "User" with "ID" "johndoe_12312312acxasc" with an additional tag "electronics"


As every entity has it's own microservice, once the tag is set, the tagging microservice will also notify the entity's service about the new tag.

Eg:
STEP 2
When the User "johndoe_12312312acxasc" had a tag "electronics" added - the net tags on the user are now: ["user","premium","electronics"] -> this is POSTed on users/update API
