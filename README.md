# Pomodoro Timer

## Overview
The Pomodoro Timer is a simple command-line utility that helps you manage your work sessions using the Pomodoro Technique. This technique involves focusing on work for a set period of time (e.g., 25 minutes), followed by a short break, helping you maintain productivity while reducing burnout.

This Python-based Pomodoro Timer uses the `curses` library to provide a dynamic countdown display in the terminal, making it an easy and effective tool for staying on track.

## Features
- Adjustable work and break durations.
- Configurable number of Pomodoro cycles.
- Graceful handling of interruptions (e.g., pressing `Ctrl+C` to stop).
- Visual countdown timer displayed in the terminal.

## Requirements
- Python 3.x

The following Python libraries are required:
- `argparse` (comes with the standard library)
- `time` (comes with the standard library)
- `curses` (comes with the standard library, but may not be available on some non-UNIX systems)

## Installation
Make sure you have Python 3 installed on your system. Clone the repository or copy the script to your local machine.

## Usage
Run the script from your terminal as follows:

```sh
./main.py --work 25 --break 5 --cycles 4
```

### Arguments
- `--work (-w)`: Set the work duration in minutes (default is 25).
- `--break (-b)`: Set the short break duration in minutes (default is 5).
- `--cycles (-c)`: Set the number of Pomodoro cycles (default is 4).

For example, to run the timer with a 30-minute work session, 10-minute break, and 3 cycles:

```sh
./main.py --work 30 --break 10 --cycles 3
```

## Example
```sh
$ ./main.py --work 25 --break 5 --cycles 4
Pomodoro 1: Work for 25 minutes
... (countdown running) ...
Take a short break for 5 minutes
... (countdown running) ...
All pomodoro cycles complete! Great job!
```

## Notes
- The countdown timer will display dynamically in the terminal, updating every second.
- The script handles `Ctrl+C` gracefully, allowing users to exit the timer without abrupt termination.

## Limitations
- The `curses` library might not be available on all platforms (e.g., some versions of Windows). If you encounter compatibility issues, consider using a UNIX-like environment or adapting the script to use an alternative display method.

## License
This project is open-source and available under the MIT License.

## Contributions
Feel free to submit pull requests or open issues for improvements or bug fixes.


