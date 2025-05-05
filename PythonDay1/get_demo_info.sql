CREATE DEFINER=`root`@`localhost` PROCEDURE `get_demo_info`(in myid int)
BEGIN
select * from demo where id = myid;
END