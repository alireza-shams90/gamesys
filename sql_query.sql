select t.member_id
     , t.calendar_year_month                                                      -- here after finding the previous month played and use of flag that
     , case when t.calendar_year_month = prev_month_played then 'New'             -- whether played on the current month can apply case when statement as required
            when t.played_flag is not null and months_between(to_date(t.calendar_year_month,'yyyymm'),to_date(t.prev_month_played,'yyyymm')) = 1 then 'Retained'
            when t.played_flag is not null and months_between(to_date(t.calendar_year_month,'yyyymm'),to_date(t.prev_month_played,'yyyymm')) != 1 then 'Reactivated' 
            when t.played_flag is null and months_between(to_date(t.calendar_year_month,'yyyymm'),to_date(t.prev_month_played,'yyyymm')) = 1 then 'Unretained' 
            when t.played_flag is null and months_between(to_date(t.calendar_year_month,'yyyymm'),to_date(t.prev_month_played,'yyyymm')) != 1 then 'Lapsed' end as member_lifecycle_status
     , case when t.played_flag is null and months_between(to_date(t.calendar_year_month,'yyyymm'),to_date(t.prev_month_played,'yyyymm')) != 1 
       then months_between(to_date(t.calendar_year_month,'yyyymm'),to_date(t.prev_month_played,'yyyymm')) end as lapsed_month
  from(
with tmp as
(select r.member_id            -- this select statement is designed to select member_id, activity_year_month, flag that whether the player played on the month 
       , r.activity_year_month  -- and previous month that palyed by using lag of activity year month(default value min activity_year_month) partitioned by member id 
       , max(case when r.wager_amount is not null then 'Yes' end) as played_flag   -- grouped by member_id and activity year month.
       , lag(r.activity_year_month, 1, min(activity_year_month))ignore nulls over (partition by r.member_id order by r.activity_year_month) as prev_month_played
       , max(activity_year_month) over (partition by r.member_id) as latest_play
    from revenue_analysis r
   where r.bank_type_id = 0
   group by r.member_id, r.activity_year_month)
 select c.calendar_year_month  -- this aggregated select statements joins calender to the query above with partition by(member_id) to get all the months.
      , r.member_id            -- The coalesce designed to get the previous month player put wager on. It first tries to get the previous month played which is not null for
      , r.played_flag          -- the month that played on them. For other months it gets the lead value of previous month. At this stage all populated correctly but need
      , coalesce( prev_month_played   -- to find the previous month played for the records after the latest month played. Really complicated but worth it as it works fine!
                , lead(prev_month_played, 1) ignore nulls over (partition by member_id order by c.calendar_year_month)
                , max(latest_play) over (partition by r.member_id)  ) as prev_month_played
   from calendar c 
   left join tmp r
        partition by (r.member_id)
     on r.activity_year_month = c.calendar_year_month
  group by c.calendar_year_month, r.member_id, r.played_flag, r.prev_month_played, latest_play) t
  where t.calendar_year_month >= prev_month_played   -- as lead used, the months before first play need to be removed as asked
