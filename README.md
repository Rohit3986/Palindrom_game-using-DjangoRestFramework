# Palindrom_game-using-DjangoRestFramework
I have divided this project into two blocks :- usermanagement and gamemanagement
In usermanagement i have added facilty of user create,user update and user delete
Only admin (superuser) have permission to delete any user's account
User can access and update only their account
Superuser can to update any user's information

#GameManagement
By hitting creategame endpoint game_id will be created automatically
this endpoint will raise exception when user with registered game id will try to re-create
and user(player) can add value in updateboard endpoint
when string length will reach to 6 then user can check weather the string is palindrome or not
in updatedboard endpoint when user can send a simple get request he can get information of all the register game ids.
