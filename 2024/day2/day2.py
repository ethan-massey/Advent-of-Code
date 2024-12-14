lines = open("data.txt", "r").readlines()

reports = []
for line in lines:
    report = [int(i) for i in line.split(" ")]
    reports.append(report)

# part 1


def is_safely_increasing(report) -> bool:
    for i in range(1, len(report)):
        if report[i] <= report[i - 1] or not is_safe_jump(report[i], report[i - 1]):
            return False
    return True


def is_safely_decreasing(report) -> bool:
    for i in range(1, len(report)):
        if report[i] >= report[i - 1] or not is_safe_jump(report[i], report[i - 1]):
            return False
    return True


def is_safe_jump(num1, num2) -> bool:
    diff = abs(num1 - num2)
    return 1 <= diff <= 3


safe_reports = []
for report in reports:
    if is_safely_decreasing(report) or is_safely_increasing(report):
        safe_reports.append(report)

print(len(safe_reports))

# part 2

