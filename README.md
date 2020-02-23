# Concert Booking
## Structor
- Actor
	- Add Actor
	- Edit Actor
	- Delete Actor
	- Get Actor
- Booking
	- Add Booking
	- Edit Booking
	- Delete Booking
	- Get Booking
- Concert
	- Add Concert
	- Edit Concert
	- Delete Concert
	- Get Concert
- Users
	- Sign Up
	- Sign In
	- Show Booking Concert each of users
	- Differance roles between admin adn user
- Home
	- Show Infomation Concert
	

## Interface, Model
- Booking
	- id_booking
	- id_concert
	- id_users
	- date_booking
	- count_concert_ticket
	- status_booking # 0 is not confirm, 1 is confirm
- Concert
	- id_concert
	- name_concert
	- date_play
	- date_buy
	- date_end_buy
- GroupConcertAndActor
	- id_group
	- id_concert
	- id_actor
- Users
	- id_user
	- name_user
	- username
	- password
	- role ## 1 is admin , 2 is user
- Actor
	- id_actor
	- name_actor
	- detail_actor
	- age_actor

## Role
- Admin 
	- Add
	- Delete
	- Edit
	- Get
- User
	- Get
	- Booking

