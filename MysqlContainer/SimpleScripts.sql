use mydatabase;

select * from User;

SELECT FirstName, Email, DateOfHire FROM User WHERE DateOfHire > '2020-10-20' AND DateOfHire < '2020-12-20';

SELECT count(*) as AmountOfUsers FROM User WHERE DateOfHire > '2020-10-20' AND DateOfHire < '2020-12-20';


