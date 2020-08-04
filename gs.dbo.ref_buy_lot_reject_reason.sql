create table ref_buy_lot_reject_reason(
[uid] bigint identity (1,1), 
createdDate  datetime default current_timestamp, 
item_id nvarchar(max), 
item_name_ru nvarchar(max), 
item_name_kz nvarchar(max))
select * from ref_buy_lot_reject_reason
delete from ref_buy_lot_reject_reason
select DISTINCT *   from ref_buy_lot_reject_reason