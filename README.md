# Final Project (Jack Chilton)

## To run the program

Run the **jrchilto_ProjectGUI.py** file in the PyCharm window.

## Functionality

### Check in to gym

#### Upon clicking the Check In button to run the check_in function:

A new instance of the Member Class will be created if there is a new gym member with a Member ID that has never been
entered before. The new member will be added to the members.json file.

An instance of the Member Class has the following information:

* Member ID: The ID number of the member, which must be a 4-digit number such as "0001"
* Ball Status: Either a 0 or 1 to determine whether the member has checked out a basketball that has yet to be checked
back in (1 means the ball has yet to be checked back in)
* Fine: The amount the gym member owes if the member pays a fine for not successfully returning a ball

A new or existing gym member will have their ball status attribute changed if the member checks out a basketball, also 
updating their ball status in the members.json file.

#### Important Note

A gym member will **not** be allowed to check in to the gym if the member has not checked their basketball back in. In 
this case, he or she must pay a fine to be allowed to check back in to the gym.

### Pay Fine

Allows the member to pay a $60 fine to be allowed back into the gym if the member has yet to check their basketball back
in.

By clicking the Pay Fine button, the pay_fine function will add 60 to the fine attribute and set the ball status
attribute to 0 in the members.json file.

### Check In Basketball

Upon moving to the second GUI page, the Check In Basketball button will appear to call the ball_check_in function, which
sets the member's ball status to 0 in the members.json file.

### Exit

The Exit button will call the exit function to close the application.

## Data File

### members.json

```json
{"0001": {"Ball Status": 0, "Fine": 0}, "0002": {"Ball Status": 0, "Fine": 60}, "0003": {"Ball Status": 1, "Fine": 0}}
```

## Class

### Member Class

#### Variables

Each instance of the Member Class has these instance variables:
1. gym_id: public, string
2. ball_status: public, int, default value = 0
3. fine: public, int, default value = 0
4. ball_status getter
5. ball_status setter
6. fine getter
7. fine setter

#### Methods

Each instance of the Member Class has these instance methods:
* The dunder "**init**" method
* The dunder "**str**" method


## Auto Testing

Run the following command to test the test_member.py file

```shell
$ pip install pytest
$ pytest -v
```
