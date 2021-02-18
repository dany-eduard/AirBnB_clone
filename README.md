# AirBnB clone - The console

![project_logo](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210218%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210218T034209Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2dadd7694b6e44d37793cb1919a50e163b765877c58602dea90aafe2f5abbc78)

## Description

This repository contains the first part of the AirBnB_clone project, which consists of an AirBnb Web Clone. This first part consists of a command interpreter to manage the AirBnB objects (User, State, City, Place).

## Description of the command interpreter

Just like a Shell, this command line works the same. But limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

### To use the command interpreter

Follow these steps:

1. Clone repository: `git clone https://github.com/dany-eduard/AirBnB_clone.git`
2. Enter the directory and run the file [console.py](https://github.com/dany-eduard/AirBnB_clone/blob/main/console.py): `cd AirBnB_clone && ./console.py` for run on interactive mode.
3. Have fun trying out the available commands.

### Available commands

| Commands  | Description                                                                                                                | Example                                                                                                                                             |
| --------- | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `create`  | Create a new instance of `BaseModel` and save it to the JSON file                                                          | `(hbnb) create <class name>`                                                                                                                        |
| `show`    | Prints the string representation of an instance based on the class name and id.                                            | `(hbnb) show <class name> 1234-1234-1234` or write `<class name>.show(<id>)`                                                                        |
| `destroy` | Deletes an instance based on the class name and id and save the change into the JSON file.                                 | `(hbnb) destroy <class name> 1234-1234-1234` or write `<class name>.destroy(<id>)`                                                                  |
| `all`     | Prints all string representation of all instances based or not on the class name.                                          | `(hbnb) all <class name>` or write `<class name>.all()`                                                                                             |
| `update`  | Updates an instance based on the class name and id by adding or updating attribute and save the change into the JSON file. | `(hbnb) update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"` or write `<class name>.update(<id>, <attribute name>, <attribute value>` |
| `count`   | Print the number of instances stored in the JSON file.                                                                     | `(hbnb) User.count()`                                                                                                                               |
| `help`    | The `help` command is built into Cmd. With no arguments, help displays the list of available commands.                     | `(hbnb) help`                                                                                                                                       |
| `EOF`     | The end of file marker is sent to do_EOF (). If a command handler returns true, the program will exit cleanly.             | `(hbnb) ctrl+D`                                                                                                                                     |
| `quit`    | Use it to exit the console, as an alternative to `EOF`                                                                     | `(hbnb) quit`                                                                                                                                       |

## Examples

![Example-imge](https://raw.githubusercontent.com/dany-eduard/AirBnB_clone/main/Example_CommandLineAirBnB-2021-02-18%20104733.png)

## Environment

- Language: Python
- OS: Ubuntu 14.04 LTS
- Style guidelines: PEP8

## Authors

- [AndresSern](https://github.com/AndresSern) - <andrecamposer@gmail.com>
- [Daniel Eduardo Almagro](https://github.com/dany-eduard) - <danyeduard17@gmail.com>
