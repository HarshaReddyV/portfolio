-- Keep a log of any SQL queries you execute as you solve the mystery.

--Accessing the crime reports
SELECT description FROM crime_scene_reports WHERE  day=28 AND year=2020 AND month = 7;

--Checking the interviews of 3 people
SELECT transcript FROM interviews WHERE  day=28 AND year=2020 AND month = 7;

--Accessing court house logs to check
SELECT license_plate,activity FROM courthouse_security_logs
WHERE year=2020 AND month=7 AND day=28 AND hour=10 AND minute=16;

--License plate is "5P2BI95"
-- 10:16 as they are delayed by 1 minute is exit and 10:14 is entrance so 10:16 is the right time

---reviewing atm transactions
SELECT atm_location,account_number,transaction_type,amount FROM atm_transactions
WHERE year=2020 AND month=7 AND day=28 AND atm_location="Fifer Street";




--checking phone call
SELECT caller,receiver,duration FROM phone_calls
WHERE year=2020 AND month=7 AND day=28 AND duration<60;

--checking bank account
SELECT account_number,name,creation_year FROM bank_accounts
JOIN people ON people.id = bank_accounts.person_id ORDER BY account_number DESC;

--orgin airport
SELECT year,month,day,hour,minute,full_name FROM flights
JOIN airports ON flights.origin_airport_id = airports.id
WHERE year=2020 AND month=7 AND day=29 ORDER BY hour ASC;


--checking departure flights
SELECT year,month,day,hour,minute,full_name FROM flights
JOIN airports ON flights.destination_airport_id = airports.id
WHERE year=2020 AND month=7 AND day=29 ORDER BY hour ASC;

--seems like 8:20 is trhe earliest out of fiftyville and to heathrow

--checking passenger info
SELECT passport_number,seat FROM passengers
JOIN flights ON passengers.flight_id = flights.id
WHERE year=2020 AND month=7 AND day=29 AND hour = 8 AND minute=20;


SELECT name,phone_number,passport_number FROM people
WHERE license_plate = "5P2BI95";