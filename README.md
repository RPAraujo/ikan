# IKAN is a YAML to ANKI script

## Create Cards
Create a new yaml file with the following structure:
```
deck: Programming::Golang::HTTP
tags: ["golang", "go", "HTTP"]
cards:
  - front: How do you add a Handler to and HTTP server in Go?
    back: >-
      http.HandleFunc("/", handleFunction)
      
      The handleFunction must have the following signature:
      func ProductsHandler(w http.ResponseWriter, r *http.Request) {...}

      And according to the http method in the request perform the required logic
```

This will create the `Programming::Golang::HTTP` if it does not exist and add the basic card to it.

## Delete Cards
To delete an existing card just add the `delete:true` flag to the yaml of the card:
```
deck: Programming::Golang::HTTP
tags: ["golang", "go", "HTTP"]
cards:
  - front: How do you add a Handler to and HTTP server in Go?
    back: >-
      http.HandleFunc("/", handleFunction)
      
      The handleFunction must have the following signature:
      func ProductsHandler(w http.ResponseWriter, r *http.Request) {...}

      And according to the http method in the request perform the required logic
    delete: true
```
Once the script runs, the card will be deleted and will not be added while the flag is set.
If you want you can delete the card entry from the yaml file

## Update Cards
If you need to update the text from and existing card, you can do so. Just add the `update:true` flag to the yaml of the card:
```
deck: Programming::Golang::HTTP
tags: ["golang", "go", "HTTP"]
cards:
  - front: How do you add a Handler to and HTTP server in Go?
    back: >-
      http.HandleFunc("/", handleFunction)
      
      The handleFunction must have the following signature:
      func ProductsHandler(w http.ResponseWriter, r *http.Request) {...}

      And according to the http method in the request perform the required logic
    update: true
```
While this flag is set the script will always update the card.
After you run the update you can choose to remove or leave the flag.

All the operation are idempotent so running the script multiple times will always leave the deck in the same state.