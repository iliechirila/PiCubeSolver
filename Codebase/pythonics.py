from Motors.MotorsController import MotorsController
from Solvers.Solver import Solver
import RPi.GPIO as GPIO
import time

def main():
    # solver = Solver()
    # solver.cube.apply_alg_std("F' D' U B F2 L U' R B F2 R2 D2 F U L' R' F2 D U B' R B2 R' F R2 F' L2 D2 B R2")
    print("Setup step")
    print(input())

    motors_controller = MotorsController()

    motors_controller.add_pins_configuration("U",3,2,4)
    motors_controller.add_pins_configuration("D",18,15,14)
    motors_controller.add_pins_configuration("F",22,27,17)
    motors_controller.add_pins_configuration("B",11,9,10)
    motors_controller.add_pins_configuration("L",7,8,25)
    motors_controller.add_pins_configuration("R",21,20,16)

    print("Setup done")

    print("Solve")
    # q = input()
    # solver.solve_cube()

    # print("Wait for solve")
    q = input()
    
    while q != 'q':
        rpm = 90


        # motors_controller.command_stepper(("D", "cw"), rpm)
        # motors_controller.command_stepper(("D", "ccw"), rpm)
        # motors_controller.command_stepper(("D", "dt"), rpm)

        # time.sleep(1)
        # motors_controller.command_stepper(("F", "cw"), rpm)
        # motors_controller.command_stepper(("F", "ccw"), rpm)
        # motors_controller.command_stepper(("F", "dt"), rpm)

        # time.sleep(5)

        # motors_cont.command_stepper(("R", "cw"), rpm, rotation_pol=GPIO.LOW)
        # motors_cont.command_stepper(("R", "ccw"), rpm, rotation_pol=GPIO.HIGH)
        alg = [('U','cw'),('F','cw'),('L','cw'),('D','cw'),('B','cw'),('R','cw')]
        motors_controller.solve_cube(alg, rpm)

        print("Continue or q to quit")
        q = input()

    print("After next input, the GPIO will be reset")
    print(input())
    GPIO.cleanup()

if __name__ == "__main__":
    main()
