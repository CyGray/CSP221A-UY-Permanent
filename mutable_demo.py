class BuggyRobot:
    tasks = []

    def __init__(self, name):
        self.name = name


class CorrectedRobot:
    def __init__(self, name):
        self.name = name
        self.tasks = []


if __name__ == "__main__":
    first_buggy_robot = BuggyRobot("First Buggy Robot")
    second_buggy_robot = BuggyRobot("Second Buggy Robot")
    first_buggy_robot.tasks.append("salted nuts")
    print(f"Buggy shared tasks: {second_buggy_robot.tasks}")

    first_corrected_robot = CorrectedRobot("First Corrected Robot")
    second_corrected_robot = CorrectedRobot("Second Corrected Robot")
    first_corrected_robot.tasks.append("coated nuts")
    print(f"Corrected isolated tasks: {second_corrected_robot.tasks}")
