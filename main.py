#!/bin/python
import time
import curses
import argparse

def countdown(minutes):
    total_seconds = minutes * 60
    def run_countdown(stdscr):
        nonlocal total_seconds
        prev_timer = ""
        try:
            while total_seconds > 0:
                minutes, seconds = divmod(total_seconds, 60)
                timer = '{:02d}:{:02d}'.format(minutes, seconds)
                if timer != prev_timer:
                    stdscr.addstr(0, 0, timer)
                    stdscr.refresh()
                    prev_timer = timer
                time.sleep(1)
                total_seconds -= 1

            stdscr.addstr(0, 0, "Time's up! Take a break!")
            stdscr.refresh()
            time.sleep(2)
        except KeyboardInterrupt:
            stdscr.addstr(1, 0, "Countdown interrupted. Exiting gracefully...")
            stdscr.refresh()
            time.sleep(2)

    curses.wrapper(run_countdown)

def pomodoro_timer(work_minutes=25, short_break_minutes=5, cycles=4):
    for cycle in range(1, cycles + 1):
        print(f"Pomodoro {cycle}: Work for {work_minutes} minutes")
        countdown(work_minutes)

        if cycle < cycles:
            print(f"Take a short break for {short_break_minutes} minutes")
            countdown(short_break_minutes)

    print("All pomodoro cycles complete! Great job!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pomodoro Timer")
    parser.add_argument('-w', '--work', type=int, default=25, help='Work duration in minutes')
    parser.add_argument('-b', '--break', type=int, default=5, help='Short break duration in minutes')
    parser.add_argument('-c', '--cycles', type=int, default=4, help='Number of Pomodoro cycles')
    args = vars(parser.parse_args())

    # Validate input arguments
    if args["work"] <= 0:
        raise ValueError("Work duration must be a positive integer.")
    if args["break"] < 0:
        raise ValueError("Break duration must be a non-negative integer.")
    if args["cycles"] <= 0:
        raise ValueError("Number of cycles must be a positive integer.")

    pomodoro_timer(work_minutes=args["work"], short_break_minutes=args["break"], cycles=args["cycles"])
