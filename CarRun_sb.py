from .mods import (
    CarRun as run,
    servo_ultrasonic_avoid as servo,
    ServoControlColorVersion1 as ctrl1,
    ServoControlColorVersion2 as ctrl2,
)
import simple_chalk as chalk

mods = (run, servo, ctrl1, ctrl2)


print(chalk.green('Starting the program'))
while True:
    try:
        for ext in mods:
            ext.__run__()
    except KeyboardInterrupt:
        print(chalk.red('Stopping the program'))
        for ext in mods:
            ext.__stop__()
        break