# Flight_Ticket_Booking_System
This project is accomplished using integration of python with MySQL.

Flight Ticket Booking provides the ability to book airline tickets, cancel them, update the information, delete the records and checking the details of flights. The system contains the following processes:
1.	Book one way or round flight tickets.
2.	Change the name or phone number of the ticket bearer.
3.	Delete the record of a customer
4.	Check the details of a customer’s ticket by entering their necessary details.
The program starts with giving the user the option to book their ticket, check the details of their ticket, have the admin login or simply exit.

If the user chooses the option to book their tickets then they need to enter their information and choose either one way or round flight as their option.
The user can check and confirm their details using the second option. They only need to enter their name, phone number and flight type to check the database and confirm their tickets. This also allows the user to cancel their tickets if needed.

The third option is intended to be used by an admin or a manager. This option requires a username and password to be entered to gain admin access. The admin can delete, update and check the condition of flights with this option. 

The last option simply exits the program.

The user is given the option to go back at every step and if the user enters any wrong option then an appropriate message is flashed against the user to enter a correct option. The flights to be chosen by the user are selected by the help of a random function which chooses the table of flights at random. This program features a discount system in which the logic of the discount code is that the number should be 12 digits long and the sum of the digits should be divisible by 11.


The program uses the following tables in MySQL.

![custonetable](https://github.com/Kuber144/Flight_Ticket_Booking_System/blob/main/pictures/customeroneway.png)
![custroundtable](https://github.com/Kuber144/Flight_Ticket_Booking_System/blob/main/pictures/custemround.png)
![flt1](https://github.com/Kuber144/Flight_Ticket_Booking_System/blob/main/pictures/flight1.png)
## The table flight1 has the default values:-
![flt1val](https://github.com/Kuber144/Flight_Ticket_Booking_System/blob/main/pictures/flight1_val.png)
![flt2](https://github.com/Kuber144/Flight_Ticket_Booking_System/blob/main/pictures/flight2.png)
## The table flight2 has the default values:-
![flt2val](https://github.com/Kuber144/Flight_Ticket_Booking_System/blob/main/pictures/flight2_val.png)
![flt3](https://github.com/Kuber144/Flight_Ticket_Booking_System/blob/main/pictures/flight3.png)
## The table flight3 has the default values:-
![flt3val](https://github.com/Kuber144/Flight_Ticket_Booking_System/blob/main/pictures/flight3_val.png)
![flt4](https://github.com/Kuber144/Flight_Ticket_Booking_System/blob/main/pictures/flight4.png)
## The table flight4 has the default values:-
![flt4val](https://github.com/Kuber144/Flight_Ticket_Booking_System/blob/main/pictures/flight4_val.png)
![mangr](https://github.com/Kuber144/Flight_Ticket_Booking_System/blob/main/pictures/manager.png)
## The table manager has the default values:-
![mngrval](https://github.com/Kuber144/Flight_Ticket_Booking_System/blob/main/pictures/manager_val.png)

# The commmands used to create the tables in MySQL are listed below:-
create database flightbook;

use flightbook;

create table customeroneway(name varchar(30),phonenum bigintdest_place varchar(20),dest_date varchar(15),passengers int(3),Flight_Name varchar(10),cost decimal(10,4),disc varchar(1));

create table customeround(name varchar(30),phonenum bigint,dest_place varchar(20) dest_date varchar(15),ret_place varchar(20),ret_date varchar(15),passengers int(3),flight_name_dest varchar(7),flight_name_ret varchar(7),cost decimal(10,4),disc varchar(1));

create table flight1(srno int(2),flight_timing varchar(15),flight_name varchar(7) primary key,duration varchar(7),fare varchar(10));

create table flight2(srno int(2),flight_timing varchar(15),flight_name varchar(7) primary key,duration varchar(7),fare varchar(10));

create table flight3(srno int(2),flight_timing varchar(15),flight_name varchar(7) primary key,duration varchar(7),fare varchar(10));

create table flight4(srno int(2),flight_timing varchar(15),flight_name varchar(7) primary key,duration varchar(7),fare varchar(10));

create table manager(user varchar(20),password varchar(20));

DETAILS:

insert into manager values(“mngr3459”,”mn123424”);

insert into manager values(“retlr5676”,”rr5437”);

insert into manager values(“hlo1326”,”bs243”);

insert into flight1 values(1,”02:10-04:20”,”6E 6371”,”2h 10m”,”INR 6370”);

insert into flight1 values(2,”07:30-08:20”,”6E 7820”,”50m”,”INR 9370”);

insert into flight1 values(3,”10:10-13:20”,”6E 9810”,”3h 10m”,”INR 4210”);

insert into flight1 values(4,”14:30-16:20”,”6E 4517”,”1h 50m”,”INR 7910”);

insert into flight1 values(5,”23:00-00:20”,”6E 9513”,”2h 20m”,”INR 6200”);

insert into flight1 values(6,”20:10-22:30”,”6E 6598”,”2h 20m”,”INR 6390”);

insert into flight1 values(7,”11:10-12:20”,”6E 3412”,”1h 10m”,”INR 8780”); 

insert into flight1 values(8,”04:10-05:40”,”6E 9845”,”2h 30m”,”INR 5790”);

insert into flight1 values(9,”01:50-03:00”,”6E 0845”,”1h 10m”,”INR 8945”);

insert into flight1 values(10,”05:30-07:10”,”6E 3476”,”1h 40m”,”INR 7910”);

insert into flight2 values(1,”02:20-05:10”,”6E 2376”,”2h 50m”,”INR 5670”);

insert into flight2 values(2,”04:40-06:20”,”6E 3282”,”1h 40m”,”INR 8000”);

insert into flight2 values(3,”07:40-09:40”,”6E 2893”,”2h”,”INR 6580”);

insert into flight2 values(4,”08:30-11:30”,”6E 3876”,”3h”,”INR 4010”);

insert into flight2 values(5,”10:00-11:30”,”6E 3974”,”1h 30m”,”INR 8020”);

insert into flight2 values(6,”11:00-11:55”,”6E 3018”,”55m”,”INR 9300”);

insert into flight2 values(7,”12:00-13:20”,”6E 3027”,”1h 20m”,”INR 8580”); 

insert into flight2 values(8,”13:00-14:00”,”6E 2836”,”1h”,”INR 8800”);

insert into flight2 values(9,”15:00-17:10”,”6E 2982”,”2h 10m”,”INR 6400”);

insert into flight2 values(10,”19:00-21:05”,”6E 9378”,”2h 5m”,”INR 6450”);

insert into flight3 values(1,”02:10-04:20”,”6E 2323”,”2h 10m”,”INR 6370”);

insert into flight3 values(2,”07:30-08:20”,”6E 2355”,”50m”,”INR 9370”);

insert into flight3 values(3,”10:10-13:20”,”6E 4686”,”3h 10m”,”INR 4210”);

insert into flight3 values(4,”14:30-16:20”,”6E 8654”,”1h 50m”,”INR 7910”);

insert into flight3 values(5,”23:00-00:20”,”6E 9543”,”2h 20m”,”INR 6200”);

insert into flight3 values(6,”20:10-22:30”,”6E 9463”,”2h 20m”,”INR 6390”);

insert into flight3 values(7,”11:10-12:20”,”6E 8346”,”1h 10m”,”INR 8780”); 

insert into flight3 values(8,”04:10-05:40”,”6E 1446”,”2h 30m”,”INR 5790”);

insert into flight3 values(9,”01:50-03:00”,”6E 1526”,”1h 10m”,”INR 8940”);

insert into flight3 values(10,”05:30-07:10”,”6E 9354”,”1h 40m”,”INR 7900”);

insert into flight4 values(1,”15:00-17:00”,”6E 5474”,”2h”,”INR 6200”);

insert into flight4 values(2,”16:20-18:20”,”6E 7674”,”2h”,”INR 6230”);

insert into flight4 values(3,”17:10-18:00”,”6E 5795”,”50m”,”INR 9230”);

insert into flight4 values(4,”20:00-21:40”,”6E 6780”,”1h 40m”,”INR 7800”);

insert into flight4 values(5,”22:00-00:30”,”6E 0846”,”2h 30m”,”INR 5970”);

insert into flight4 values(6,”01:00-03:10”,”6E 6587”,”2h 10m”,”INR 6300”);

insert into flight4 values(7,”03:00-04:50”,”6E 4658”,”1h 50m”,”INR 7210”); 

insert into flight4 values(8,”04:00-05:00”,”6E 7648”,”1h”,”INR 8580”);

insert into flight4 values(9,”05:40-08:00”,”6E 0968”,”2h 20m”,”INR 6000”);

insert into flight4 values(10,”08:50-10:00”,”6E 4326”,”1h 10m”,”INR 8880”);
