##/////////////////////////////////////
create schema if not exists Assignment;
use Assignment;

#Import 5 Tables using right click on assignment->Tables-> Table Data Import Wizard. 
#Name of the tables should be same has csv file name. But ensure space is replace with "_" in table name. 

#Bajaj Auto -> 888 records imported
#Eicher Motors -> 888 records imported
#Hero Motocor -> 888 records imported
#Infosys -> 888 records imported
#TCS -> 888 records imported
#TVS_Motors -> 888 records imported


select count(*) from bajaj_auto;
select count(*) from eicher_motors;
select count(*) from hero_motocorp;
select count(*) from infosys;
select count(*) from tcs;
select count(*) from tvs_motors;

#////////////////////////////////////////////////////////////
#Create a date table with unique  date field for all the transaction dates. 
#In these kind of projects when we are joining data from multiple tables (on date field) 
#it is a best practice to have a common date table. 
#This will help in avoiding chaos which can happen because of joins.
#Date1 is original imported date and date2 is formated date in mysql date format.

drop table if exists dates;
create table dates 
(
(
SELECT date as date1, STR_TO_DATE(date,'%d-%M-%Y') as date from bajaj_auto
union
SELECT date as date1, STR_TO_DATE(date,'%d-%M-%Y') as date  from eicher_motors
union
SELECT date as date1, STR_TO_DATE(date,'%d-%M-%Y') as date  from hero_motocorp
union
SELECT date as date1, STR_TO_DATE(date,'%d-%M-%Y') as date  from infosys
union
SELECT date as date1, STR_TO_DATE(date,'%d-%M-%Y') as date  from tcs
union
SELECT date as date1, STR_TO_DATE(date,'%d-%M-%Y') as date  from tvs_motors) ) ;

select count(*) from dates;
#889 rows.
select * from dates limit 3;


#Join Date table with all other transaction tables.
#///////////////////////////////////////////////////////////
####################QUESTON 2 //////////////////////////////
#Create a master table containing the date and close price of all the six stocks.
#///////////////////////////////////////////////////////////

drop table if exists master;
create table master as 
(select d.date, b.`close price` as 'Bajaj', tcs.`close price` as TCS, 
tvs.`close price` as TVS, i.`close price` as Infosys, e.`close price` as 'Eicher',
h.`close price` as Hero from dates d 
left join bajaj_auto b    on d.date1 = b.date  
left join TCS             on d.date1 = tcs.date 
left join TVS_motors tvs  on d.date1 = tvs.date 
left join infosys i       on d.date1 = i.date 
left join eicher_motors e on d.date1 = e.date 
left join Hero_motocorp h on d.date1 = h.date);

select count(*) from master limit 5; 

select * from master where Bajaj is null;
select * from master where tcs is null;

#31-Aug-17 There is no trading in Bajaj & Infosys so no transaction record available for this date
#9-Dec-15 There is no trading in TCS, TVS, Eicher & Hero, so no transaction record available for this date
#This was the reason creating date table helps.

#///////////////////////////////////////////////////////////
####################QUESTON 1 //////////////////////////////
#Create a new table named 'bajaj1' containing the date, close price, 20 Day MA and 50 Day MA.
#///////////////////////////////////////////////////////////
drop table if exists bajaj1;

create table bajaj1
select date , bajaj as 'Close Price',
round(avg(bajaj) over (order by date rows between 19 preceding and 0 following),2) as '20 Day MA',
round(avg(bajaj) over (order by date rows between 49 preceding and 0 following),2) as '50 Day MA' 
from master;

select * from bajaj1 limit 115;

#####
drop table if exists tcs1;
create table TCS1
select date, TCS as 'Close Price',
round(avg(TCS) over (order by date rows between 19 preceding and 0 following),2) as '20 Day MA',
round(avg(TCS) over (order by date rows between 49 preceding and 0 following),2) as '50 Day MA' 
from master;

select * from TCS1 limit 5;
######
drop table if exists tvs1;

create table TVS1
select date, TVS as 'Close Price',
round(avg(TVS) over (order by date rows between 19 preceding and 0 following),2) as '20 Day MA',
round(avg(TVS) over (order by date rows between 49 preceding and 0 following),2) as '50 Day MA' 
from master;

select * from TVS1 limit 5;
#######
drop table if exists infosys1;

create table INFOSYS1
select date , TCS as 'Close Price',
round(avg(INFOSYS) over (order by date rows between 19 preceding and 0 following),2) as '20 Day MA',
round(avg(INFOSYS) over (order by date rows between 49 preceding and 0 following),2) as '50 Day MA' 
from master;

select * from INFOSYS1 limit 5;
########

drop table if exists eicher1;
create table EICHER1
select date, TCS as 'Close Price',
round(avg(EICHER) over (order by date rows between 19 preceding and 0 following),2) as '20 Day MA',
round(avg(EICHER) over (order by date rows between 49 preceding and 0 following),2) as '50 Day MA' 
from master;

select * from EICHER1 limit 5;
####################
drop table if exists hero1;

create table HERO1
select date , TCS as 'Close Price',
round(avg(HERO) over (order by date rows between 19 preceding and 0 following),2) as '20 Day MA',
round(avg(HERO) over (order by date rows between 49 preceding and 0 following),2) as '50 Day MA' 
from master;

select * from HERO1 limit 5;

#///////////////////////////////////////////////////////////
####################QUESTON 3 //////////////////////////////
#Use the table created in Part(1) to generate buy and sell signal.
#///////////////////////////////////////////////////////////
drop function if exists buy_sell;

delimiter $$
create function buy_sell( day20 float(9,2), day50 float(9,2)) returns varchar(4) deterministic
begin
    declare flag varchar(4);
  
    
        
    if day20>day50 then
		set flag= "BUY";
	elseif day20<day50 then
		set flag= "SELL";
	else
        set flag="Hold";
	end if;
    return flag;
end
$$

delimiter ;

drop table if exists Bajaj2;
create table Bajaj2
select date, buy_sell(`20 Day MA`,`50 Day MA`) as 'Signal' from Bajaj1;
select * from Bajaj2 order by date;

drop table if exists TCS2;
create table TCS2
select date, buy_sell(`20 Day MA`,`50 Day MA`) as 'Signal' from TCS1;
select * from TCS2 order by date;

drop table if exists TVS2;
create table TVS2
select date, buy_sell(`20 Day MA`,`50 Day MA`) as 'Signal' from TVS1;
select * from TVS2 order by date;

drop table if exists Infosys2;
create table Infosys2
select date, buy_sell(`20 Day MA`,`50 Day MA`) as 'Signal' from Infosys1;
select * from Infosys2 order by date;

drop table if exists Eicher2;
create table Eicher2
select date, buy_sell(`20 Day MA`,`50 Day MA`) as 'Signal' from Eicher1;
select * from Eicher2 order by date;

drop table if exists Hero2;
create table Hero2
select date, buy_sell(`20 Day MA`,`50 Day MA`) as 'Signal' from Hero1;
select * from Hero2 order by date;

#///////////////////////////////////////////////////////////
####################QUESTON 4 //////////////////////////////
#Create a User defined function, that takes the date as input and returns the signal for that particular day (Buy/Sell/Hold) for the Bajaj stock.
#///////////////////////////////////////////////////////////
drop function if exists buy_sell_signal;
delimiter $$
create function buy_sell_signal( dateinput varchar(12), stock varchar(10)) returns varchar(4) deterministic
begin
    declare flag varchar(4);
    declare tbl varchar(10);
    if stock="bajaj" then
		select `signal` into @flag from bajaj2 where `date`= str_to_date(dateinput,'%Y-%m-%d'); 
	elseif stock="eicher" then
		select `signal` into @flag from eicher2 where `date`= str_to_date(dateinput,'%Y-%m-%d');
    elseif stock="hero" then
		select `signal` into @flag from hero2 where `date`= str_to_date(dateinput,'%Y-%m-%d');
    elseif stock="infosys" then
		select `signal` into @flag from infosys2 where `date`= str_to_date(dateinput,'%Y-%m-%d');
    elseif stock="tcs" then
		select `signal` into @flag from tcs2 where `date`= str_to_date(dateinput,'%Y-%m-%d');
    elseif stock="tvs" then
		select `signal` into @flag from tvs2 where `date`= str_to_date(dateinput,'%Y-%m-%d');
    
	end if;
    return @flag;
end
$$
delimiter ;

#Enter date in YYYY-MM-DD format. Do not change the stock names. As they are used inside the function.
select buy_sell_signal('2015-03-24',"bajaj") as 'Action';
select buy_sell_signal('2015-03-24',"eicher") as 'Action';
select buy_sell_signal('2015-03-24',"hero") as 'Action';
select buy_sell_signal('2015-03-24',"infosys") as 'Action';
select buy_sell_signal('2015-03-24',"tcs") as 'Action';
select buy_sell_signal('2015-03-24',"tvs") as 'Action';

