### 1. Expand the flask app from class to add functions to create, update, and delete records. Use the mongodb documentation https://docs.mongodb.com/manual/reference/ . Create can use insert_one method, update can use update_one, and delete can use delete_one

## Homepage 
### Displays all the records
![image](https://user-images.githubusercontent.com/90784468/156877562-fc4a9e63-3c55-4660-a872-f6124c5796c6.png)

## Create 
### Displays form to add a new entry
* Here I add an entry for the show "SharkTank" and I leave the year column entry. We will see later how I use update function to add the year data.
![insert](https://user-images.githubusercontent.com/90784468/156877581-3bf99c32-20ea-49ca-8331-62e407d4306f.PNG)
### New entry displayed on homepage
![post_insert](https://user-images.githubusercontent.com/90784468/156877592-b0448e4d-9726-4229-aea2-66bbc0cc6535.PNG)

## Update
### Displays form to update an existing entry
* Here I query the existing entry by name and add all the data related to it including the year this time.
![update](https://user-images.githubusercontent.com/90784468/156877447-c059a92d-375d-49b9-a177-ed8190000d96.PNG)
### update entry displayed on homepage
![post_update](https://user-images.githubusercontent.com/90784468/156877454-642ad86d-c71d-4247-b304-f94e50cac751.PNG)

## Deletion
### Displays the form to enter the name of the record to query for deletion
![image](https://user-images.githubusercontent.com/90784468/156877498-674abf07-65f4-4eb4-ac6e-091df1ba6db5.png)
![Delete](https://user-images.githubusercontent.com/90784468/156877510-09c31356-fe75-43e2-a436-1da5b66d9d6a.PNG)
### Entries displayed on homepage post deletion
![post_del](https://user-images.githubusercontent.com/90784468/156877524-505bba82-13f0-49cb-a644-48e4a8e4db62.PNG)
