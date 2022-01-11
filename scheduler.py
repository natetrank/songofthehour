from grab_song import *

from apscheduler.schedulers.blocking import BlockingScheduler


def scheduler():

    schdlr = BlockingScheduler()
    schdlr.add_job(grab_song, 'interval', seconds=10)
    schdlr.start()

if __name__ == "__main__":
    scheduler()
