from apscheduler.scheduler import Scheduler

sched = Scheduler()


@sched.interval_schedule(seconds=5)
def my_job():
    print 'Hello World!'

sched.start()